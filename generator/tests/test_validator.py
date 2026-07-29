"""Tests for the desktop configuration validator module."""

import pytest
from pydantic import ValidationError

from akuma_generator.core.validator import validate_desktop_config


def test_validate_desktop_config_valid():
    """Test validating valid monitor data dictionary."""
    data = {
        "monitors": [
            {
                "name": "DP-1",
                "resolution": "2560x1440",
                "refresh": 165,
                "position": "0x0",
                "scale": 1,
            }
        ]
    }
    desktop = validate_desktop_config(data)
    assert len(desktop.monitors) == 1
    assert desktop.monitors[0].name == "DP-1"
    assert desktop.monitors[0].resolution == "2560x1440"
    assert desktop.monitors[0].refresh == 165


def test_validate_desktop_config_invalid():
    """Test validating invalid monitor data."""
    data = {"monitors": [{"name": "DP-1"}]}  # Missing required fields
    with pytest.raises(ValidationError):
        validate_desktop_config(data)
