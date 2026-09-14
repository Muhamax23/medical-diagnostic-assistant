from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class FollowUpQuestion(Base):
    __tablename__ = "follow_up_questions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("diagnostic_sessions.id"),
        nullable=False
    )

    question = Column(Text, nullable=False)

    reason = Column(Text, nullable=True)

    priority = Column(String(20), nullable=True)

    answer = Column(Text, nullable=True)

    answered_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    session = relationship("DiagnosticSession")