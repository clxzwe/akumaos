"""AkumaOS Generator Core Module."""

from akuma_generator.core.base_plugin import BasePlugin
from akuma_generator.core.loader import load_yaml
from akuma_generator.core.plugin_manager import PluginManager
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config

__all__ = [
    "BasePlugin",
    "PluginManager",
    "load_yaml",
    "render_template",
    "validate_desktop_config",
]
