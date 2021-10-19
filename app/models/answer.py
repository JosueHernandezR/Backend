import datetime

from uuid import uuid4
from app.db.base_class import Base
from sqlalchemy import Column, Text, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Answer(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    weight = Column(Integer(), nullable= False)
    open_answer = Column(Text(), nullable=True)
    answered_at=Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    option_id = Column(UUID(as_uuid=True), nullable=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)
    surveyed_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relacion muchos a uno
    users = relationship("User", back_populates="answers")
    questions = relationship("Question", back_populates="answers")
