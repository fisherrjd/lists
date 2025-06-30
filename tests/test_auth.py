"""
Tests for authentication endpoints: /auth/register and /auth/login
"""


def test_register(client):
    payload = {"email": "testuser@example.com", "password": "testpassword"}
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 200


def test_login(client):
    # First, register the user
    payload = {"email": "testuser2@example.com", "password": "testpassword1!"}
    client.post("/auth/register", json=payload)
    # Now, login with form data
    response = client.post(
        "/auth/login",
        data={"username": "testuser2@example.com", "password": "testpassword1!"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
