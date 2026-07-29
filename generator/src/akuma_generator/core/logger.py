"""Structured logging module for AkumaOS Generator."""

import logging
import sys

_logger = logging.getLogger("akuma")


def setup_logger(verbose: bool = False) -> logging.Logger:
    """Configure structured logger stream handler and log level.

    Args:
        verbose: If True, set log level to DEBUG; otherwise INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    level = logging.DEBUG if verbose else logging.INFO
    _logger.setLevel(level)

    if not _logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s - %(name)s: %(message)s",
            datefmt="%H:%M:%S",
        )
        handler.setFormatter(formatter)
        _logger.addHandler(handler)
    else:
        _logger.handlers[0].setLevel(level)

    return _logger


def debug(msg: str, *args: object) -> None:
    """Log a debug message."""
    _logger.debug(msg, *args)


def info(msg: str, *args: object) -> None:
    """Log an info message."""
    _logger.info(msg, *args)


def warning(msg: str, *args: object) -> None:
    """Log a warning message."""
    _logger.warning(msg, *args)


def error(msg: str, *args: object) -> None:
    """Log an error message."""
    _logger.error(msg, *args)
