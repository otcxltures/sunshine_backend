from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InquiryBase(BaseModel):
    name: str
    email: str
    message: str


class InquiryCreate(InquiryBase):
    pass


class InquiryResponse(InquiryBase):
    id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True