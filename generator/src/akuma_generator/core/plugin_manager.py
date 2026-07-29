"""Plugin registry and manager for AkumaOS Generator plugins."""

from typing import Dict, List, Type

from akuma_generator.core.base_plugin import BasePlugin


class PluginManager:
    """Registry manager for discovering, registering, and retrieving plugins."""

    _registry: Dict[str, BasePlugin] = {}

    @classmethod
    def register(cls, plugin: BasePlugin | Type[BasePlugin]) -> None:
        """Register a plugin instance or class in the registry.

        Args:
            plugin: BasePlugin instance or class.
        """
        instance = plugin() if isinstance(plugin, type) else plugin
        cls._registry[instance.name] = instance

    @classmethod
    def get(cls, name: str) -> BasePlugin:
        """Retrieve a registered plugin by name.

        Args:
            name: Plugin component name (e.g. 'hypr').

        Returns:
            BasePlugin: Registered plugin instance.

        Raises:
            KeyError: If no plugin is registered under the given name.
        """
        cls._ensure_default_plugins()
        if name not in cls._registry:
            avail = cls.list_plugins()
            raise KeyError(f"Plugin '{name}' is not registered. Available: {avail}")
        return cls._registry[name]

    @classmethod
    def list_plugins(cls) -> List[str]:
        """List all currently registered plugin names.

        Returns:
            List[str]: Sorted list of registered plugin names.
        """
        cls._ensure_default_plugins()
        return sorted(list(cls._registry.keys()))

    @classmethod
    def clear(cls) -> None:
        """Clear all registered plugins (used for testing)."""
        cls._registry.clear()

    @classmethod
    def _ensure_default_plugins(cls) -> None:
        """Lazily load default built-in plugins if registry is empty."""
        if "hypr" not in cls._registry:
            try:
                from akuma_generator.plugins.hypr import HyprPlugin

                cls.register(HyprPlugin)
            except ImportError:
                pass
