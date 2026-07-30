"""Base interface for Hyprland components."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional

from akuma_generator.core.output import OutputManager
from akuma_generator.core.validator import validate_hypr_syntax


class HyprComponent(ABC):
    """Abstract base class for Hyprland sub-components."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Component name (e.g. 'monitors', 'environment')."""
        pass

    @abstractmethod
    def load(self, project_root: Path) -> Dict[str, Any]:
        """Load raw configuration for this component."""
        pass

    @abstractmethod
    def validate(self, raw_data: Dict[str, Any]) -> Any:
        """Validate raw data against Pydantic schema."""
        pass

    @abstractmethod
    def render(self, validated_data: Any, project_root: Path) -> str:
        """Render component template into text content."""
        pass

    @abstractmethod
    def get_output_path(
        self, project_root: Path, output_dir: Optional[Path] = None
    ) -> Path:
        """Get output destination path for this component."""
        pass

    def generate(
        self,
        project_root: Path,
        dry_run: bool = False,
        backup: bool = False,
        overwrite: bool = True,
        output_dir: Optional[Path] = None,
    ) -> Path:
        """Execute full component generation lifecycle."""
        raw_data = self.load(project_root)
        validated_data = self.validate(raw_data)
        rendered_content = self.render(validated_data, project_root)
        output_path = self.get_output_path(project_root, output_dir=output_dir)

        validate_hypr_syntax(
            rendered_content, file_path=output_path if not dry_run else None
        )

        return OutputManager.write(
            rendered_content,
            output_path,
            dry_run=dry_run,
            backup=backup,
            overwrite=overwrite,
        )
