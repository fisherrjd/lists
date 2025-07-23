"""
Tests for task list endpoints: /lists, /lists/{list_id}, etc.
"""


def login_and_get_token(client, username, password):
    login_payload = {"username": username, "password": password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = client.post("/auth/login", data=login_payload, headers=headers)
    assert response.status_code in (200, 201)
    token = response.json().get("access_token") or response.json().get("token")
    assert token
    return token


def test_create_list(client, registered_users):
    user = registered_users[0]
    token = login_and_get_token(client, user["username"], user["password"])
    list_payload = {"title": "Costco", "description": "Test Costco Shopping List"}
    auth_headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post("/lists/", json=list_payload, headers=auth_headers)
    assert create_response.status_code in (200, 201)
    data = create_response.json()
    assert data["title"] == list_payload["title"]
    assert data["description"] == list_payload["description"]
    assert "id" in data


def test_get_unique_list(client):
    pass


def test_update_list(client):
    pass


def test_delete_list(client):
    pass
