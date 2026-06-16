import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routers import auth, courses, applications, announcements, school_info, inquiries


from app.models.user import User
from app.models.course import Course
from app.models.application import Application
from app.models.announcement import Announcement
from app.models.school_info import SchoolInfo
from app.models.inquiry import Inquiry


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sunshine School API",
    description="Backend API for Sunshine School Course Portal",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(applications.router)
app.include_router(announcements.router)
app.include_router(school_info.router)
app.include_router(inquiries.router)


@app.get("/")
def root():
    return {
        "message": "Sunshine School API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)