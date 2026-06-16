from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    duration = Column(String, nullable=True)
    seats = Column(Integer, nullable=True)
    requirements = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    applications = relationship("Application", back_populates="course", cascade="all, delete-orphan")