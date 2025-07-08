"""
Tests for task list endpoints: /lists, /lists/{list_id}, etc.
"""


def login(client):
    """Helper to log in and return an access token. Raises on failure."""
    login_payload = {
        "username": "testuser",
        "password": "Testpass123!",
    }
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
    token = login(client)
    # First, create a list to ensure there is one to fetch
    payload = {"title": "Costco", "description": "Large Weekly shopping"}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    create_response = client.post("/lists/", json=payload, headers=headers)
    assert create_response.status_code == 200 or create_response.status_code == 201
    created = create_response.json()
    list_id = created.get("id")
    assert list_id is not None
    # Now, fetch the unique list
    response = client.get(f"/lists/{list_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == list_id
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]


def test_update_list(client):
    token = login(client)
    # Create a list to update
    payload = {"title": "Costco", "description": "Large Weekly shopping"}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    create_response = client.post("/lists/", json=payload, headers=headers)
    assert create_response.status_code == 200 or create_response.status_code == 201
    created = create_response.json()
    list_id = created.get("id")
    assert list_id is not None
    # Update the list
    update_payload = {"title": "Updated Title", "description": "Updated description"}
    response = client.put(f"/lists/{list_id}", json=update_payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == list_id
    assert data["title"] == update_payload["title"]
    assert data["description"] == update_payload["description"]


def test_delete_list(client):
    token = login(client)
    # Create a list to delete
    payload = {"title": "Costco", "description": "Large Weekly shopping"}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    create_response = client.post("/lists/", json=payload, headers=headers)
    assert create_response.status_code == 200 or create_response.status_code == 201
    created = create_response.json()
    list_id = created.get("id")
    assert list_id is not None
    # Delete the list
    response = client.delete(f"/lists/{list_id}", headers=headers)
    assert response.status_code == 200 or response.status_code == 204
    # Confirm it is deleted
    get_response = client.get(f"/lists/{list_id}", headers=headers)
    assert get_response.status_code == 404
