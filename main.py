from fastapi import APIRouter, FastAPI

from app.core.config import app_config
from app.jobs.router import router as job_router

app = FastAPI(
    title=app_config.app_name,
)

api_routes = APIRouter(
    prefix="/api",
)

api_routes.include_router(job_router)

app.include_router(api_routes)
