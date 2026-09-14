from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(200),
        unique=True,
        nullable=False,
        index=True
    )

    description = Column(Text, nullable=True)