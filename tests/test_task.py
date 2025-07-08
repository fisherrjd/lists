"""
Tests for task endpoints: /lists/{list_id}/tasks, etc.
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


def create_list(client, token):
    payload = {"title": "Test List", "description": "Test Description"}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = client.post("/lists/", json=payload, headers=headers)
    assert response.status_code in (200, 201)
    return response.json()


def test_create_task(client):
    token = login(client)
    task_list = create_list(client, token)
    list_id = task_list["id"]
    payload = {"title": "Test Task", "completed": False, "quantity": 2}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = client.post(f"/tasks/list/{list_id}", json=payload, headers=headers)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["completed"] == payload["completed"]
    assert data["quantity"] == payload["quantity"]
    assert data["task_list_id"] == list_id


def test_update_task(client):
    token = login(client)
    task_list = create_list(client, token)
    list_id = task_list["id"]
    # Create a task first
    task_payload = {"title": "Task to Update", "completed": False, "quantity": 1}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    create_response = client.post(
        f"/tasks/list/{list_id}", json=task_payload, headers=headers
    )
    assert create_response.status_code in (200, 201)
    task = create_response.json()
    task_id = task["id"]
    # Update the task
    update_payload = {"title": "Updated Task", "completed": True, "quantity": 5}
    update_response = client.put(
        f"/tasks/{task_id}", json=update_payload, headers=headers
    )
    assert update_response.status_code == 200
    updated = update_response.json()
    assert updated["id"] == task_id
    assert updated["title"] == update_payload["title"]
    assert updated["completed"] == update_payload["completed"]
    assert updated["quantity"] == update_payload["quantity"]


def test_delete_task(client):
    token = login(client)
    task_list = create_list(client, token)
    list_id = task_list["id"]
    # Create a task first
    task_payload = {"title": "Task to Delete", "completed": False, "quantity": 3}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    create_response = client.post(
        f"/tasks/list/{list_id}", json=task_payload, headers=headers
    )
    assert create_response.status_code in (200, 201)
    task = create_response.json()
    task_id = task["id"]
    # Delete the task
    delete_response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert delete_response.status_code == 204
    # Confirm it is deleted
    get_response = client.get(f"/tasks/{task_id}", headers=headers)
    assert get_response.status_code == 405
