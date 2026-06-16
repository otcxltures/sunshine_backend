from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ApplicationBase(BaseModel):
    name: str
    email: Optional[str] = None
    course_id: int
    message: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    status: str


class ApplicationResponse(ApplicationBase):
    id: int
    user_id: Optional[int] = None
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True