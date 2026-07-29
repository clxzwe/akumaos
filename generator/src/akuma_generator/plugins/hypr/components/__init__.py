"""Hyprland components package."""

from akuma_generator.plugins.hypr.components.animations import AnimationsComponent
from akuma_generator.plugins.hypr.components.autostart import AutostartComponent
from akuma_generator.plugins.hypr.components.base import HyprComponent
from akuma_generator.plugins.hypr.components.binds import BindsComponent
from akuma_generator.plugins.hypr.components.decoration import DecorationComponent
from akuma_generator.plugins.hypr.components.environment import EnvironmentComponent
from akuma_generator.plugins.hypr.components.general import GeneralComponent
from akuma_generator.plugins.hypr.components.input import InputComponent
from akuma_generator.plugins.hypr.components.master import HyprlandConfigComponent
from akuma_generator.plugins.hypr.components.monitors import MonitorsComponent

__all__ = [
    "AnimationsComponent",
    "AutostartComponent",
    "BindsComponent",
    "DecorationComponent",
    "EnvironmentComponent",
    "GeneralComponent",
    "HyprComponent",
    "HyprlandConfigComponent",
    "InputComponent",
    "MonitorsComponent",
]
