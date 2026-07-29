"""Unit tests for BasePlugin lifecycle."""

from pathlib import Path
from typing import Any, Dict

from akuma_generator.core.base_plugin import BasePlugin
from akuma_generator.plugins.hypr import HyprPlugin


class DummyPlugin(BasePlugin):
    """Dummy plugin implementation for testing lifecycle."""

    @property
    def name(self) -> str:
        return "dummy"

    def load(self, project_root: Path, component: str, **kwargs: Any) -> Dict[str, Any]:
        return {"value": "hello"}

    def validate(self, raw_data: Dict[str, Any], component: str, **kwargs: Any) -> Any:
        return raw_data

    def render(
        self, validated_data: Any, component: str, project_root: Path, **kwargs: Any
    ) -> str:
        return f"content: {validated_data['value']}"

    def get_output_path(self, project_root: Path, component: str) -> Path:
        return project_root / "out.txt"


def test_base_plugin_lifecycle(tmp_path):
    """Test full BasePlugin generate lifecycle."""
    plugin = DummyPlugin()
    out_file = plugin.generate(tmp_path, component="dummy")
    assert out_file == tmp_path / "out.txt"
    assert out_file.exists()
    assert out_file.read_text(encoding="utf-8") == "content: hello"


def test_hypr_plugin_inherits_base_plugin():
    """Test that HyprPlugin is an instance of BasePlugin."""
    plugin = HyprPlugin()
    assert isinstance(plugin, BasePlugin)
    assert plugin.name == "hypr"
