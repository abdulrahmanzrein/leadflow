import logging
import sys

import structlog

from app.config import settings


def configure_logging() -> None:
    """Call once at app startup in main.py."""

    log_level = logging.DEBUG if settings.debug else logging.INFO

    # stdlib logging config — structlog sits on top of this
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=log_level,
    )

    # in dev: pretty colored output
    # in prod: machine-readable JSON lines
    renderer = (
        structlog.dev.ConsoleRenderer()
        if settings.app_env == "development"
        else structlog.processors.JSONRenderer()
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,   # adds request-scoped context
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.ExceptionRenderer(),
            renderer,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
    )


# usage anywhere in the app:
#   from app.core.logging import get_logger
#   logger = get_logger(__name__)
#   logger.info("signal_detected", company="Acme", severity="high")
def get_logger(name: str) -> structlog.BoundLogger:
    return structlog.get_logger(name)
