from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class MedicalHistory(Base):
    __tablename__ = "medical_history"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    condition = Column(String(200), nullable=False)
    diagnosed_date = Column(Date, nullable=True)
    status = Column(String(50), nullable=True)
    notes = Column(Text, nullable=True)

    patient = relationship("Patient")