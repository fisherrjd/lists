"""
Tests for authentication endpoints: /auth/register and /auth/login
"""


def test_register(client):
    import uuid

    unique = str(uuid.uuid4())[:8]
    username = f"testuser_{unique}"
    email = f"{username}@example.com"
    payload = {
        "email": email,
        "username": username,
        "password": "Testpass123!",
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code in (200, 201)
    data = response.json()
    assert "email" in data
    assert data["email"] == payload["email"]
    assert "username" in data
    assert data["username"] == payload["username"]
    assert "id" in data


def test_login(client):
    import uuid

    unique = str(uuid.uuid4())[:8]
    username = f"testuser_{unique}"
    email = f"{username}@example.com"
    password = "Testpass123!"
    # Register a unique user
    payload = {"email": email, "username": username, "password": password}
    response = client.post("/auth/register", json=payload)
    assert response.status_code in (200, 201)
    # Now attempt to log in with the same credentials
    login_payload = {"username": username, "password": password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    login_response = client.post("/auth/login", data=login_payload, headers=headers)
    assert login_response.status_code in (200, 201)
    login_data = login_response.json()
    assert "access_token" in login_data or "token" in login_data
