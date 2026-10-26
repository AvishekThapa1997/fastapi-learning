from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response

from .schema import APIResponse


async def http_exception_handler(request: Request, exception: HTTPException) -> Response:

    return JSONResponse(
        status_code=exception.status_code,
        headers=exception.headers,
        content=APIResponse(
            success=False,
            error={
                "code": exception.status_code,
                "message": exception.detail,
            },
        ).model_dump(mode="json"),
    )


async def request_validation_exception_handler(
    request: Request, exception: RequestValidationError
) -> Response:

    formatted_errors = [{".".join(err.get("loc")): err.get("msg")} for err in exception.errors()]
    return JSONResponse(
        status_code=422,
        content=APIResponse(
            success=False,
            error={
                "code": 422,
                "message": "validation_failed",
                "errors": formatted_errors,
            },
        ).model_dump(mode="json"),
    )
