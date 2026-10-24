import re
from datetime import datetime
from enum import IntEnum, StrEnum
from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_serializer,
    field_validator,
    model_validator,
)

JobId = Annotated[int, Field(gt=0, description="Unique identifier for the job")]


class JobType(StrEnum):
    SEND_EMAIL = "send_email"
    SEND_SMS = "send_sms"


class JobStatus(IntEnum):
    PENDING = 0
    PROCESSING = 1
    COMPLETED = 2
    FAILED = 3


class EmailPayload(BaseModel):
    to: str = Field(
        ...,
        description="Receiver Email",
    )
    subject: str = Field(
        ...,
        description="Email's subject",
    )

    @field_validator("to")
    @classmethod
    def validate_email(cls, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Email is invalid")
        return email


class SMSPayload(BaseModel):
    to: str = Field(
        min_length=10,
        max_length=10,
        description="Recipient's phone number",
    )
    message: str = Field(min_length=1)


JobPayload = Annotated[EmailPayload | SMSPayload, "Payload to process job"]


class BaseJob(BaseModel):
    name: str
    type: JobType


class CreateJob(BaseJob):
    max_attempts: int = Field(default=3, gt=1)
    payload: JobPayload = Field(...)

    model_config = ConfigDict(
        use_enum_values=True,
    )

    @model_validator(mode="before")
    @classmethod
    def validate_job_payload(cls, data):
        if not isinstance(data, dict):
            return data
        job_type = data.get("type")
        job_payload = data.get("payload")
        if job_type is None:
            raise ValueError("Please add a valid job type")
        data = {**data}
        if job_type == JobType.SEND_EMAIL:
            data["payload"] = EmailPayload.model_validate(job_payload)
        elif job_type == JobType.SEND_SMS:
            data["payload"] = SMSPayload.model_validate(job_payload)
        else:
            raise ValueError("Unsupported job type")
        return data


class Job(BaseJob):
    id: JobId
    created_at: datetime = Field(default_factory=datetime.now)
    status: JobStatus = JobStatus.PENDING

    # model_config = ConfigDict(
    #     json_encoders={datetime: lambda value: value.strftime("%Y-%m-%d %H:%M:%S")}
    # )

    @field_serializer("created_at")
    def serialize_datetime(self, created_at: datetime):
        return created_at.strftime("%Y-%m-%d %H:%M:%S")


class UpdateJob(BaseModel):
    id: JobId
    name: str | None = None
    type: JobType | None = None
    status: JobStatus | None = None
