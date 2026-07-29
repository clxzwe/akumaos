"""Abstract base plugin class defining component plugin lifecycle."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict


class BasePlugin(ABC):
    """Abstract Base Class for AkumaOS configuration generator plugins."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the plugin component (e.g. 'hypr', 'waybar')."""
        pass

    @abstractmethod
    def load(self, project_root: Path, component: str, **kwargs: Any) -> Dict[str, Any]:
        """Load raw configuration data for the specified component.

        Args:
            project_root: Repository root path.
            component: Target component name.

        Returns:
            Dict[str, Any]: Raw loaded configuration dictionary.
        """
        pass

    @abstractmethod
    def validate(self, raw_data: Dict[str, Any], component: str, **kwargs: Any) -> Any:
        """Validate raw configuration data using Pydantic schemas.

        Args:
            raw_data: Raw configuration dictionary.
            component: Target component name.

        Returns:
            Any: Validated data model instance.
        """
        pass

    @abstractmethod
    def render(
        self, validated_data: Any, component: str, project_root: Path, **kwargs: Any
    ) -> str:
        """Render component template with validated context data.

        Args:
            validated_data: Validated data model instance.
            component: Target component name.
            project_root: Repository root path.

        Returns:
            str: Rendered configuration content string.
        """
        pass

    def write(self, content: str, output_path: Path) -> Path:
        """Write rendered content to the specified output file path.

        Args:
            content: Rendered string content.
            output_path: Destination file path.

        Returns:
            Path: Destination output file path.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path

    @abstractmethod
    def get_output_path(self, project_root: Path, component: str) -> Path:
        """Determine target output path for generated configuration.

        Args:
            project_root: Repository root path.
            component: Target component name.

        Returns:
            Path: Target destination file path.
        """
        pass

    def generate(self, project_root: Path, component: str, **kwargs: Any) -> Path:
        """Orchestrate the full plugin lifecycle: load -> validate -> render -> write.

        Args:
            project_root: Repository root path.
            component: Target component name to generate.

        Returns:
            Path: Path to the generated configuration file.
        """
        raw_data = self.load(project_root, component, **kwargs)
        validated_data = self.validate(raw_data, component, **kwargs)
        rendered_content = self.render(
            validated_data, component, project_root, **kwargs
        )
        output_path = self.get_output_path(project_root, component)
        return self.write(rendered_content, output_path)
