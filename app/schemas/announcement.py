from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AnnouncementBase(BaseModel):
    title: str
    content: str


class AnnouncementCreate(AnnouncementBase):
    pass


class AnnouncementUpdate(AnnouncementBase):
    pass


class AnnouncementResponse(AnnouncementBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True