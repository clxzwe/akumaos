"""Hyprland master configuration component."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from akuma_generator.core.loader import load_yaml
from akuma_generator.core.logger import debug
from akuma_generator.core.output import OutputManager
from akuma_generator.core.renderer import render_template
from akuma_generator.core.validator import (
    validate_desktop_config,
    validate_hypr_syntax,
)
from akuma_generator.plugins.hypr.components.base import HyprComponent


class HyprlandConfigComponent(HyprComponent):
    """Component for generating Hyprland master hyprland.conf file."""

    @property
    def name(self) -> str:
        """Component identifier."""
        return "hyprland"

    def load(self, project_root: Path) -> Dict[str, Any]:
        """Load raw desktop YAML data."""
        config_path = project_root / "examples" / "desktop.yaml"
        return load_yaml(config_path)

    def validate(self, raw_data: Dict[str, Any]) -> Any:
        """Validate raw data against DesktopModel schema."""
        return validate_desktop_config(raw_data)

    def render(self, validated_data: Any, project_root: Path) -> str:
        """Render hyprland.conf master template."""
        template_path = project_root / "generator" / "templates" / "hyprland.conf.j2"
        if not template_path.exists():
            template_path = project_root / "templates" / "hyprland.conf.j2"
        context = {}
        return render_template(template_path, context)

    def get_output_path(
        self, project_root: Path, output_dir: Optional[Path] = None
    ) -> Path:
        """Get output destination path for hyprland.conf."""
        target_dir = output_dir or (Path.home() / ".config" / "hypr")
        return target_dir / "hyprland.conf"

    def generate(
        self,
        project_root: Path,
        dry_run: bool = False,
        backup: bool = False,
        overwrite: bool = True,
        output_dir: Optional[Path] = None,
    ) -> Path:
        """Execute full component generation lifecycle for master hyprland.conf."""
        output_path = self.get_output_path(project_root, output_dir=output_dir)
        if output_path.exists() and not dry_run:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_path = output_path.parent / f"{output_path.name}.bak_{timestamp}"
            debug(f"Creating timestamped backup of hyprland.conf: {backup_path}")
            backup_path.write_bytes(output_path.read_bytes())

        raw_data = self.load(project_root)
        validated_data = self.validate(raw_data)
        rendered_content = self.render(validated_data, project_root)

        validate_hypr_syntax(
            rendered_content, file_path=output_path if not dry_run else None
        )

        return OutputManager.write(
            rendered_content,
            output_path,
            dry_run=dry_run,
            backup=False,  # Timestamped backup handled above if exists
            overwrite=overwrite,
        )
