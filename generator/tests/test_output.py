"""Unit tests for OutputManager abstraction."""

import pytest

from akuma_generator.core.errors import FilesystemError
from akuma_generator.core.output import OutputManager


def test_write_standard(tmp_path):
    """Test OutputManager standard file writing."""
    out_file = tmp_path / "test.conf"
    result = OutputManager.write("hello=world\n", out_file)

    assert result == out_file
    assert out_file.exists()
    assert out_file.read_text(encoding="utf-8") == "hello=world\n"


def test_write_backup(tmp_path):
    """Test OutputManager backup mode."""
    out_file = tmp_path / "test.conf"
    out_file.write_text("old_content\n", encoding="utf-8")

    OutputManager.write("new_content\n", out_file, backup=True)

    assert out_file.read_text(encoding="utf-8") == "new_content\n"
    bak_file = tmp_path / "test.conf.bak"
    assert bak_file.exists()
    assert bak_file.read_text(encoding="utf-8") == "old_content\n"


def test_write_no_overwrite(tmp_path):
    """Test OutputManager overwrite=False raises FilesystemError."""
    out_file = tmp_path / "test.conf"
    out_file.write_text("existing\n", encoding="utf-8")

    with pytest.raises(FilesystemError):
        OutputManager.write("new\n", out_file, overwrite=False)


def test_write_dry_run(tmp_path, capsys):
    """Test OutputManager dry-run mode prints content without writing."""
    out_file = tmp_path / "dry_run_test.conf"

    result = OutputManager.write("dry_run_content\n", out_file, dry_run=True)

    assert result == out_file
    assert not out_file.exists()

    captured = capsys.readouterr()
    assert "dry_run_content" in captured.out
    assert "DRY-RUN" in captured.out
