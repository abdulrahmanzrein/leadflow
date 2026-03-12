import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CompanyCreate(BaseModel):
    name: str
    domain: str | None = None
    industry: str | None = None
    sub_industry: str | None = None
    employee_count: int | None = None
    revenue_estimate: int | None = None
    country: str | None = None
    state: str | None = None
    city: str | None = None
    linkedin_url: str | None = None
    description: str | None = None
    source: str | None = None
    source_url: str | None = None


class CompanyUpdate(BaseModel):
    name: str | None = None
    domain: str | None = None
    industry: str | None = None
    sub_industry: str | None = None
    employee_count: int | None = None
    revenue_estimate: int | None = None
    country: str | None = None
    state: str | None = None
    city: str | None = None
    linkedin_url: str | None = None
    description: str | None = None
    status: str | None = None


class CompanyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    domain: str | None
    industry: str | None
    sub_industry: str | None
    employee_count: int | None
    revenue_estimate: int | None
    country: str | None
    state: str | None
    city: str | None
    linkedin_url: str | None
    description: str | None
    source: str | None
    source_url: str | None
    status: str
    lead_score: int
    lead_band: str | None
    pipeline_run_id: uuid.UUID | None
    created_at: datetime
    updated_at: datetime


class CompanyListResponse(BaseModel):
    items: list[CompanyResponse]
    total: int
    page: int
    page_size: int
