"""Tests for the desktop configuration validator module."""

import pytest

from akuma_generator.core.errors import ValidationError
from akuma_generator.core.validator import (
    validate_desktop_config,
    validate_hypr_syntax,
)


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


def test_validate_hypr_syntax_pseudotile_rejected():
    """Regression test ensuring pseudotile directive raises ValidationError."""
    invalid_cfg = "dwindle {\n    pseudotile = true\n}\n"
    with pytest.raises(ValidationError, match="pseudotile"):
        validate_hypr_syntax(invalid_cfg)


def test_validate_hypr_syntax_togglesplit_rejected():
    """Test ensuring standalone togglesplit dispatcher raises ValidationError."""
    invalid_cfg = "bind = SUPER, M, togglesplit\n"
    with pytest.raises(ValidationError, match="togglesplit"):
        validate_hypr_syntax(invalid_cfg)


def test_validate_hypr_syntax_valid_config():
    """Test valid Hyprland 0.56.x syntax passes validation."""
    valid_cfg = (
        "dwindle {\n    preserve_split = true\n}\n"
        "bind = SUPER, M, layoutmsg, togglesplit\n"
    )
    validate_hypr_syntax(valid_cfg)


def test_generated_components_no_obsolete_directives():
    """Audit registered components to ensure no obsolete directives are generated."""
    from pathlib import Path

    from akuma_generator.plugins.hypr.component_registry import ComponentRegistry

    repo_root = Path(__file__).resolve().parent.parent.parent
    for name in ComponentRegistry.list_components():
        comp = ComponentRegistry.get(name)
        raw = comp.load(repo_root)
        validated = comp.validate(raw)
        rendered = comp.render(validated, repo_root)

        assert "pseudotile" not in rendered, f"Component {name} emitted pseudotile"
        assert (
            "bind = SUPER, M, togglesplit" not in rendered
        ), f"Component {name} emitted standalone togglesplit dispatcher"
        validate_hypr_syntax(rendered)
