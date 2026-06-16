import pytest
from app.models.course import Course


def test_get_courses_empty(client):
    response = client.get("/courses")
    assert response.status_code == 200
    assert response.json() == []


def test_create_course(client, db):
    from app.models.user import User
    from app.core.security import get_password_hash

    admin = User(
        email="admin@test.com",
        hashed_password=get_password_hash("admin123"),
        is_admin=True
    )
    db.add(admin)
    db.commit()

    login = client.post("/auth/login", data={
        "username": "admin@test.com",
        "password": "admin123"
    })
    token = login.json()["access_token"]

    response = client.post(
        "/courses",
        json={"title": "Test Course", "description": "Test Desc", "duration": "3 months"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Course"
    assert data["description"] == "Test Desc"


def test_get_courses_with_data(client, db):
    course = Course(title="Python 101", description="Learn Python", duration="3 months")
    db.add(course)
    db.commit()

    response = client.get("/courses")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Python 101"