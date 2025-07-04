"""
Tests for authentication endpoints: /auth/register and /auth/login
"""


def test_register(client):
    payload = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "Testpass123!",
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert "email" in data
    assert data["email"] == payload["email"]
    assert "id" in data


def test_login(client):
    # First, register the user
    pass
