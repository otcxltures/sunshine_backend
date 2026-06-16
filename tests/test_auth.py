def test_register(client):
    response = client.post("/auth/register", json={
        "email": "user@test.com",
        "password": "password123",
        "full_name": "Test User"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_login(client, db):
    from app.models.user import User
    from app.core.security import get_password_hash

    user = User(
        email="login@test.com",
        hashed_password=get_password_hash("pass123"),
        full_name="Login User"
    )
    db.add(user)
    db.commit()

    response = client.post("/auth/login", data={
        "username": "login@test.com",
        "password": "pass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_login_invalid(client):
    response = client.post("/auth/login", data={
        "username": "wrong@test.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401