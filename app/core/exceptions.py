from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


# ── Base ───────────────────────────────────────────────────────────────────────

class AppException(Exception):
    """Base class — all custom exceptions inherit from this."""
    status_code: int = 500
    detail: str = "Internal server error"

    def __init__(self, detail: str | None = None):
        self.detail = detail or self.__class__.detail


# ── Resource errors ────────────────────────────────────────────────────────────

class NotFoundError(AppException):
    status_code = 404
    detail = "Resource not found"

class AlreadyExistsError(AppException):
    status_code = 409
    detail = "Resource already exists"

class ValidationError(AppException):
    status_code = 422
    detail = "Validation failed"


# ── Auth errors ────────────────────────────────────────────────────────────────

class UnauthorizedError(AppException):
    status_code = 401
    detail = "Not authorized"

class ForbiddenError(AppException):
    status_code = 403
    detail = "Access forbidden"


# ── Pipeline errors ────────────────────────────────────────────────────────────

class PipelineAlreadyRunningError(AppException):
    status_code = 409
    detail = "A pipeline run is already in progress"

class PipelineStageError(AppException):
    status_code = 500
    detail = "Pipeline stage failed"


# ── External API errors ────────────────────────────────────────────────────────

class ExternalAPIError(AppException):
    status_code = 502
    detail = "External API request failed"

class RateLimitError(AppException):
    status_code = 429
    detail = "Rate limit hit on external API"


# ── Register handlers on the FastAPI app ──────────────────────────────────────

def register_exception_handlers(app: FastAPI) -> None:
    """Call this in main.py so all AppExceptions return clean JSON responses."""

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
