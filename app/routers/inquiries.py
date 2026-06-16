from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.inquiry import Inquiry
from app.models.user import User
from app.schemas.inquiry import InquiryCreate, InquiryResponse
from app.routers.auth import get_current_admin

router = APIRouter(prefix="/inquiries", tags=["Inquiries"])


@router.post("", response_model=InquiryResponse)
def send_inquiry(inquiry: InquiryCreate, db: Session = Depends(get_db)):
    db_inquiry = Inquiry(**inquiry.model_dump())
    db.add(db_inquiry)
    db.commit()
    db.refresh(db_inquiry)
    return db_inquiry


@router.get("", response_model=List[InquiryResponse])
def get_inquiries(
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    return db.query(Inquiry).order_by(Inquiry.created_at.desc()).all()