"""Hyprland decoration configuration component."""

from pathlib import Path
from typing import Any, Dict, Optional

from akuma_generator.core.loader import load_yaml
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config
from akuma_generator.plugins.hypr.components.base import HyprComponent


class DecorationComponent(HyprComponent):
    """Component for generating Hyprland decoration configuration."""

    @property
    def name(self) -> str:
        """Component identifier."""
        return "decoration"

    def load(self, project_root: Path) -> Dict[str, Any]:
        """Load raw desktop YAML data."""
        config_path = project_root / "examples" / "desktop.yaml"
        return load_yaml(config_path)

    def validate(self, raw_data: Dict[str, Any]) -> Any:
        """Validate raw data against DesktopModel schema."""
        return validate_desktop_config(raw_data)

    def render(self, validated_data: Any, project_root: Path) -> str:
        """Render decoration Jinja2 template."""
        template_path = project_root / "generator" / "templates" / "decoration.conf.j2"
        if not template_path.exists():
            template_path = project_root / "templates" / "decoration.conf.j2"
        context = {"decoration": validated_data.decoration}
        return render_template(template_path, context)

    def get_output_path(
        self, project_root: Path, output_dir: Optional[Path] = None
    ) -> Path:
        """Get output destination path for decoration.conf."""
        target_dir = output_dir or (Path.home() / ".config" / "hypr" / "config")
        return target_dir / "decoration.conf"
