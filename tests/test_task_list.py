import pytest


# Fixture to create a list and return its data and auth headers
@pytest.fixture
def created_list(client, registered_users):
    user = registered_users[0]
    token = user["access_token"]
    list_payload = {"title": "Costco", "description": "Test Costco Shopping List"}
    auth_headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post("/lists/", json=list_payload, headers=auth_headers)
    assert create_response.status_code in (200, 201)
    data = create_response.json()
    return {
        "id": data["id"],
        "token": token,
        "payload": list_payload,
        "auth_headers": auth_headers,
    }


def test_create_list(client, registered_users):
    user = registered_users[0]
    token = user["access_token"]
    list_payload = {"title": "Costco", "description": "Test Costco Shopping List"}
    auth_headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post("/lists/", json=list_payload, headers=auth_headers)
    assert create_response.status_code in (200, 201)
    data = create_response.json()
    assert data["title"] == list_payload["title"]
    assert data["description"] == list_payload["description"]
    assert "id" in data


def test_get_unique_list(client, created_list):
    list_id = created_list["id"]
    auth_headers = created_list["auth_headers"]
    response = client.get(f"/lists/{list_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == list_id
    assert data["title"] == created_list["payload"]["title"]
    assert data["description"] == created_list["payload"]["description"]


def test_update_list(client, created_list):
    list_id = created_list["id"]
    auth_headers = created_list["auth_headers"]
    list_payload = {"title": "Target", "description": "Test Target Shopping List"}
    response = client.put(f"/lists/{list_id}", json=list_payload, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == list_id
    assert data["title"] == list_payload["title"]
    assert data["description"] == list_payload["description"]


def test_delete_list(client, created_list):
    list_id = created_list["id"]
    auth_headers = created_list["auth_headers"]
    # Delete the list
    response = client.delete(f"/lists/{list_id}", headers=auth_headers)
    assert response.status_code in (200, 204)
    # Try to get the deleted list, should return 404
    get_response = client.get(f"/lists/{list_id}", headers=auth_headers)
    assert get_response.status_code == 404
