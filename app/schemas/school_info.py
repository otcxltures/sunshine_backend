from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SchoolInfoBase(BaseModel):
    about: Optional[str] = None
    mission: Optional[str] = None
    achievements: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class SchoolInfoCreate(SchoolInfoBase):
    pass


class SchoolInfoResponse(SchoolInfoBase):
    id: int
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True