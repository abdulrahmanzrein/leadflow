import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OutreachEmailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    company_id: uuid.UUID
    contact_id: uuid.UUID | None
    diagnosis_id: uuid.UUID | None
    subject: str | None
    body_text: str | None
    variant: str
    status: str
    approved_at: datetime | None
    sent_at: datetime | None
    opened_at: datetime | None
    replied_at: datetime | None
    message_id: str | None
    sendgrid_status: str | None
    created_at: datetime
    updated_at: datetime


class OutreachStatusUpdate(BaseModel):
    status: str
