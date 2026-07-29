"""Unit tests for Sprint 2 AkumaOS CLI and deployment workflow."""

import shutil
from pathlib import Path

from typer.testing import CliRunner

from akuma_generator.cli import app
from akuma_generator.core.deployment import create_backup, restore_newest_backup
from akuma_generator.plugins.hypr.components.autostart import AutostartComponent

runner = CliRunner()


def test_doctor_command():
    """Test `akuma doctor` checks all required system dependencies."""
    result = runner.invoke(app, ["doctor"])
    assert result.exit_code == 0
    assert "AkumaOS Dependency Check:" in result.stdout
    for dep in [
        "hyprland",
        "ghostty",
        "firefox",
        "nautilus",
        "waybar",
        "wofi",
        "mako",
        "mpvpaper",
        "swayosd-server",
    ]:
        assert dep in result.stdout


def test_apply_command(tmp_path, monkeypatch):
    """Test `akuma apply` generates configs, updates hyprland.conf, and backs up."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: fake_home)

    result = runner.invoke(app, ["apply"])
    assert result.exit_code == 0
    assert "Configuration applied successfully" in result.stdout

    config_dir = fake_home / ".config" / "hypr" / "config"
    assert config_dir.exists()
    for conf in [
        "monitors.conf",
        "env.conf",
        "general.conf",
        "input.conf",
        "decoration.conf",
        "animations.conf",
        "binds.conf",
        "autostart.conf",
        "groups.conf",
        "rules.conf",
    ]:
        assert (config_dir / conf).exists()

    master_conf = fake_home / ".config" / "hypr" / "hyprland.conf"
    assert master_conf.exists()


def test_apply_dry_run(tmp_path, monkeypatch):
    """Test `akuma apply --dry-run` does not modify disk."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: fake_home)

    result = runner.invoke(app, ["apply", "--dry-run"])
    assert result.exit_code == 0

    hypr_dir = fake_home / ".config" / "hypr"
    assert not hypr_dir.exists() or not (hypr_dir / "hyprland.conf").exists()


def test_backup_command(tmp_path, monkeypatch):
    """Test `akuma backup` creates timestamped backup dir."""
    fake_home = tmp_path / "home"
    fake_hypr = fake_home / ".config" / "hypr"
    fake_config = fake_hypr / "config"
    fake_config.mkdir(parents=True)

    (fake_hypr / "hyprland.conf").write_text("# master config")
    (fake_config / "monitors.conf").write_text("# monitors config")

    backup_dir = create_backup(hypr_dir=fake_hypr)
    assert backup_dir.exists()
    assert (backup_dir / "hyprland.conf").exists()
    assert (backup_dir / "hyprland.conf").read_text() == "# master config"
    assert (backup_dir / "config" / "monitors.conf").exists()
    assert (backup_dir / "config" / "monitors.conf").read_text() == "# monitors config"


def test_restore_command(tmp_path, monkeypatch):
    """Test `akuma restore` restores configuration from newest backup."""
    fake_home = tmp_path / "home"
    fake_hypr = fake_home / ".config" / "hypr"
    backups_dir = fake_hypr / "backups"

    b1 = backups_dir / "2026-01-01_10-00-00"
    b1.mkdir(parents=True)
    (b1 / "hyprland.conf").write_text("# old master")

    b2 = backups_dir / "2026-01-02_10-00-00"
    (b2 / "config").mkdir(parents=True)
    (b2 / "hyprland.conf").write_text("# new master")
    (b2 / "config" / "monitors.conf").write_text("# new monitors")

    restored_dir = restore_newest_backup(hypr_dir=fake_hypr)
    assert restored_dir == b2

    assert (fake_hypr / "hyprland.conf").read_text() == "# new master"
    assert (fake_hypr / "config" / "monitors.conf").read_text() == "# new monitors"


def test_hyprland_conf_rewriting(tmp_path, monkeypatch):
    """Test hyprland.conf rewriting with source lines and timestamped backup."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    fake_home = tmp_path / "home"
    fake_hypr = fake_home / ".config" / "hypr"
    fake_hypr.mkdir(parents=True)

    old_hyprland = fake_hypr / "hyprland.conf"
    old_hyprland.write_text("# Original user config")

    monkeypatch.setattr(Path, "home", lambda: fake_home)

    result = runner.invoke(app, ["apply"])
    assert result.exit_code == 0

    content = old_hyprland.read_text()
    expected_sources = [
        "source = ~/.cache/wal/colors-hyprland.conf",
        "source = ~/.config/hypr/config/monitors.conf",
        "source = ~/.config/hypr/config/env.conf",
        "source = ~/.config/hypr/config/autostart.conf",
        "source = ~/.config/hypr/config/general.conf",
        "source = ~/.config/hypr/config/decoration.conf",
        "source = ~/.config/hypr/config/animations.conf",
        "source = ~/.config/hypr/config/input.conf",
        "source = ~/.config/hypr/config/groups.conf",
        "source = ~/.config/hypr/config/binds.conf",
        "source = ~/.config/hypr/config/rules.conf",
    ]
    for src in expected_sources:
        assert src in content

    # Verify backup of old hyprland.conf was created
    bak_files = list(fake_hypr.glob("hyprland.conf.bak_*"))
    assert len(bak_files) > 0
    assert bak_files[0].read_text() == "# Original user config"


def test_wallpaper_generation(monkeypatch):
    """Test video wallpaper generation with mpvpaper and exclusion of swww."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    component = AutostartComponent()
    raw = component.load(repo_root)
    validated = component.validate(raw)

    # 1. Test when mpvpaper is installed
    monkeypatch.setattr(
        shutil, "which", lambda cmd: "/usr/bin/mpvpaper" if cmd == "mpvpaper" else None
    )
    rendered = component.render(validated, repo_root)

    assert "mpvpaper" in rendered
    expected_cmd = (
        "exec-once = mpvpaper '*' "
        "/home/akuma/Downloads/plana-blue-archive-1-moewalls-com.mp4"
    )
    assert expected_cmd in rendered
    assert "swww" not in rendered

    # 2. Test when mpvpaper is not installed
    monkeypatch.setattr(shutil, "which", lambda cmd: None)
    rendered_no_mpv = component.render(validated, repo_root)

    assert "mpvpaper" not in rendered_no_mpv
    assert "swww" not in rendered_no_mpv
