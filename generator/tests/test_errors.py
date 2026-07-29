"""Unit tests for custom exception hierarchy."""

import pytest

from akuma_generator.core.errors import (
    AkumaError,
    FilesystemError,
    PluginError,
    SchemaError,
    TemplateError,
    ValidationError,
)


def test_exception_inheritance():
    """Test custom exceptions inherit from AkumaError."""
    assert issubclass(SchemaError, AkumaError)
    assert issubclass(TemplateError, AkumaError)
    assert issubclass(PluginError, AkumaError)
    assert issubclass(ValidationError, AkumaError)
    assert issubclass(FilesystemError, AkumaError)


def test_raising_custom_errors():
    """Test raising and catching custom errors."""
    with pytest.raises(AkumaError):
        raise SchemaError("Invalid schema")

    with pytest.raises(FilesystemError):
        raise FilesystemError("File not found")
