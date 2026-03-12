import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PipelineRunRequest(BaseModel):
    triggered_by: str = "api"
    skip_stages: list[str] = []
    stop_on_failure: bool = True


class PipelineStageTrigger(BaseModel):
    stage: str
    company_id: uuid.UUID | None = None


class PipelineRunResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    triggered_by: str | None
    status: str
    stages_completed: list
    companies_discovered: int
    companies_scored: int
    emails_generated: int
    emails_sent: int
    errors: list
    started_at: datetime
    completed_at: datetime | None
    duration_seconds: int | None
