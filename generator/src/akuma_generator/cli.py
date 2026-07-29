"""CLI module for AkumaOS Generator."""

from pathlib import Path

import typer

from akuma_generator.loader import load_yaml
from akuma_generator.renderer import render_template
from akuma_generator.validator import validate_desktop_config

app = typer.Typer(
    name="akuma",
    help="AkumaOS Configuration Generator CLI",
)


def _find_project_root() -> Path:
    """Locate the root directory of the AkumaOS repository."""
    current = Path.cwd()
    while current != current.parent:
        if (current / "examples" / "desktop.yaml").exists():
            return current
        current = current.parent
    return Path.cwd()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """AkumaOS Generator main CLI entry point."""
    if ctx.invoked_subcommand is None:
        pass


@app.command("generate")
def generate(
    component: str = typer.Option(
        "monitors",
        "--component",
        "-c",
        help="Component to generate (e.g. monitors)",
    ),
) -> None:
    """Generate configuration files for AkumaOS components."""
    if component == "monitors":
        root = _find_project_root()
        config_path = root / "examples" / "desktop.yaml"
        template_path = root / "generator" / "templates" / "monitors.conf.j2"
        output_dir = root / "config" / "hypr" / "generated"
        output_file = output_dir / "monitors.conf"

        raw_data = load_yaml(config_path)
        validated_desktop = validate_desktop_config(raw_data)

        context = {"monitors": [m.model_dump() for m in validated_desktop.monitors]}
        rendered_content = render_template(template_path, context)

        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(rendered_content)

        typer.echo(f"Generated: {output_file.relative_to(root)}")
    else:
        typer.echo(f"Unknown component: {component}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
