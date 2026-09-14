from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    date_of_birth = Column(Date, nullable=True)
    sex = Column(String(20), nullable=True)

    user = relationship("User", back_populates="patient")

    medications = relationship(
        "Medication",
        back_populates="patient"
    )