from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    duration: Optional[str] = None
    seats: Optional[int] = None
    requirements: Optional[str] = None


class CourseCreate(CourseBase):
    name: Optional[str] = None


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[str] = None
    seats: Optional[int] = None
    requirements: Optional[str] = None


class CourseResponse(CourseBase):
    id: int
    name: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True