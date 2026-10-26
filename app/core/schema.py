from typing import Annotated, TypedDict

from pydantic import BaseModel, Field


class APIError(TypedDict):
    code: Annotated[int, Field(gt=0)]
    message: str


class ValidationError(APIError):
    errors: dict[str, str | int]


class APIResponse[T](BaseModel):
    data: T | None = None
    success: bool = True
    error: APIError | ValidationError | None = None
