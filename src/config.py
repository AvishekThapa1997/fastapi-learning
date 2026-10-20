from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    app_env: Literal["development", "staging", "production"] = Field(alias="TEST_ENV")
    app_name: str = Field(alias="TEST_NAME")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


app_config = AppConfig()
