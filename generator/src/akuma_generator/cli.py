"""CLI module for AkumaOS Generator."""

from pathlib import Path

import typer

from akuma_generator.plugins.hypr import HyprPlugin

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
        output_file = HyprPlugin.generate_monitors(root)
        typer.echo(f"Generated: {output_file.relative_to(root)}")
    else:
        typer.echo(f"Unknown component: {component}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
