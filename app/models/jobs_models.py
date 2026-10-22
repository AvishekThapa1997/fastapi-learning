from datetime import datetime
from enum import IntEnum, StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

JobId = Annotated[int, Field(gt=0, description="Unique identifier for the job")]


class JobType(StrEnum):
    SEND_EMAIL = "send_email"
    SEND_SMS = "send_sms"


class JobStatus(IntEnum):
    PENDING = 0
    PROCESSING = 1
    COMPLETED = 2
    FAILED = 3


class CreateJob(BaseModel):
    name: str
    type: JobType

    model_config = ConfigDict(
        use_enum_values=True,
    )


class Job(CreateJob):
    id: JobId
    created_at: datetime = Field(default_factory=datetime.now())
    status: JobStatus = JobStatus.PENDING


class UpdateJob(BaseModel):
    id: JobId
    name: str | None = None
    type: JobType | None = None
    status: JobStatus | None = None
