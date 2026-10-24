from typing import Annotated, TypedDict

from pydantic import BaseModel, Field


class APIError(TypedDict):
    code: Annotated[int, Field(gt=0)]
    message: str


class APIResponse[T](BaseModel):
    data: T | None = None
    success: bool = True
    error: APIError | None = None
