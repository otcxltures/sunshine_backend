from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.application import Application
from app.models.course import Course
from app.models.user import User
from app.schemas.application import ApplicationCreate, ApplicationUpdate, ApplicationResponse
from app.routers.auth import get_current_user, get_current_admin

router = APIRouter(tags=["Applications"])


@router.post("/apply", response_model=ApplicationResponse)
def submit_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    course = db.query(Course).filter(Course.id == application.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    db_app = Application(
        name=application.name,
        email=application.email or (current_user.email if current_user else None),
        course_id=application.course_id,
        user_id=current_user.id if current_user else None,
        message=application.message,
        status="Pending"
    )
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app


@router.get("/applications/me", response_model=List[ApplicationResponse])
def get_my_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    return db.query(Application).filter(Application.user_id == current_user.id).all()


@router.get("/applications", response_model=List[ApplicationResponse])
def get_all_applications(
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    return db.query(Application).all()


@router.put("/applications/{application_id}", response_model=ApplicationResponse)
def update_application_status(
    application_id: int,
    status_update: ApplicationUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_app = db.query(Application).filter(Application.id == application_id).first()
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")

    db_app.status = status_update.status
    db.commit()
    db.refresh(db_app)
    return db_app