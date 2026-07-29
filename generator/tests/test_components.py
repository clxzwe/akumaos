"""Unit tests for all Sprint 1 Hyprland components."""

from pathlib import Path

from typer.testing import CliRunner

from akuma_generator.cli import app
from akuma_generator.plugins.hypr.component_registry import ComponentRegistry

runner = CliRunner()


def test_all_components_registered():
    """Test that all 9 components are registered in ComponentRegistry."""
    ComponentRegistry.clear()
    components = ComponentRegistry.list_components()
    expected = [
        "animations",
        "autostart",
        "binds",
        "decoration",
        "environment",
        "general",
        "hyprland",
        "input",
        "monitors",
    ]
    assert components == expected


def test_cli_generate_default_all(monkeypatch):
    """Test calling `akuma generate` without flags generates all components."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    result = runner.invoke(app, ["generate"])
    assert result.exit_code == 0
    assert "Generating Hyprland..." in result.stdout
    assert "✓ animations" in result.stdout
    assert "✓ autostart" in result.stdout
    assert "✓ binds" in result.stdout
    assert "✓ decoration" in result.stdout
    assert "✓ environment" in result.stdout
    assert "✓ general" in result.stdout
    assert "✓ hyprland" in result.stdout
    assert "✓ input" in result.stdout
    assert "✓ monitors" in result.stdout
    assert "Done." in result.stdout


def test_component_outputs_exist(monkeypatch):
    """Test that all generated output files exist with non-empty content."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    runner.invoke(app, ["generate"])

    gen_dir = repo_root / "config" / "hypr" / "generated"
    for comp_file in [
        "monitors.conf",
        "env.conf",
        "general.conf",
        "input.conf",
        "decoration.conf",
        "animations.conf",
        "autostart.conf",
        "binds.conf",
        "hyprland.conf",
    ]:
        path = gen_dir / comp_file
        assert path.exists(), f"Missing output file: {comp_file}"
        assert path.stat().st_size > 0, f"Empty output file: {comp_file}"
