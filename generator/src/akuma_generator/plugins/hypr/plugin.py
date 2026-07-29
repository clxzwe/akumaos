"""Hyprland compositor plugin implementation."""

from pathlib import Path
from typing import Any, Dict

from akuma_generator.core.base_plugin import BasePlugin
from akuma_generator.plugins.hypr.component_registry import ComponentRegistry


class HyprPlugin(BasePlugin):
    """Plugin for generating Hyprland configurations via component dispatch."""

    @property
    def name(self) -> str:
        """Plugin component name."""
        return "hypr"

    def load(self, project_root: Path, component: str, **kwargs: Any) -> Dict[str, Any]:
        """Delegate load stage to registered sub-component."""
        comp_obj = ComponentRegistry.get(component)
        return comp_obj.load(project_root)

    def validate(self, raw_data: Dict[str, Any], component: str, **kwargs: Any) -> Any:
        """Delegate validate stage to registered sub-component."""
        comp_obj = ComponentRegistry.get(component)
        return comp_obj.validate(raw_data)

    def render(
        self,
        validated_data: Any,
        component: str,
        project_root: Path,
        **kwargs: Any,
    ) -> str:
        """Delegate render stage to registered sub-component."""
        comp_obj = ComponentRegistry.get(component)
        return comp_obj.render(validated_data, project_root)

    def get_output_path(self, project_root: Path, component: str) -> Path:
        """Delegate output path determination to registered sub-component."""
        comp_obj = ComponentRegistry.get(component)
        return comp_obj.get_output_path(project_root)

    def generate(
        self,
        project_root: Path,
        component: str,
        dry_run: bool = False,
        backup: bool = False,
        overwrite: bool = True,
        **kwargs: Any,
    ) -> Path:
        """Dispatch component generation to target registered sub-component."""
        comp_obj = ComponentRegistry.get(component)
        return comp_obj.generate(
            project_root=project_root,
            dry_run=dry_run,
            backup=backup,
            overwrite=overwrite,
        )

    @classmethod
    def generate_monitors(cls, project_root: Path) -> Path:
        """Backward-compatible helper method for monitor generation."""
        instance = cls()
        return instance.generate(project_root, component="monitors")
