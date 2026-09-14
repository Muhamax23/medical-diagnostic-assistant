from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class SessionDiagnosis(Base):
    __tablename__ = "session_diagnoses"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("diagnostic_sessions.id"),
        nullable=False
    )

    diagnosis_id = Column(
        Integer,
        ForeignKey("diagnoses.id"),
        nullable=False
    )

    rank = Column(Integer, nullable=True)

    confidence = Column(Float, nullable=True)

    supporting_evidence = Column(Text, nullable=True)

    contradicting_evidence = Column(Text, nullable=True)

    session = relationship("DiagnosticSession")
    diagnosis = relationship("Diagnosis")
    