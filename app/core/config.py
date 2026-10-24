from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    app_env: Literal["development", "staging", "production"] = Field(
        ...,
    )
    app_name: str = Field(
        ...,
    )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


app_config = Config()
