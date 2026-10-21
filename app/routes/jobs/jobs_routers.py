from typing import Annotated

from fastapi import APIRouter, Path

job_router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@job_router.get("/")
def get_user_jobs():
    return []


@job_router.get("/{job_id}")
def get_job_details(job_id: Annotated[int, Path(title="The ID of the job to get")]):
    return {
        "job": {"job_id": job_id},
    }
