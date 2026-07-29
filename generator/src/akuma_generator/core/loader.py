"""Configuration and theme loader module for AkumaOS Generator."""

from pathlib import Path
from typing import Any, Dict

import yaml


def load_yaml(file_path: Path | str) -> Dict[str, Any]:
    """Load and parse a YAML configuration file.

    Args:
        file_path: Path to the YAML file.

    Returns:
        Dict[str, Any]: Parsed YAML content.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
        return content if isinstance(content, dict) else {}


def load_theme(theme_name: str = "default") -> Any:
    """Load theme tokens and configuration definitions.

    Raises:
        NotImplementedError: Loader logic not implemented yet.
    """
    raise NotImplementedError("Theme loading logic is not implemented yet.")


def load_schema(schema_name: str) -> Any:
    """Load YAML schema specification file.

    Raises:
        NotImplementedError: Loader logic not implemented yet.
    """
    raise NotImplementedError("Schema loading logic is not implemented yet.")
