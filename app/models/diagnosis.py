import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class Diagnosis(Base, TimestampMixin):
    __tablename__ = "diagnoses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("companies.id", ondelete="CASCADE"), nullable=False
    )
    symptoms: Mapped[str] = mapped_column(Text, nullable=False)
    root_causes: Mapped[list] = mapped_column(JSONB, nullable=False)
    business_impact: Mapped[str | None] = mapped_column(Text)
    opportunity: Mapped[str | None] = mapped_column(Text)
    model_used: Mapped[str | None] = mapped_column(String(100))
    prompt_version: Mapped[str | None] = mapped_column(String(20))
    raw_llm_response: Mapped[str | None] = mapped_column(Text)

    company: Mapped["Company"] = relationship("Company", back_populates="diagnoses")
    outreach_emails: Mapped[list["OutreachEmail"]] = relationship(
        "OutreachEmail", back_populates="diagnosis"
    )
