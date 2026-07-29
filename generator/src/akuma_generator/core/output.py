"""Output management and file writing abstraction module."""

from pathlib import Path

from akuma_generator.core.errors import FilesystemError
from akuma_generator.core.logger import debug, info


class OutputManager:
    """Abstraction manager for handling output file writing, dry-runs, and backups."""

    @staticmethod
    def write(
        content: str,
        output_path: Path,
        dry_run: bool = False,
        backup: bool = False,
        overwrite: bool = True,
    ) -> Path:
        """Write content to output path with dry-run, backup, and overwrite support.

        Args:
            content: Rendered configuration string content.
            output_path: Destination file path.
            dry_run: If True, print content to stdout without writing file.
            backup: If True and target exists, create a .bak backup file.
            overwrite: If False and target exists, raise FilesystemError.

        Returns:
            Path: Destination output file path.

        Raises:
            FilesystemError: If writing or backup fails.
        """
        if dry_run:
            info(f"[DRY-RUN] Target output: {output_path}")
            print(f"--- BEGIN {output_path.name} (DRY-RUN) ---")
            print(content.strip())
            print(f"--- END {output_path.name} ---")
            return output_path

        try:
            if output_path.exists():
                if not overwrite:
                    raise FilesystemError(
                        f"File exists and overwrite is disabled: {output_path}"
                    )
                if backup:
                    backup_path = output_path.with_suffix(output_path.suffix + ".bak")
                    debug(f"Creating backup: {backup_path}")
                    backup_path.write_bytes(output_path.read_bytes())

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            debug(f"Successfully wrote output to {output_path}")
            return output_path
        except OSError as e:
            raise FilesystemError(
                f"Failed to write output to {output_path}: {e}"
            ) from e
