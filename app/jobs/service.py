from fastapi import HTTPException, status

from .schema import CreateJobWithMaxAttempts, Job, JobId


class JobService:
    __jobs: list[Job] = []

    def create_job(
        self,
        create_job: CreateJobWithMaxAttempts,
    ):
        new_job = Job(
            id=len(self.__jobs) + 1,
            **create_job.model_dump(),
        )
        self.__jobs.append(new_job)
        return new_job

    def get_jobs(self) -> list[Job]:
        return self.__jobs

    def get_job_details_by_id(self, job_id: JobId) -> Job:
        job = next((job for job in self.__jobs if job.id == job_id), None)
        if job is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Job is not available with id {job_id}",
            )
        return job
