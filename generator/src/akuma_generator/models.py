"""Pydantic data models for AkumaOS configuration schema."""

from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field, field_validator


class MonitorModel(BaseModel):
    """Pydantic model representing a display monitor configuration."""

    name: str
    resolution: str
    refresh: Union[int, float]
    position: Union[str, int]
    scale: Union[int, float] = 1

    @field_validator("position", mode="before")
    @classmethod
    def format_position(cls, v: Any) -> str:
        """Format position value to string (handling YAML 0x0 hex parsing)."""
        if isinstance(v, int):
            return f"{v}x0"
        return str(v)


class GeneralModel(BaseModel):
    """Pydantic model representing general compositor settings."""

    gaps_in: int = 5
    gaps_out: int = 10
    border_size: int = 2
    active_border_color: str = "rgba(33ccffee) rgba(00ff99ee) 45deg"
    inactive_border_color: str = "rgba(595959aa)"
    layout: str = "dwindle"
    resize_on_border: bool = True


class BlurModel(BaseModel):
    """Pydantic model representing blur settings."""

    enabled: bool = True
    size: int = 8
    passes: int = 3
    new_optimizations: bool = True
    vibrancy: float = 0.1696


class ShadowModel(BaseModel):
    """Pydantic model representing drop shadow settings."""

    enabled: bool = True
    range: int = 15
    render_power: int = 3
    color: str = "rgba(1a1a1aee)"


class DecorationModel(BaseModel):
    """Pydantic model representing window decoration settings."""

    rounding: int = 12
    active_opacity: float = 0.95
    inactive_opacity: float = 0.85
    blur: BlurModel = Field(default_factory=BlurModel)
    shadow: ShadowModel = Field(default_factory=ShadowModel)


class TouchpadModel(BaseModel):
    """Pydantic model representing touchpad input settings."""

    natural_scroll: bool = True
    tap_to_click: bool = True


class InputModel(BaseModel):
    """Pydantic model representing input device settings."""

    kb_layout: str = "us"
    sensitivity: Union[int, float] = 0
    touchpad: TouchpadModel = Field(default_factory=TouchpadModel)


class AutostartModel(BaseModel):
    """Pydantic model representing autostart services and wallpaper loading."""

    services: List[str] = Field(
        default_factory=lambda: [
            "waybar",
            "mako",
            "swww-daemon",
            "swayosd-server",
        ]
    )
    wallpaper_path: str = "~/Pictures/Wallpapers/default.jpg"


class EnvironmentModel(BaseModel):
    """Pydantic model representing environment variables."""

    vars: Dict[str, Union[str, int, float]] = Field(default_factory=dict)


class DesktopModel(BaseModel):
    """Pydantic model representing desktop environment settings."""

    monitors: List[MonitorModel] = Field(default_factory=list)
    environment: Dict[str, Union[str, int, float]] = Field(default_factory=dict)
    general: GeneralModel = Field(default_factory=GeneralModel)
    decoration: DecorationModel = Field(default_factory=DecorationModel)
    input: InputModel = Field(default_factory=InputModel)
    autostart: AutostartModel = Field(default_factory=AutostartModel)


class ThemeModel(BaseModel):
    """Placeholder model for visual theme definitions."""

    pass


class ModuleModel(BaseModel):
    """Placeholder model for desktop component module settings."""

    pass


class KeybindModel(BaseModel):
    """Placeholder model for declarative keybinding definitions."""

    pass
