"""
Tests for sharing endpoints: /lists/{list_id}/share, /invites, etc.
"""


def login(client, username="testuser", password="Testpass123!"):
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


def create_list(client, token, title="Shared List", description="A list to share"):
    payload = {"title": title, "description": description}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = client.post("/lists/", json=payload, headers=headers)
    assert response.status_code in (200, 201)
    return response.json()


def test_share_list(client):
    import uuid

    unique = str(uuid.uuid4())[:8]
    owner_email = f"owner_{unique}@example.com"
    owner_username = f"owner_{unique}"
    invitee_email = f"invitee_{unique}@example.com"
    invitee_username = f"invitee_{unique}"
    owner = register_user(client, owner_email, owner_username, "OwnerPass123!")
    invitee = register_user(client, invitee_email, invitee_username, "InviteePass123!")
    owner_token = login(client, owner_username, "OwnerPass123!")
    # Create a list as owner
    task_list = create_list(
        client, owner_token, title="Groceries", description="Weekly shopping"
    )
    list_id = task_list["id"]
    # Share the list with invitee as editor
    from schemas.list_share import RoleEnum

    share_payload = {
        "task_list_id": list_id,
        "user_id": invitee["id"],
        "role": RoleEnum.editor.value,
    }
    headers = {
        "Authorization": f"Bearer {owner_token}",
        "Content-Type": "application/json",
    }
    response = client.post(
        f"/lists/{list_id}/share", json=share_payload, headers=headers
    )
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["task_list_id"] == list_id
    assert data["user_id"] == invitee["id"]
    assert data["role"] == RoleEnum.editor.value


def test_accept_invite(client):
    pass


def test_reject_invite(client):
    pass
