"""Tests for the configuration loader module."""

import pytest

from akuma_generator.core.loader import load_yaml


def test_load_yaml_valid(tmp_path):
    """Test loading a valid YAML file."""
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text("monitors:\n  - name: DP-1\n", encoding="utf-8")

    data = load_yaml(yaml_file)
    assert "monitors" in data
    assert data["monitors"][0]["name"] == "DP-1"


def test_load_yaml_not_found():
    """Test loading a non-existent YAML file."""
    with pytest.raises(FileNotFoundError):
        load_yaml("non_existent_path.yaml")
