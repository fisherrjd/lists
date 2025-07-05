"""
Tests for task list endpoints: /lists, /lists/{list_id}, etc.
"""


def login(client):
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
    return login_data.get("access_token") or login_data.get("token")


def test_create_list(client):
    token = login(client)
    payload = {"title": "Costco", "description": "Large Weekly shopping"}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = client.post("/lists/", json=payload, headers=headers)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]


def test_get_lists(client):
    token = login(client)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = client.get("/lists/", headers=headers)
    assert response.status_code == 200 or response.status_code == 201


def test_get_unique_list(client):
    pass  # TODO: Implement get lists test


def test_update_list(client):
    pass  # TODO: Implement update list test


def test_delete_list(client):
    pass  # TODO: Implement delete list test
