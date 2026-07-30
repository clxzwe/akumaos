"""Desktop configuration deployment and lifecycle management module."""

import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

from akuma_generator.core.logger import info, warning
from akuma_generator.core.plugin_manager import PluginManager
from akuma_generator.core.validator import check_hyprctl_configerrors
from akuma_generator.plugins.hypr.component_registry import ComponentRegistry

DOCTOR_DEPENDENCIES = [
    "hyprland",
    "ghostty",
    "firefox",
    "nautilus",
    "waybar",
    "wofi",
    "mako",
    "mpvpaper",
    "swayosd-server",
]


def check_dependencies() -> List[Tuple[str, bool]]:
    """Check availability of desktop dependencies.

    Returns:
        List of tuples (dependency_name, is_installed).
    """
    results = []
    for dep in DOCTOR_DEPENDENCIES:
        is_installed = shutil.which(dep) is not None
        results.append((dep, is_installed))
    return results


def is_hyprland_running() -> bool:
    """Check if Hyprland compositor is currently active."""
    if os.environ.get("HYPRLAND_INSTANCE_SIGNATURE"):
        return True
    if shutil.which("hyprctl"):
        try:
            res = subprocess.run(
                ["hyprctl", "instances"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            return res.returncode == 0
        except Exception:
            return False
    return False


def reload_hyprland(dry_run: bool = False) -> bool:
    """Trigger hyprctl reload if Hyprland is active.

    Args:
        dry_run: If True, log execution without running command.

    Returns:
        bool: True if reloaded successfully, False if skipped or failed.
    """
    if not is_hyprland_running():
        warning("Hyprland is not running. Skipping reload.")
        return False

    if dry_run:
        info("[DRY-RUN] Would execute: hyprctl reload")
        return True

    try:
        subprocess.run(["hyprctl", "reload"], check=True, capture_output=True)
        info("Successfully reloaded Hyprland configuration.")
        return True
    except (subprocess.SubprocessError, OSError) as e:
        warning(f"Hyprland reload failed: {e}. Skipping reload.")
        return False


def create_backup(
    hypr_dir: Optional[Path] = None,
    dry_run: bool = False,
) -> Path:
    """Create timestamped backup of hyprland.conf and config directory.

    Args:
        hypr_dir: Base ~/.config/hypr path (defaults to Path.home() / .config / hypr).
        dry_run: If True, simulate backup without writing files.

    Returns:
        Path: Path to created backup directory.
    """
    base_hypr = hypr_dir or (Path.home() / ".config" / "hypr")
    backups_dir = base_hypr / "backups"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target_backup_dir = backups_dir / timestamp

    if dry_run:
        info(f"[DRY-RUN] Would create backup directory at: {target_backup_dir}")
        return target_backup_dir

    target_backup_dir.mkdir(parents=True, exist_ok=True)

    src_hyprland = base_hypr / "hyprland.conf"
    if src_hyprland.exists():
        shutil.copy2(src_hyprland, target_backup_dir / "hyprland.conf")
        info(f"Backed up hyprland.conf to {target_backup_dir / 'hyprland.conf'}")

    src_config = base_hypr / "config"
    if src_config.exists() and src_config.is_dir():
        dest_config = target_backup_dir / "config"
        shutil.copytree(src_config, dest_config, dirs_exist_ok=True)
        info(f"Backed up config/ to {dest_config}")

    return target_backup_dir


def restore_newest_backup(
    hypr_dir: Optional[Path] = None,
    dry_run: bool = False,
) -> Optional[Path]:
    """Restore configuration from the newest backup directory.

    Args:
        hypr_dir: Base ~/.config/hypr path (defaults to Path.home() / .config / hypr).
        dry_run: If True, simulate restoration without modifying disk.

    Returns:
        Optional[Path]: Restored backup directory path, or None if no backups exist.
    """
    base_hypr = hypr_dir or (Path.home() / ".config" / "hypr")
    backups_dir = base_hypr / "backups"

    if not backups_dir.exists() or not backups_dir.is_dir():
        warning(f"No backups directory found at {backups_dir}")
        return None

    entries = [d for d in backups_dir.iterdir() if d.is_dir()]
    if not entries:
        warning(f"No backups found in {backups_dir}")
        return None

    newest_backup = sorted(entries, key=lambda p: p.name)[-1]
    info(f"Selected newest backup for restoration: {newest_backup}")

    if dry_run:
        info(f"[DRY-RUN] Would restore from {newest_backup} to {base_hypr}")
        return newest_backup

    src_hyprland = newest_backup / "hyprland.conf"
    if src_hyprland.exists():
        shutil.copy2(src_hyprland, base_hypr / "hyprland.conf")
        info(f"Restored {src_hyprland} -> {base_hypr / 'hyprland.conf'}")

    src_config = newest_backup / "config"
    if src_config.exists() and src_config.is_dir():
        dest_config = base_hypr / "config"
        dest_config.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src_config, dest_config, dirs_exist_ok=True)
        info(f"Restored {src_config} -> {dest_config}")

    reload_hyprland(dry_run=dry_run)
    return newest_backup


def apply_desktop_config(
    project_root: Path,
    hypr_dir: Optional[Path] = None,
    dry_run: bool = False,
) -> None:
    """Orchestrate full desktop application: backup, generate, update master, reload.

    Args:
        project_root: Repository root path.
        hypr_dir: Base ~/.config/hypr path (defaults to Path.home() / .config / hypr).
        dry_run: If True, simulate all operations without modifying disk.
    """
    base_hypr = hypr_dir or (Path.home() / ".config" / "hypr")
    config_dir = base_hypr / "config"

    # 1 & 2. Backup existing configs
    create_backup(hypr_dir=base_hypr, dry_run=dry_run)

    # 3. Generate configs into ~/.config/hypr/config
    plugin = PluginManager.get("hypr")
    all_components = ComponentRegistry.list_components()

    for comp in all_components:
        if comp == "hyprland":
            continue
        plugin.generate(
            project_root=project_root,
            component=comp,
            dry_run=dry_run,
            output_dir=config_dir,
        )

    # 4. Update hyprland.conf
    plugin.generate(
        project_root=project_root,
        component="hyprland",
        dry_run=dry_run,
        output_dir=base_hypr,
    )

    # 5. Reload Hyprland
    reload_hyprland(dry_run=dry_run)

    # 6. Check for runtime configuration errors
    if not dry_run:
        check_hyprctl_configerrors()
