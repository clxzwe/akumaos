"""Unit tests for CLI dry-run and verbose modes."""

from pathlib import Path

from typer.testing import CliRunner

from akuma_generator.cli import app

runner = CliRunner()


def test_cli_dry_run_monitors(tmp_path, monkeypatch, capsys):
    """Test CLI dry-run mode for monitors component."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    result = runner.invoke(app, ["generate", "--component", "monitors", "--dry-run"])
    assert result.exit_code == 0
    assert "monitor=DP-1,2560x1440@165,0x0,1" in result.stdout
    assert "DRY-RUN" in result.stdout


def test_cli_verbose_logging(monkeypatch):
    """Test CLI verbose logging option."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    result = runner.invoke(
        app, ["generate", "--component", "monitors", "--dry-run", "--verbose"]
    )
    assert result.exit_code == 0
