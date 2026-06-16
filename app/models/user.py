from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    firebase_uid = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    applications = relationship("Application", back_populates="user", cascade="all, delete-orphan")