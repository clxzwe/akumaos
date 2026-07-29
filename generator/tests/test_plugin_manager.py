"""Unit tests for PluginManager registry."""

from pathlib import Path
from typing import Any, Dict

import pytest

from akuma_generator.core.base_plugin import BasePlugin
from akuma_generator.core.errors import PluginError
from akuma_generator.core.plugin_manager import PluginManager


class MockPlugin(BasePlugin):
    """Mock plugin for registry testing."""

    @property
    def name(self) -> str:
        return "mock"

    def load(self, project_root: Path, component: str, **kwargs: Any) -> Dict[str, Any]:
        return {"test": "data"}

    def validate(self, raw_data: Dict[str, Any], component: str, **kwargs: Any) -> Any:
        return raw_data

    def render(
        self,
        validated_data: Any,
        component: str,
        project_root: Path,
        **kwargs: Any,
    ) -> str:
        return "rendered_mock_content"

    def get_output_path(self, project_root: Path, component: str) -> Path:
        return project_root / "mock_output.conf"


def test_plugin_registration():
    """Test registering and retrieving a plugin."""
    PluginManager.register(MockPlugin)
    plugin = PluginManager.get("mock")
    assert plugin.name == "mock"
    assert "mock" in PluginManager.list_plugins()


def test_plugin_not_found():
    """Test retrieving a non-existent plugin raises PluginError."""
    with pytest.raises(PluginError):
        PluginManager.get("non_existent_plugin")


def test_hypr_plugin_auto_registration():
    """Test that built-in hypr plugin is retrieved automatically."""
    hypr_plugin = PluginManager.get("hypr")
    assert hypr_plugin.name == "hypr"
