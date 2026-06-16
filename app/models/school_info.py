from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base
from datetime import datetime, timezone


class SchoolInfo(Base):
    __tablename__ = "school_info"

    id = Column(Integer, primary_key=True, index=True)
    about = Column(Text, nullable=True)
    mission = Column(Text, nullable=True)
    achievements = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))