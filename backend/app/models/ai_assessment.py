from sqlalchemy import Column, Integer, Float, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class AIAssessment(Base):
    __tablename__ = "ai_assessments"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("diagnostic_sessions.id"),
        nullable=False,
        unique=True
    )

    risk_level = Column(String(50), nullable=True)

    summary = Column(Text, nullable=True)

    uncertainty = Column(Float, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    session = relationship("DiagnosticSession")