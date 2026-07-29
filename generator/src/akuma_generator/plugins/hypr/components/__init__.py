"""Hyprland components package."""

from akuma_generator.plugins.hypr.components.base import HyprComponent
from akuma_generator.plugins.hypr.components.environment import EnvironmentComponent
from akuma_generator.plugins.hypr.components.monitors import MonitorsComponent

__all__ = ["EnvironmentComponent", "HyprComponent", "MonitorsComponent"]
