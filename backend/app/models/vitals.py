from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class Vitals(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    session_id = Column(
        Integer,
        ForeignKey("diagnostic_sessions.id"),
        nullable=False
    )

    systolic_bp = Column(Integer, nullable=True)
    diastolic_bp = Column(Integer, nullable=True)

    heart_rate = Column(Integer, nullable=True)

    temperature = Column(String(10), nullable=True)

    respiratory_rate = Column(Integer, nullable=True)

    oxygen_saturation = Column(Float, nullable=True)

    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
        )

    patient = relationship("Patient")
    session = relationship("DiagnosticSession")
    