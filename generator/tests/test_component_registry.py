"""Unit tests for Hyprland ComponentRegistry and component dispatch."""

from pathlib import Path
from typing import Any, Dict

import pytest

from akuma_generator.core.errors import PluginError
from akuma_generator.plugins.hypr.component_registry import ComponentRegistry
from akuma_generator.plugins.hypr.components.base import HyprComponent
from akuma_generator.plugins.hypr.plugin import HyprPlugin


class MockComponent(HyprComponent):
    """Mock component for registry testing."""

    @property
    def name(self) -> str:
        return "mock_comp"

    def load(self, project_root: Path) -> Dict[str, Any]:
        return {"key": "val"}

    def validate(self, raw_data: Dict[str, Any]) -> Any:
        return raw_data

    def render(self, validated_data: Any, project_root: Path) -> str:
        return f"mock_rendered_{validated_data['key']}"

    def get_output_path(self, project_root: Path) -> Path:
        return project_root / "mock.conf"


def test_component_registration():
    """Test registering and retrieving a sub-component."""
    ComponentRegistry.register(MockComponent)
    comp = ComponentRegistry.get("mock_comp")
    assert comp.name == "mock_comp"
    assert "mock_comp" in ComponentRegistry.list_components()


def test_component_not_found():
    """Test retrieving non-existent component raises PluginError."""
    with pytest.raises(PluginError):
        ComponentRegistry.get("invalid_component")


def test_hypr_plugin_dispatch(tmp_path, monkeypatch):
    """Test HyprPlugin dispatching to registered components."""
    plugin = HyprPlugin()
    assert "monitors" in ComponentRegistry.list_components()
    assert "environment" in ComponentRegistry.list_components()

    repo_root = Path(__file__).resolve().parent.parent.parent
    monkeypatch.chdir(repo_root)

    out_monitors = plugin.generate(repo_root, component="monitors")
    assert out_monitors.name == "monitors.conf"

    out_env = plugin.generate(repo_root, component="environment")
    assert out_env.name == "env.conf"
