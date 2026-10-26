import logging

from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from starlette.exceptions import HTTPException as StarletteException

from .schema import APIResponse

logger = logging.getLogger(__name__)


async def http_exception_handler(
    request: Request,
    exception: StarletteException,
) -> Response:
    logger.exception(exception)
    return JSONResponse(
        status_code=exception.status_code,
        headers=exception.headers,
        content=APIResponse.create_json_response(
            success=False,
            error={
                "code": exception.status_code,
                "message": exception.detail,
            },
        ),
    )


async def request_validation_exception_handler(
    request: Request, exception: RequestValidationError
) -> Response:
    logger.exception(exception)
    status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
    formatted_errors = [
        {".".join(map(str, err.get("loc"))): err.get("msg")} for err in exception.errors()
    ]
    return JSONResponse(
        status_code=status_code,
        content=APIResponse.create_json_response(
            success=False,
            error={
                "code": status_code,
                "message": "validation_failed",
                "errors": formatted_errors,
            },
        ),
    )


async def unexpected_exception_handler(request: Request, exception: Exception) -> Response:
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    logger.exception(exception)
    return JSONResponse(
        status_code=status_code,
        content=APIResponse.create_json_response(
            success=False,
            error={
                "code": status_code,
                "message": "Internal server error",
            },
        ),
    )
