from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models.course import Course
from app.models.user import User
from app.schemas.course import CourseCreate, CourseUpdate, CourseResponse
from app.routers.auth import get_current_admin, get_current_user

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("", response_model=List[CourseResponse])
def get_courses(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Course)
    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (Course.title.ilike(search_filter)) | 
            (Course.description.ilike(search_filter)) |
            (Course.duration.ilike(search_filter))
        )
    return query.offset(skip).limit(limit).all()


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("", response_model=CourseResponse)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    course: CourseUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    update_data = course.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_course, field, value)

    db.commit()
    db.refresh(db_course)
    return db_course


@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(db_course)
    db.commit()
    return {"message": "Course deleted successfully"}