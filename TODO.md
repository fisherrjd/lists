# Lists API Endpoints

## Users & Authentication

| Method | Path                  | Description                        |
|--------|-----------------------|------------------------------------|
| POST   | /auth/register        | Register a new user                |
| POST   | /auth/login           | User login                         |
| GET    | /auth-methods         | List available authentication methods |

## Lists

| Method | Path                        | Description                |
|--------|-----------------------------|----------------------------|
| GET    | /lists                      | Get all lists for the user |
| POST   | /lists                      | Create a new list          |
| GET    | /lists/{list_id}            | Get a specific list        |
| PUT    | /lists/{list_id}            | Update a list              |
| DELETE | /lists/{list_id}            | Delete a list              |

### Tasks

| Method | Path                                         | Description              |
|--------|----------------------------------------------|--------------------------|
| POST   | /lists/{list_id}/tasks                       | Add a task to a list     |
| PUT    | /lists/{list_id}/tasks/{task_id}             | Update a task in a list  |

## Sharing

| Method | Path                                 | Description                |
|--------|--------------------------------------|----------------------------|
| POST   | /lists/{list_id}/share               | Share a list with a user   |
| GET    | /invites                            | Get all invites for user   |
| POST   | /invites/{invite_id}/accept         | Accept an invite           |
| POST   | /invites/{invite_id}/reject         | Reject an invite           |

---

## Data Models

### users

- id: UUID
- email: str (unique)
- hashed_password: str
- created_at: datetime

### lists

- id: UUID
- title: str
- owner_id: UUID (foreign key to users.id)
- created_at: datetime
- updated_at: datetime

### tasks

- id: UUID
- list_id: UUID (foreign key to lists.id)
- title: str
- completed: bool
- created_at: datetime
- updated_at: datetime

### list_shares

- list_id: UUID (foreign key to lists.id)
- user_id: UUID (foreign key to users.id)
- role: ENUM('owner', 'editor', 'viewer')
- invited_at: datetime
- accepted_at: datetime

---

## Project Structure Example

```
task_list_app/
│
├── main.py                          # App entry point
├── requirements.txt                 # Dependencies
├── .env                             # Environment variables
│
├── core/
│   └── config.py                    # Settings loading
│
├── models/                          # ORM Models
│   ├── user.py
│   ├── list.py
│   ├── task.py
│   └── list_share.py
│
├── schemas/                         # Pydantic models for request/response
│   ├── auth.py
│   ├── list.py
│   ├── task.py
│   └── share.py
│
├── services/                        # Business logic
│   ├── auth_service.py
│   ├── list_service.py
│   └── share_service.py
│
├── api/
│   └── v1/
│       ├── auth.py                  # Auth routes
│       ├── lists.py                 # List CRUD
│       ├── tasks.py                 # Task CRUD
│       └── shares.py                # Sharing logic
│
├── auth/
│   ├── security.py                  # JWT, password hashing
│   └── dependencies.py              # get_current_user etc.
│
└── utils/
    └── helpers.py                   # Helper functions
```
