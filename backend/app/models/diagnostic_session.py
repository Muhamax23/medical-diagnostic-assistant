from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class DiagnosticSession(Base):
    __tablename__ = "diagnostic_sessions"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    status = Column(String(50), nullable=False, default="active")

    start_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
        )

    end_time = Column(
        DateTime(timezone=True), 
        nullable=True
        )

    # notes = Column(String(500), nullable=True)

    patient = relationship("Patient")