"""Test import and package initialization for akuma_generator."""

import akuma_generator
from akuma_generator import cli, loader, models, renderer, validator


def test_package_import() -> None:
    """Test that akuma_generator package imports successfully."""
    assert akuma_generator.__version__ == "0.1.0"


def test_modules_import() -> None:
    """Test that all core submodules import successfully."""
    assert cli.app is not None
    assert hasattr(loader, "load_theme")
    assert hasattr(validator, "validate_theme")
    assert hasattr(renderer, "render_template")
    assert hasattr(models, "ThemeModel")
