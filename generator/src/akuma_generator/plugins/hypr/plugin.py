"""Hyprland compositor plugin implementation."""

from pathlib import Path

from akuma_generator.core.loader import load_yaml
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import validate_desktop_config


class HyprPlugin:
    """Plugin for generating Hyprland compositor configurations."""

    @staticmethod
    def generate_monitors(project_root: Path) -> Path:
        """Generate Hyprland monitors configuration file.

        Args:
            project_root: Root directory of the AkumaOS repository.

        Returns:
            Path: Path to the generated monitors configuration file.
        """
        config_path = project_root / "examples" / "desktop.yaml"
        template_path = project_root / "generator" / "templates" / "monitors.conf.j2"
        output_dir = project_root / "config" / "hypr" / "generated"
        output_file = output_dir / "monitors.conf"

        raw_data = load_yaml(config_path)
        validated_desktop = validate_desktop_config(raw_data)

        context = {"monitors": [m.model_dump() for m in validated_desktop.monitors]}
        rendered_content = render_template(template_path, context)

        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(rendered_content)

        return output_file
