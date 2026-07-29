"""Hyprland compositor plugin implementation."""

from pathlib import Path
from typing import Any, Dict

from akuma_generator.core.base_plugin import BasePlugin
from akuma_generator.core.loader import load_yaml
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config


class HyprPlugin(BasePlugin):
    """Plugin for generating Hyprland compositor configurations."""

    @property
    def name(self) -> str:
        """Plugin component name."""
        return "hypr"

    def load(self, project_root: Path, component: str, **kwargs: Any) -> Dict[str, Any]:
        """Load raw configuration data for Hyprland component."""
        config_path = project_root / "examples" / "desktop.yaml"
        return load_yaml(config_path)

    def validate(self, raw_data: Dict[str, Any], component: str, **kwargs: Any) -> Any:
        """Validate raw data against DesktopModel schema."""
        return validate_desktop_config(raw_data)

    def render(
        self,
        validated_data: Any,
        component: str,
        project_root: Path,
        **kwargs: Any,
    ) -> str:
        """Render Hyprland component template."""
        if component == "monitors":
            template_path = (
                project_root / "generator" / "templates" / "monitors.conf.j2"
            )
            context = {"monitors": [m.model_dump() for m in validated_data.monitors]}
        elif component == "environment":
            template_path = project_root / "generator" / "templates" / "env.conf.j2"
            context = {"environment": validated_data.environment}
        else:
            raise ValueError(f"Unsupported Hyprland component: {component}")

        return render_template(template_path, context)

    def get_output_path(self, project_root: Path, component: str) -> Path:
        """Get output file destination for Hyprland component."""
        if component == "monitors":
            filename = "monitors.conf"
        elif component == "environment":
            filename = "env.conf"
        else:
            filename = f"{component}.conf"

        return project_root / "config" / "hypr" / "generated" / filename

    @classmethod
    def generate_monitors(cls, project_root: Path) -> Path:
        """Backward-compatible helper method for monitor generation."""
        instance = cls()
        return instance.generate(project_root, component="monitors")
