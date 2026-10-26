from typing import Annotated

from fastapi import Depends

from app.core.dependencies import AppConfig

from .constants import MAX_ATTEMPTS
from .service import JobService as JobServiceClass

count = 0


def get_max_attempts(app_config: AppConfig):
    return app_config.max_attempts or MAX_ATTEMPTS


JobService = Annotated[
    JobServiceClass,
    Depends(),
]
