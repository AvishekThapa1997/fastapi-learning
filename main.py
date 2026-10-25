from fastapi import APIRouter, FastAPI

from app.jobs.router import router as job_router

app = FastAPI()

api_routes = APIRouter(
    prefix="/api",
)

api_routes.include_router(job_router)

app.include_router(api_routes)
