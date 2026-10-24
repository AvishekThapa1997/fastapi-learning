from typing import Annotated

from fastapi import Depends

from app.core.dependencies import AppConfig

from .constants import MAX_ATTEMPTS
from .service import JobService as JobServiceClass


def get_max_attempts(app_config: AppConfig):
    print("APP_CONFIG", app_config)
    if (max_attempts := app_config.max_attempts) is not None:
        return max_attempts
    return MAX_ATTEMPTS


JobService = Annotated[
    JobServiceClass,
    Depends(),
]
