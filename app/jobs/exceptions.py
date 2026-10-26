from fastapi import HTTPException, status

from .schema import JobId


class JobNotFoundError(HTTPException):
    job_id: JobId

    def __init__(self, job_id: JobId):
        self.job_id = job_id
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job not found with id {self.job_id}",
        )
