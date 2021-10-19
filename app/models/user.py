import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, CHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    """
    Database Model for an application user
    """
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    gender = Column(CHAR(), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    # Relacion 1 a muchos
    surveys = relationship("Survey", back_populates="users")
    answers = relationship("Answer", back_populates="users")