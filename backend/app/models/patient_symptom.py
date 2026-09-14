from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class PatientSymptom(Base):
    __tablename__ = "patient_symptoms"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    symptom_id = Column(
        Integer,
        ForeignKey("symptoms.id"),
        nullable=False
    )

    severity = Column(Integer, nullable=True)
    duration = Column(String(100), nullable=True)
    onset = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)

    patient = relationship("Patient")
    symptom = relationship("Symptom")