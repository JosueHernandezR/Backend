import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Column, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Survey(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    title = Column(Text(), nullable=False)
    create_at = Column(DateTime, default=datetime.datetime.utcnow())
    expire_at = Column(DateTime, nullable=False)

    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relacion 1 a muchos
    questions = relationship("Question", back_populates="surveys")

    # Relacion muchos a 1
    users = relationship("User", back_populates="surveys")
