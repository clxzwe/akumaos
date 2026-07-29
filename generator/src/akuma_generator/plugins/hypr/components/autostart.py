"""Hyprland autostart configuration component."""

import shutil
from pathlib import Path
from typing import Any, Dict, Optional

from akuma_generator.core.loader import load_yaml
from akuma_generator.core.logger import warning
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config
from akuma_generator.plugins.hypr.components.base import HyprComponent


class AutostartComponent(HyprComponent):
    """Component for generating Hyprland autostart configuration."""

    @property
    def name(self) -> str:
        """Component identifier."""
        return "autostart"

    def load(self, project_root: Path) -> Dict[str, Any]:
        """Load raw desktop YAML data."""
        config_path = project_root / "examples" / "desktop.yaml"
        return load_yaml(config_path)

    def validate(self, raw_data: Dict[str, Any]) -> Any:
        """Validate raw data against DesktopModel schema."""
        return validate_desktop_config(raw_data)

    def render(self, validated_data: Any, project_root: Path) -> str:
        """Render autostart Jinja2 template."""
        template_path = project_root / "generator" / "templates" / "autostart.conf.j2"
        if not template_path.exists():
            template_path = project_root / "templates" / "autostart.conf.j2"

        mpvpaper_installed = bool(shutil.which("mpvpaper"))
        if not mpvpaper_installed:
            warning("mpvpaper is not installed. Video wallpaper autostart skipped.")

        wallpaper_path = "/home/akuma/Downloads/plana-blue-archive-1-moewalls-com.mp4"
        if hasattr(validated_data, "autostart") and getattr(
            validated_data.autostart, "wallpaper_path", ""
        ).endswith(".mp4"):
            wallpaper_path = validated_data.autostart.wallpaper_path

        context = {
            "autostart": validated_data.autostart,
            "mpvpaper_installed": mpvpaper_installed,
            "wallpaper_path": wallpaper_path,
        }
        return render_template(template_path, context)

    def get_output_path(
        self, project_root: Path, output_dir: Optional[Path] = None
    ) -> Path:
        """Get output destination path for autostart.conf."""
        target_dir = output_dir or (Path.home() / ".config" / "hypr" / "config")
        return target_dir / "autostart.conf"
