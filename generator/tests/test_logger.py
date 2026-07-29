"""Unit tests for structured logging module."""

import logging

from akuma_generator.core.logger import debug, error, info, setup_logger, warning


def test_setup_logger_default():
    """Test default logger setup."""
    logger = setup_logger(verbose=False)
    assert logger.level == logging.INFO


def test_setup_logger_verbose():
    """Test logger setup with verbose=True."""
    logger = setup_logger(verbose=True)
    assert logger.level == logging.DEBUG


def test_logging_functions(caplog):
    """Test logger level messages."""
    setup_logger(verbose=True)

    with caplog.at_level(logging.DEBUG):
        debug("Debug test")
        info("Info test")
        warning("Warning test")
        error("Error test")

    assert "Debug test" in caplog.text
    assert "Info test" in caplog.text
    assert "Warning test" in caplog.text
    assert "Error test" in caplog.text
