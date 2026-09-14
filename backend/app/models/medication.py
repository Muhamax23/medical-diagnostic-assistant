from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    name = Column(String(100), unique=True, nullable=False, index=True)
    # description = Column(String(255), nullable=True)
    dosage = Column(String(50), nullable=True)
    frequency = Column(String(50), nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

    patient = relationship("Patient", back_populates="medications")