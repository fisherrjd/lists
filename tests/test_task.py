import pytest


# Fixture to create a task and return its data and auth headers
@pytest.fixture
def created_task(client, registered_users, created_list):
    user = registered_users[0]
    list_id = created_list["id"]
    token = user["access_token"]
    task_payload = {"title": "Apples", "quantity": 1, "completed": False}
    auth_headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post(
        f"/tasks/list/{list_id}", json=task_payload, headers=auth_headers
    )
    assert create_response.status_code in (200, 201)
    data = create_response.json()
    return {
        "id": data["id"],
        "list_id": list_id,
        "token": token,
        "payload": task_payload,
        "auth_headers": auth_headers,
    }


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


def test_create_task(client, registered_users, created_list):
    user = registered_users[0]
    list_id = created_list["id"]
    token = user["access_token"]
    task_payload = {"title": "Pears", "quantity": 1, "completed": False}
    auth_headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post(
        f"/tasks/list/{list_id}", json=task_payload, headers=auth_headers
    )
    assert create_response.status_code in (200, 201)
    data = create_response.json()
    assert "id" in data
    assert data["title"] == task_payload["title"]
    assert data["quantity"] == task_payload["quantity"]
    assert data["completed"] == task_payload["completed"]


def test_update_task(client, created_task):
    task_id = created_task["id"]
    auth_headers = created_task["auth_headers"]
    update_payload = {"title": "Oranges", "quantity": 2, "completed": True}
    response = client.put(
        f"/tasks/{task_id}", json=update_payload, headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == update_payload["title"]
    assert data["quantity"] == update_payload["quantity"]
    assert data["completed"] == update_payload["completed"]


def test_delete_task(client, created_task):
    task_id = created_task["id"]
    auth_headers = created_task["auth_headers"]
    # Delete the task
    response = client.delete(f"/tasks/{task_id}", headers=auth_headers)
    assert response.status_code in (200, 204)
    # Try to get the deleted task, should return 404
    get_response = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert get_response.status_code == 405
