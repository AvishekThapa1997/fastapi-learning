from .exceptions import JobNotFoundError
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
            raise JobNotFoundError(job_id=job_id)
        return job
