"""Tests for the template renderer module."""

from akuma_generator.renderer import render_template


def test_render_template(tmp_path):
    """Test rendering Jinja2 template with context."""
    template_file = tmp_path / "test.j2"
    template_file.write_text(
        "{% for m in monitors %}monitor={{ m.name }},{{ m.resolution }}{% endfor %}\n",
        encoding="utf-8",
    )

    context = {"monitors": [{"name": "DP-1", "resolution": "2560x1440"}]}
    result = render_template(template_file, context)
    assert "monitor=DP-1,2560x1440" in result
