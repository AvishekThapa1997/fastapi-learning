from typing import cast

from fastapi import APIRouter, FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.types import ExceptionHandler

from app.core.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
    unexpected_exception_handler,
)
from app.jobs.router import router as job_router

app = FastAPI()

api_routes = APIRouter(
    prefix="/api",
)

app.add_exception_handler(
    StarletteHTTPException,
    cast(
        ExceptionHandler,
        http_exception_handler,
    ),
)
app.add_exception_handler(
    RequestValidationError,
    cast(
        ExceptionHandler,
        request_validation_exception_handler,
    ),
)
app.add_exception_handler(Exception, unexpected_exception_handler)
api_routes.include_router(job_router)

app.include_router(api_routes)
