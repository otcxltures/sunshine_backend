from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.announcement import Announcement
from app.models.user import User
from app.schemas.announcement import AnnouncementCreate, AnnouncementUpdate, AnnouncementResponse
from app.routers.auth import get_current_admin

router = APIRouter(prefix="/announcements", tags=["Announcements"])


@router.get("", response_model=List[AnnouncementResponse])
def get_announcements(db: Session = Depends(get_db)):
    return db.query(Announcement).order_by(Announcement.created_at.desc()).all()


@router.post("", response_model=AnnouncementResponse)
def create_announcement(
    announcement: AnnouncementCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_announcement = Announcement(**announcement.model_dump())
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement


@router.put("/{announcement_id}", response_model=AnnouncementResponse)
def update_announcement(
    announcement_id: int,
    announcement: AnnouncementUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_announcement = db.query(Announcement).filter(Announcement.id == announcement_id).first()
    if not db_announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    for field, value in announcement.model_dump().items():
        setattr(db_announcement, field, value)

    db.commit()
    db.refresh(db_announcement)
    return db_announcement


@router.delete("/{announcement_id}")
def delete_announcement(
    announcement_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_announcement = db.query(Announcement).filter(Announcement.id == announcement_id).first()
    if not db_announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    db.delete(db_announcement)
    db.commit()
    return {"message": "Announcement deleted successfully"}