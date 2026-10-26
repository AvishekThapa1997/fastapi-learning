from typing import Annotated, TypedDict

from pydantic import BaseModel, Field


class APIError(TypedDict):
    code: Annotated[int, Field(gt=0)]
    message: str


class ValidationError(APIError):
    errors: list[dict[str, str]]


class APIResponse[T](BaseModel):
    data: T | None = None
    success: bool = True
    error: APIError | ValidationError | None = None

    @classmethod
    def create_json_reponse(cls: type["APIResponse[T]"], *args, **kwargs) -> dict:
        return cls(*args, **kwargs).model_dump(mode="json")
