"""Custom exception hierarchy for AkumaOS Generator."""


class AkumaError(Exception):
    """Base exception class for all AkumaOS Generator errors."""

    pass


class SchemaError(AkumaError):
    """Raised when configuration schema parsing or structure is invalid."""

    pass


class TemplateError(AkumaError):
    """Raised when Jinja2 template loading or rendering fails."""

    pass


class PluginError(AkumaError):
    """Raised when plugin registration, lookup, or execution fails."""

    pass


class ValidationError(AkumaError):
    """Raised when Pydantic schema validation fails."""

    pass


class FilesystemError(AkumaError):
    """Raised when file reading, writing, or directory creation fails."""

    pass
