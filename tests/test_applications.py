import pytest
from app.models.course import Course
from app.models.application import Application


def test_submit_application(client, db):
    course = Course(title="Test Course", description="Test", duration="3 months")
    db.add(course)
    db.commit()

    response = client.post("/apply", json={
        "name": "John Doe",
        "email": "john@test.com",
        "course_id": course.id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["status"] == "Pending"


def test_get_all_applications_admin(client, db):
    from app.models.user import User
    from app.core.security import get_password_hash

    admin = User(
        email="admin@test.com",
        hashed_password=get_password_hash("admin123"),
        is_admin=True
    )
    db.add(admin)

    course = Course(title="Test Course", description="Test", duration="3 months")
    db.add(course)
    db.commit()

    app = Application(name="John", course_id=course.id, status="Pending")
    db.add(app)
    db.commit()

    login = client.post("/auth/login", data={
        "username": "admin@test.com",
        "password": "admin123"
    })
    token = login.json()["access_token"]

    response = client.get("/applications", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1