from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.school_info import SchoolInfo
from app.models.user import User
from app.schemas.school_info import SchoolInfoCreate, SchoolInfoResponse
from app.routers.auth import get_current_admin

router = APIRouter(tags=["School Info"])


@router.get("/school-info", response_model=SchoolInfoResponse)
def get_school_info(db: Session = Depends(get_db)):
    info = db.query(SchoolInfo).first()
    if not info:
        info = SchoolInfo(
            about="Sunshine School is a leading institution in Nairobi offering practical, career-focused programmes.",
            mission="To equip students with the skills and knowledge to thrive in a competitive world.",
            achievements="Best Vocational School 2023, 95% Graduate Employment Rate"
        )
        db.add(info)
        db.commit()
        db.refresh(info)
    return info


@router.put("/school-info", response_model=SchoolInfoResponse)
def update_school_info(
    info: SchoolInfoCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_info = db.query(SchoolInfo).first()
    if not db_info:
        db_info = SchoolInfo(**info.model_dump())
        db.add(db_info)
    else:
        for field, value in info.model_dump(exclude_unset=True).items():
            setattr(db_info, field, value)

    db.commit()
    db.refresh(db_info)
    return db_info