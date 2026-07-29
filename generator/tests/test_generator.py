"""Tests for CLI generate command and output file generation."""

from pathlib import Path

from typer.testing import CliRunner

from akuma_generator.cli import app

runner = CliRunner()


def test_cli_generate_monitors(tmp_path, monkeypatch):
    """Test full CLI generate command for monitors component."""
    # Set CWD to repo root so _find_project_root works
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    result = runner.invoke(app, ["generate", "--component", "monitors"])
    assert result.exit_code == 0
    assert "Generated:" in result.stdout

    output_file = repo_root / "config" / "hypr" / "generated" / "monitors.conf"
    assert output_file.exists()

    content = output_file.read_text(encoding="utf-8")
    assert "monitor=DP-1,2560x1440@165,0x0,1" in content
    assert "monitor=HDMI-A-1,1920x1080@75,2560x0,1" in content
