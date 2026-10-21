from fastapi import APIRouter, FastAPI

from app.config.app_config import app_config
from app.routes.jobs.jobs_routers import job_router

app = FastAPI(
    title=app_config.app_name,
)

api_routes = APIRouter(
    prefix="/api",
)

api_routes.include_router(job_router)

app.include_router(api_routes)
