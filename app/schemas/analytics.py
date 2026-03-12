from pydantic import BaseModel


class OverviewStats(BaseModel):
    total_companies: int
    hot_leads: int
    warm_leads: int
    emails_sent: int
    emails_opened: int
    emails_replied: int
    open_rate: float
    reply_rate: float
    pipeline_runs_total: int
    last_run_status: str | None


class LeadDistribution(BaseModel):
    hot: int
    warm: int
    cool: int
    cold: int


class OutreachStats(BaseModel):
    total_sent: int
    total_opened: int
    total_replied: int
    total_bounced: int
    open_rate: float
    reply_rate: float
    bounce_rate: float


class PipelineThroughput(BaseModel):
    run_id: str
    started_at: str
    companies_discovered: int
    companies_scored: int
    emails_generated: int
    emails_sent: int
    duration_seconds: int | None
    status: str
