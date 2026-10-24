from fastapi import APIRouter, FastAPI

from app.core.config import Config
from app.jobs.router import router as job_router


def start_app():
    app_config = Config()
    app = FastAPI(
        title=app_config.app_name,
    )

    api_routes = APIRouter(
        prefix="/api",
    )

    api_routes.include_router(job_router)

    app.include_router(api_routes)
    return app
