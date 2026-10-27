from typing import Annotated

from fastapi import APIRouter, Depends, Path, status

from app.core.schema import APIResponse

from .dependencies import JobService, get_max_attempts
from .schema import CreateJob, CreateJobWithMaxAttempts, Job, JobId

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
def get_user_jobs(job_service: JobService) -> APIResponse[list[Job]]:
    jobs = job_service.get_jobs()
    return APIResponse(data=jobs)


@router.get("/{job_id}", status_code=status.HTTP_200_OK)
def get_job_details(
    job_id: Annotated[JobId, Path(title="The ID of the job to get")],
    job_service: JobService,
) -> APIResponse[Job]:
    job = job_service.get_job_details_by_id(job_id=job_id)
    return APIResponse(
        data=job,
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_job(
    create_job: CreateJob,
    max_attempts: Annotated[int, Depends(get_max_attempts)],
    job_service: JobService,
) -> APIResponse[Job]:

    job = job_service.create_job(
        create_job=CreateJobWithMaxAttempts(
            **create_job.model_dump(),
            max_attempts=max_attempts,
        )
    )
    return APIResponse(
        data=job,
    )
