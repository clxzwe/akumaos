"""CLI module for AkumaOS Generator."""

from pathlib import Path

import typer

from akuma_generator.core.logger import setup_logger
from akuma_generator.core.plugin_manager import PluginManager

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
        help="Component to generate (e.g. monitors, environment, all)",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Simulate generation without writing files to disk",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose debug logging",
    ),
) -> None:
    """Generate configuration files for AkumaOS components."""
    setup_logger(verbose=verbose)
    root = _find_project_root()

    if component == "all":
        components_to_generate = ["monitors", "environment"]
    elif component in ("monitors", "environment"):
        components_to_generate = [component]
    else:
        typer.echo(f"Unknown component: {component}")
        raise typer.Exit(code=1)

    plugin = PluginManager.get("hypr")

    if not dry_run:
        typer.echo("Generating Hyprland...")

    for comp in components_to_generate:
        plugin.generate(project_root=root, component=comp, dry_run=dry_run)
        if not dry_run:
            typer.echo(f"✓ {comp}")

    if not dry_run:
        typer.echo("Done.")


if __name__ == "__main__":
    app()
