import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DiagnosisResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    company_id: uuid.UUID
    symptoms: str
    root_causes: list
    business_impact: str | None
    opportunity: str | None
    model_used: str | None
    prompt_version: str | None
    created_at: datetime
