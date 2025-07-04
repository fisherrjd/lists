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
    assert "username" in data
    assert data["username"] == payload["username"]
    assert "id" in data


def test_login(client):
    # Register the user first
    register_payload = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "Testpass123!",
    }
    reg_response = client.post("/auth/register", json=register_payload)
    assert reg_response.status_code == 200 or reg_response.status_code == 201

    # Now attempt to log in with the same credentials (form-encoded, using username)
    login_payload = {
        "username": "testuser",
        "password": "Testpass123!",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    login_response = client.post("/auth/login", data=login_payload, headers=headers)
    assert login_response.status_code == 200 or login_response.status_code == 201
    login_data = login_response.json()
    assert "access_token" in login_data or "token" in login_data
