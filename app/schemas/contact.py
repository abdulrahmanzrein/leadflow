import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class ContactCreate(BaseModel):
    company_id: uuid.UUID
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    title: str | None = None
    seniority: str | None = None
    department: str | None = None
    linkedin_url: str | None = None
    source: str | None = None
    is_primary: bool = False


class ContactUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    title: str | None = None
    seniority: str | None = None
    department: str | None = None
    linkedin_url: str | None = None
    is_primary: bool | None = None
    email_verified: bool | None = None


class ContactResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    company_id: uuid.UUID
    first_name: str | None
    last_name: str | None
    email: str | None
    email_verified: bool
    title: str | None
    seniority: str | None
    department: str | None
    linkedin_url: str | None
    source: str | None
    is_primary: bool
    created_at: datetime
