from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

from app.models.common_models import APIResponse
from app.models.jobs_models import CreateJob, Job

job_router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)

jobs: list[Job] = []


@job_router.get("/")
def get_user_jobs() -> APIResponse[list[Job]]:
    return APIResponse(
        data=jobs,
    )


@job_router.get("/{job_id}")
def get_job_details(
    job_id: Annotated[int, Path(title="The ID of the job to get")],
) -> APIResponse[Job]:
    job_data = next((job for job in jobs if job.id == job_id), None)
    if job_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {job_id} not available",
        )
    return APIResponse(
        success=True,
        data=job_data,
    )


@job_router.post("/", status_code=status.HTTP_201_CREATED)
def create_job(create_job: CreateJob) -> APIResponse[Job]:
    job = Job(
        id=len(jobs) + 1,
        **create_job.model_dump(),
    )
    jobs.append(job)
    return APIResponse(
        data=job,
    )
