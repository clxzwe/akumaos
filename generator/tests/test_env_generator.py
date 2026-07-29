"""Tests for environment configuration generation."""

from pathlib import Path

from typer.testing import CliRunner

from akuma_generator.cli import app
from akuma_generator.core.loader import load_yaml
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config

runner = CliRunner()


def test_env_yaml_loading(tmp_path):
    """Test loading environment section from YAML."""
    yaml_file = tmp_path / "desktop.yaml"
    yaml_file.write_text("environment:\n  XCURSOR_SIZE: 24\n", encoding="utf-8")

    data = load_yaml(yaml_file)
    assert "environment" in data
    assert data["environment"]["XCURSOR_SIZE"] == 24


def test_env_validation():
    """Test validating environment configuration with DesktopModel."""
    data = {
        "environment": {
            "XCURSOR_SIZE": 24,
            "HYPRCURSOR_SIZE": 24,
            "GTK_THEME": "Adwaita-dark",
        }
    }
    desktop = validate_desktop_config(data)
    assert desktop.environment["XCURSOR_SIZE"] == 24
    assert desktop.environment["GTK_THEME"] == "Adwaita-dark"


def test_env_rendering(tmp_path):
    """Test rendering env.conf.j2 template."""
    template_file = tmp_path / "env.conf.j2"
    template_file.write_text(
        "{% for k, v in environment.items() %}env = {{ k }},{{ v }}\n{% endfor %}",
        encoding="utf-8",
    )

    context = {"environment": {"XCURSOR_SIZE": 24, "GTK_THEME": "Adwaita-dark"}}
    result = render_template(template_file, context)
    assert "env = XCURSOR_SIZE,24" in result
    assert "env = GTK_THEME,Adwaita-dark" in result


def test_cli_generate_environment(tmp_path, monkeypatch):
    """Test CLI generate command for environment component."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    result = runner.invoke(app, ["generate", "--component", "environment"])
    assert result.exit_code == 0
    assert "✓ environment" in result.stdout

    output_file = repo_root / "config" / "hypr" / "generated" / "env.conf"
    assert output_file.exists()

    content = output_file.read_text(encoding="utf-8")
    assert "env = XCURSOR_SIZE,24" in content
    assert "env = HYPRCURSOR_SIZE,24" in content
    assert "env = GTK_THEME,Adwaita-dark" in content


def test_regression_monitors_generation(tmp_path, monkeypatch):
    """Regression test ensuring monitors generation remains identical."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    result = runner.invoke(app, ["generate", "--component", "monitors"])
    assert result.exit_code == 0

    output_file = repo_root / "config" / "hypr" / "generated" / "monitors.conf"
    assert output_file.exists()

    content = output_file.read_text(encoding="utf-8")
    assert "monitor=DP-1,2560x1440@165,0x0,1" in content
    assert "monitor=HDMI-A-1,1920x1080@75,2560x0,1" in content
