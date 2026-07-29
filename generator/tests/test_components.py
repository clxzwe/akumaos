"""Unit tests for Hyprland components registration and generation."""

from pathlib import Path

from typer.testing import CliRunner

from akuma_generator.cli import app
from akuma_generator.plugins.hypr.component_registry import ComponentRegistry

runner = CliRunner()


def test_all_components_registered():
    """Test that all 11 components are registered in ComponentRegistry."""
    ComponentRegistry.clear()
    components = ComponentRegistry.list_components()
    expected = [
        "animations",
        "autostart",
        "binds",
        "decoration",
        "environment",
        "general",
        "groups",
        "hyprland",
        "input",
        "monitors",
        "rules",
    ]
    assert components == expected


def test_cli_generate_default_all(tmp_path, monkeypatch):
    """Test calling `akuma generate` without flags generates all components."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: fake_home)

    result = runner.invoke(app, ["generate"])
    assert result.exit_code == 0
    assert "Generating Hyprland..." in result.stdout
    assert "✓ animations" in result.stdout
    assert "✓ autostart" in result.stdout
    assert "✓ binds" in result.stdout
    assert "✓ decoration" in result.stdout
    assert "✓ environment" in result.stdout
    assert "✓ general" in result.stdout
    assert "✓ groups" in result.stdout
    assert "✓ hyprland" in result.stdout
    assert "✓ input" in result.stdout
    assert "✓ monitors" in result.stdout
    assert "✓ rules" in result.stdout
    assert "Done." in result.stdout


def test_component_outputs_exist(tmp_path, monkeypatch):
    """Test generated output files exist in ~/.config/hypr/config."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: fake_home)

    runner.invoke(app, ["generate"])

    config_dir = fake_home / ".config" / "hypr" / "config"
    for comp_file in [
        "monitors.conf",
        "env.conf",
        "general.conf",
        "input.conf",
        "decoration.conf",
        "animations.conf",
        "autostart.conf",
        "binds.conf",
        "groups.conf",
        "rules.conf",
    ]:
        path = config_dir / comp_file
        assert path.exists(), f"Missing output file: {comp_file}"
        assert path.stat().st_size > 0, f"Empty output file: {comp_file}"

    master_path = fake_home / ".config" / "hypr" / "hyprland.conf"
    assert master_path.exists(), "Missing master hyprland.conf"
    assert master_path.stat().st_size > 0
