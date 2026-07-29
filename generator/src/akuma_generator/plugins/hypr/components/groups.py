"""Hyprland groups configuration component."""

from pathlib import Path
from typing import Any, Dict, Optional

from akuma_generator.core.loader import load_yaml
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config
from akuma_generator.plugins.hypr.components.base import HyprComponent


class GroupsComponent(HyprComponent):
    """Component for generating Hyprland window groups configuration."""

    @property
    def name(self) -> str:
        """Component identifier."""
        return "groups"

    def load(self, project_root: Path) -> Dict[str, Any]:
        """Load raw desktop YAML data."""
        config_path = project_root / "examples" / "desktop.yaml"
        if config_path.exists():
            return load_yaml(config_path)
        return {}

    def validate(self, raw_data: Dict[str, Any]) -> Any:
        """Validate raw data against DesktopModel schema."""
        return validate_desktop_config(raw_data)

    def render(self, validated_data: Any, project_root: Path) -> str:
        """Render groups Jinja2 template."""
        template_path = project_root / "generator" / "templates" / "groups.conf.j2"
        if not template_path.exists():
            template_path = project_root / "templates" / "groups.conf.j2"
        context = {}
        if template_path.exists():
            return render_template(template_path, context)
        return "# AkumaOS Hyprland window groups configuration (placeholder)\n"

    def get_output_path(
        self, project_root: Path, output_dir: Optional[Path] = None
    ) -> Path:
        """Get output destination path for groups.conf."""
        target_dir = output_dir or (Path.home() / ".config" / "hypr" / "config")
        return target_dir / "groups.conf"
