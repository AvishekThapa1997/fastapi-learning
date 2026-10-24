from typing import Annotated

from fastapi import Depends

from app.core.config import Config


def generate_app_config():
    return Config()


AppConfig = Annotated[Config, Depends(generate_app_config)]
