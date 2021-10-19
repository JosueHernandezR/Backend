from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Question(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    question = Column(Text(), nullable=False)
    accept_open_answer = Column(Boolean(), nullable=False)
    is_mandatory = Column(Boolean(), default=True, nullable=False)

    survey_id = Column(UUID(as_uuid=True), ForeignKey("surveys.id"), nullable=False)

    # Relacion 1 a muchos
    question_options = relationship("Question_option", back_populates="questions")

    # Relacion muchos a 1
    surveys = relationship("Survey", back_populates="questions")
    answers = relationship("Answer", back_populates="questions")
