"""Pydantic data models for AkumaOS configuration schema."""

from typing import Any, List, Union

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


class DesktopModel(BaseModel):
    """Pydantic model representing desktop environment settings."""

    monitors: List[MonitorModel] = Field(default_factory=list)


class ThemeModel(BaseModel):
    """Placeholder model for visual theme definitions."""

    pass


class ModuleModel(BaseModel):
    """Placeholder model for desktop component module settings."""

    pass


class KeybindModel(BaseModel):
    """Placeholder model for declarative keybinding definitions."""

    pass
