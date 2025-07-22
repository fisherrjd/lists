"""
Tests for sharing endpoints: /lists/{list_id}/share, /invites, etc.
"""


def login(client, username, password):
    login_payload = {"username": username, "password": password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    login_response = client.post("/auth/login", data=login_payload, headers=headers)
    if not (200 <= login_response.status_code < 300):
        raise RuntimeError(
            f"Login failed: {login_response.status_code} {login_response.text}"
        )
    login_data = login_response.json()
    token = login_data.get("access_token") or login_data.get("token")
    if not token:
        raise RuntimeError("No access token in login response")
    return token


def register_user(client, email, username, password):
    payload = {"email": email, "username": username, "password": password}
    response = client.post("/auth/register", json=payload)
    assert response.status_code in (200, 201)
    return response.json()


def create_list(client, token, title, description):
    pass


def setup_users_and_tokens(client):
    users = [
        {"email": "user1@example.com", "username": "user1", "password": "password1#"},
        {"email": "user2@example.com", "username": "user2", "password": "password2#"},
        {"email": "user3@example.com", "username": "user3", "password": "password3#"},
    ]
    tokens = {}
    for user in users:
        register_user(client, user["email"], user["username"], user["password"])
        tokens[user["username"]] = login(client, user["username"], user["password"])
    return tokens


def test_share_list(client):
    pass


def test_accept_invite(client):
    pass


def test_reject_invite(client):
    pass
