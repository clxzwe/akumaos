"""AkumaOS Generator Core Module."""

from akuma_generator.core.base_plugin import BasePlugin
from akuma_generator.core.errors import (
    AkumaError,
    FilesystemError,
    PluginError,
    SchemaError,
    TemplateError,
    ValidationError,
)
from akuma_generator.core.loader import load_yaml
from akuma_generator.core.logger import debug, error, info, setup_logger, warning
from akuma_generator.core.output import OutputManager
from akuma_generator.core.plugin_manager import PluginManager
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config

__all__ = [
    "AkumaError",
    "BasePlugin",
    "FilesystemError",
    "OutputManager",
    "PluginError",
    "PluginManager",
    "SchemaError",
    "TemplateError",
    "ValidationError",
    "debug",
    "error",
    "info",
    "load_yaml",
    "render_template",
    "setup_logger",
    "validate_desktop_config",
    "warning",
]
