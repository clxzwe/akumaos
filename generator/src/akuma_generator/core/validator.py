import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional, Union

from pydantic import ValidationError as PydanticValidationError

from akuma_generator.core.errors import ValidationError
from akuma_generator.core.logger import debug
from akuma_generator.models import DesktopModel


def validate_desktop_config(data: Dict[str, Any]) -> DesktopModel:
    """Validate raw desktop configuration dictionary against DesktopModel schema.

    Args:
        data: Dictionary of desktop configuration parameters.

    Returns:
        DesktopModel: Validated DesktopModel instance.

    Raises:
        ValidationError: If schema validation fails.
    """
    debug("Validating desktop configuration against DesktopModel schema")
    try:
        return DesktopModel.model_validate(data)
    except PydanticValidationError as e:
        raise ValidationError(f"Desktop configuration validation failed: {e}") from e


def validate_theme(theme_data: Any) -> bool:
    """Validate loaded theme data against theme schema.

    Raises:
        NotImplementedError: Validation logic not implemented yet.
    """
    raise NotImplementedError("Theme validation logic is not implemented yet.")


def validate_schema(schema_data: Any) -> bool:
    """Validate configuration schema data structure.

    Raises:
        NotImplementedError: Validation logic not implemented yet.
    """
    raise NotImplementedError("Schema validation logic is not implemented yet.")


def validate_hypr_syntax(
    content_or_path: Union[str, Path], file_path: Optional[Path] = None
) -> None:
    """Validate Hyprland configuration syntax and directives compatibility for 0.56.x.

    Args:
        content_or_path: String content or Path to config file.
        file_path: Optional destination Path.

    Raises:
        ValidationError: If invalid directives or dispatchers are detected.
    """
    if isinstance(content_or_path, Path):
        path = content_or_path
        if not path.exists():
            return
        content = path.read_text(encoding="utf-8")
    else:
        content = str(content_or_path)
        path = file_path

    # 1. Static directive auditing against Hyprland 0.56.x specs
    if re.search(r"^\s*pseudotile\s*=", content, re.MULTILINE):
        raise ValidationError(
            "Invalid configuration directive: <dwindle:pseudotile> "
            "does not exist in Hyprland 0.56.x."
        )

    if re.search(
        r"^\s*bind[a-z]*\s*=\s*[^,\n]*,\s*[^,\n]*,\s*togglesplit\s*(?:,|$)",
        content,
        re.MULTILINE,
    ):
        raise ValidationError(
            "Invalid keybind dispatcher: 'togglesplit' does not exist in "
            "Hyprland 0.56.x. Use 'layoutmsg, togglesplit'."
        )

    # 2. Hyprland --verify-config syntax validation
    hypr_bin = shutil.which("Hyprland") or shutil.which("hyprland")
    if hypr_bin:
        temp_file = None
        verify_content = content
        if (
            path
            and (path.parent / "config").exists()
            and "~/.config/hypr/config/" in content
        ):
            config_dir = (path.parent / "config").resolve()
            verify_content = content.replace("~/.config/hypr/config/", f"{config_dir}/")

        if path and path.exists() and verify_content == content:
            target_file = path
        else:
            temp_file = tempfile.NamedTemporaryFile(
                mode="w", suffix=".conf", delete=False, encoding="utf-8"
            )
            temp_file.write(verify_content)
            temp_file.flush()
            temp_file.close()
            target_file = Path(temp_file.name)

        try:
            res = subprocess.run(
                [hypr_bin, "--verify-config", "-c", str(target_file)],
                capture_output=True,
                text=True,
                timeout=5,
            )
            combined_output = f"{res.stdout}\n{res.stderr}"
            if (
                res.returncode != 0
                or "Config error" in combined_output
                or "Invalid dispatcher" in combined_output
            ):
                error_lines = [
                    line
                    for line in combined_output.splitlines()
                    if (
                        "Config error" in line
                        or "Invalid dispatcher" in line
                        or "ERR" in line
                    )
                    and "source= globbing error" not in line
                ]
                if error_lines:
                    err_msg = "\n".join(error_lines)
                    raise ValidationError(
                        f"Hyprland 0.56.x syntax validation failed:\n{err_msg}"
                    )
        finally:
            if temp_file and Path(temp_file.name).exists():
                try:
                    Path(temp_file.name).unlink()
                except OSError:
                    pass


def check_hyprctl_configerrors() -> None:
    """Run `hyprctl configerrors` and raise ValidationError if errors are reported."""
    hyprctl_bin = shutil.which("hyprctl")
    if hyprctl_bin:
        try:
            res = subprocess.run(
                [hyprctl_bin, "configerrors"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if res.returncode == 0:
                output = res.stdout.strip()
                if (
                    output
                    and output != "ok"
                    and ("Config error" in output or "Invalid dispatcher" in output)
                ):
                    raise ValidationError(
                        f"Hyprland configerrors check failed:\n{output}"
                    )
        except (subprocess.SubprocessError, OSError):
            pass
