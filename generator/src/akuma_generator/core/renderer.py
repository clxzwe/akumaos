"""Template rendering engine module for AkumaOS Generator."""

from pathlib import Path
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader


def render_template(template_path: Path | str, context: Dict[str, Any]) -> str:
    """Render a Jinja2 template file with context variables.

    Args:
        template_path: Path to the Jinja2 template file.
        context: Dictionary of variables for template substitution.

    Returns:
        str: Rendered template text.
    """
    path = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(path.parent),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(path.name)
    return template.render(context)


def render_component(component_name: str, context: Dict[str, Any]) -> str:
    """Render target application component configuration.

    Raises:
        NotImplementedError: Component rendering logic not implemented yet.
    """
    raise NotImplementedError("Component rendering logic is not implemented yet.")
