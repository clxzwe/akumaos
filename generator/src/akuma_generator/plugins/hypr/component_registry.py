"""Component registry for Hyprland plugin sub-components."""

from typing import Dict, List, Type

from akuma_generator.core.errors import PluginError
from akuma_generator.plugins.hypr.components.base import HyprComponent


class ComponentRegistry:
    """Registry manager for storing and retrieving Hyprland sub-components."""

    _registry: Dict[str, HyprComponent] = {}

    @classmethod
    def register(cls, component: HyprComponent | Type[HyprComponent]) -> None:
        """Register a component instance or class in the registry.

        Args:
            component: HyprComponent instance or class.
        """
        instance = component() if isinstance(component, type) else component
        cls._registry[instance.name] = instance

    @classmethod
    def get(cls, name: str) -> HyprComponent:
        """Retrieve a registered component by name.

        Args:
            name: Component name (e.g. 'monitors', 'environment').

        Returns:
            HyprComponent: Registered component instance.

        Raises:
            PluginError: If component is not registered.
        """
        cls._ensure_default_components()
        if name not in cls._registry:
            avail = cls.list_components()
            raise PluginError(
                f"Hyprland component '{name}' is not registered. " f"Available: {avail}"
            )
        return cls._registry[name]

    @classmethod
    def list_components(cls) -> List[str]:
        """List all registered component names.

        Returns:
            List[str]: Sorted list of component names.
        """
        cls._ensure_default_components()
        return sorted(list(cls._registry.keys()))

    @classmethod
    def clear(cls) -> None:
        """Clear registered components (used for testing)."""
        cls._registry.clear()

    @classmethod
    def _ensure_default_components(cls) -> None:
        """Lazily register default built-in Hyprland components."""
        if "monitors" not in cls._registry:
            from akuma_generator.plugins.hypr.components.monitors import (
                MonitorsComponent,
            )

            cls.register(MonitorsComponent)

        if "environment" not in cls._registry:
            from akuma_generator.plugins.hypr.components.environment import (
                EnvironmentComponent,
            )

            cls.register(EnvironmentComponent)
