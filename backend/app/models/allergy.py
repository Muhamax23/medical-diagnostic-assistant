from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    allergen = Column(String(200), nullable=False)
    reaction = Column(String(200), nullable=True)
    severity = Column(String(50), nullable=True)
    # notes = Column(String(500), nullable=True)

    patient = relationship("Patient")
    