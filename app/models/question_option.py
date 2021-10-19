from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Column, Text, ForeignKey, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Question_option(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String(3), nullable=False)
    text = Column(Text(), nullable=False)
    weight = Column(Integer(), nullable=False)

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)

    # Relacion Muchos a 1
    questions = relationship("Question", back_populates="question_options")