"""Hyprland input configuration component."""

from pathlib import Path
from typing import Any, Dict

from akuma_generator.core.loader import load_yaml
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config
from akuma_generator.plugins.hypr.components.base import HyprComponent


class InputComponent(HyprComponent):
    """Component for generating Hyprland input configuration."""

    @property
    def name(self) -> str:
        """Component identifier."""
        return "input"

    def load(self, project_root: Path) -> Dict[str, Any]:
        """Load raw desktop YAML data."""
        config_path = project_root / "examples" / "desktop.yaml"
        return load_yaml(config_path)

    def validate(self, raw_data: Dict[str, Any]) -> Any:
        """Validate raw data against DesktopModel schema."""
        return validate_desktop_config(raw_data)

    def render(self, validated_data: Any, project_root: Path) -> str:
        """Render input Jinja2 template."""
        template_path = project_root / "generator" / "templates" / "input.conf.j2"
        context = {"input": validated_data.input}
        return render_template(template_path, context)

    def get_output_path(self, project_root: Path) -> Path:
        """Get output destination path for input.conf."""
        return project_root / "config" / "hypr" / "generated" / "input.conf"
