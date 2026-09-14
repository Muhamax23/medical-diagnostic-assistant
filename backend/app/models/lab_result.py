from sqlalchemy import Column, Integer, Text, Float, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class LabResult(Base):
    __tablename__ = "lab_results"

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

    test_name = Column(String(200), nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String(50), nullable=True)
    reference_range = Column(String(100), nullable=True)
    abnormal_flag = Column(String(10), nullable=True)
    notes = Column(Text, nullable=True)

    recorded_at = Column(
        String(100),
        nullable=False,
        server_default=func.now()
    )

    patient = relationship("Patient")
    session = relationship("DiagnosticSession")