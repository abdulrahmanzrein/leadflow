import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SignalCreate(BaseModel):
    company_id: uuid.UUID
    category: str
    signal_type: str | None = None
    title: str | None = None
    content: str | None = None
    source_url: str | None = None
    severity: str = "medium"
    signal_score: float = 0.0
    raw_data: dict | None = None


class SignalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    company_id: uuid.UUID
    category: str
    signal_type: str | None
    title: str | None
    content: str | None
    source_url: str | None
    severity: str
    signal_score: float
    raw_data: dict | None
    created_at: datetime
