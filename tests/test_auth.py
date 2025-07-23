"""
Tests for authentication endpoints: /auth/register and /auth/login
"""


def test_register(registered_users):
    # Test that 3 users were registered and have expected fields
    assert len(registered_users) == 3
    for user in registered_users:
        assert "username" in user
        assert "email" in user
        assert "password" in user
        assert "id" in user


def test_login(client, registered_users):
    # Use the first registered user to test login
    user = registered_users[0]
    login_payload = {"username": user["username"], "password": user["password"]}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    login_response = client.post("/auth/login", data=login_payload, headers=headers)
    assert login_response.status_code in (200, 201)
    login_data = login_response.json()
    assert "access_token" in login_data or "token" in login_data
