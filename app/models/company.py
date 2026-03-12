import uuid
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class Company(Base, TimestampMixin):
    __tablename__ = "companies"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    domain: Mapped[str | None] = mapped_column(String(255), unique=True, index=True)
    industry: Mapped[str | None] = mapped_column(String(100))
    sub_industry: Mapped[str | None] = mapped_column(String(100))
    employee_count: Mapped[int | None] = mapped_column(Integer)
    revenue_estimate: Mapped[int | None] = mapped_column(BigInteger)
    country: Mapped[str | None] = mapped_column(String(100))
    state: Mapped[str | None] = mapped_column(String(100))
    city: Mapped[str | None] = mapped_column(String(100))
    linkedin_url: Mapped[str | None] = mapped_column(String(500))
    description: Mapped[str | None] = mapped_column(Text)
    source: Mapped[str | None] = mapped_column(String(100))
    source_url: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(50), default="discovered", nullable=False, index=True)
    lead_score: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    lead_band: Mapped[str | None] = mapped_column(String(20), index=True)
    pipeline_run_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    signals: Mapped[list["Signal"]] = relationship(
        "Signal", back_populates="company", cascade="all, delete-orphan"
    )
    contacts: Mapped[list["Contact"]] = relationship(
        "Contact", back_populates="company", cascade="all, delete-orphan"
    )
    diagnoses: Mapped[list["Diagnosis"]] = relationship(
        "Diagnosis", back_populates="company", cascade="all, delete-orphan"
    )
    outreach_emails: Mapped[list["OutreachEmail"]] = relationship(
        "OutreachEmail", back_populates="company", cascade="all, delete-orphan"
    )
