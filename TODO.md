# Lists API Endpoints

## Implementation Tasks

1. **Project Setup**
    - [x] Create project directory and initialize git
    - [x] Set up Python virtual environment (using `uv`)
    - [x] Create `pyproject.toml` and add dependencies (FastAPI, SQLAlchemy, Pydantic, etc.)
    - [x] Use `uv` to install dependencies and lock them
    - [x] Create `.env` file for environment variables
    - [x] Set up initial folder structure (`core/`, `models/`, `schemas/`, etc.)
    - [x] Create `main.py` with FastAPI app instance
    - [x] Set up configuration management in `core/config.py`
    - [x] Create or update `default.nix` for reproducible builds
    - [x] Test environment setup with `nix develop` and `uv` commands

2. **Database Models**
    - [ ] Design database schema (users, lists, tasks, list_shares)
    - [ ] Implement `User` model (`models/user.py`)
        - [ ] Fields: id, email, hashed_password, created_at
        - [ ] Add SQLAlchemy model class
        - [ ] Add relationships to lists and shares
    - [ ] Implement `List` model (`models/list.py`)
        - [ ] Fields: id, title, owner_id, created_at, updated_at
        - [ ] Add SQLAlchemy model class
        - [ ] Add relationship to tasks and owner
    - [ ] Implement `Task` model (`models/task.py`)
        - [ ] Fields: id, list_id, title, completed, created_at, updated_at
        - [ ] Add SQLAlchemy model class
        - [ ] Add relationship to list
    - [ ] Implement `ListShare` model (`models/list_share.py`)
        - [ ] Fields: list_id, user_id, role, invited_at, accepted_at
        - [ ] Add SQLAlchemy model class
        - [ ] Add relationships to list and user
    - [ ] Set up database connection in `core/config.py` or `db.py`
    - [ ] Set up Alembic for migrations
    - [ ] Create initial migration and apply to database

3. **Pydantic Schemas**
    - [ ] Create `auth.py` schemas (register, login, token)
    - [ ] Create `user.py` schemas (UserRead, UserCreate, etc.)
    - [ ] Create `list.py` schemas (ListRead, ListCreate, ListUpdate, etc.)
    - [ ] Create `task.py` schemas (TaskRead, TaskCreate, TaskUpdate, etc.)
    - [ ] Create `share.py` schemas (ShareRead, ShareCreate, etc.)

4. **Authentication & Authorization**
    - [ ] Implement password hashing utilities in `auth/security.py`
    - [ ] Implement JWT token creation and verification in `auth/security.py`
    - [ ] Create dependency for getting current user in `auth/dependencies.py`
    - [ ] Add role-based access checks (owner, editor, viewer)

5. **Business Logic Services**
    - [ ] Implement authentication service (`services/auth_service.py`)
        - [ ] Register user
        - [ ] Authenticate user and issue JWT
    - [ ] Implement list service (`services/list_service.py`)
        - [ ] Create list
        - [ ] Get all lists for user
        - [ ] Get single list
        - [ ] Update list
        - [ ] Delete list
    - [ ] Implement task service (`services/list_service.py` or `services/task_service.py`)
        - [ ] Add task to list
        - [ ] Update task
        - [ ] Mark task as completed
        - [ ] Delete task
    - [ ] Implement share service (`services/share_service.py`)
        - [ ] Share list with user
        - [ ] Accept/reject invite
        - [ ] List invites

6. **API Endpoints**
    - [ ] Implement auth endpoints (`api/v1/auth.py`)
        - [ ] POST /auth/register
        - [ ] POST /auth/login
        - [ ] GET /auth-methods
    - [ ] Implement list endpoints (`api/v1/lists.py`)
        - [ ] GET /lists
        - [ ] POST /lists
        - [ ] GET /lists/{list_id}
        - [ ] PUT /lists/{list_id}
        - [ ] DELETE /lists/{list_id}
    - [ ] Implement task endpoints (`api/v1/tasks.py`)
        - [ ] POST /lists/{list_id}/tasks
        - [ ] PUT /lists/{list_id}/tasks/{task_id}
    - [ ] Implement sharing endpoints (`api/v1/shares.py`)
        - [ ] POST /lists/{list_id}/share
        - [ ] GET /invites
        - [ ] POST /invites/{invite_id}/accept
        - [ ] POST /invites/{invite_id}/reject

7. **Utilities**
    - [ ] Add helper functions for common tasks (`utils/helpers.py`)
    - [ ] Add error handling utilities
    - [ ] Add response formatting helpers

8. **Testing**
    - [ ] Set up test framework (pytest, add to `pyproject.toml` and `default.nix`)
    - [ ] Write unit tests for models
    - [ ] Write unit tests for services
    - [ ] Write unit tests for endpoints
    - [ ] Write integration tests for API flows

9. **Documentation**
    - [ ] Document API endpoints in README.md
    - [ ] Add usage examples
    - [ ] Document environment variables and configuration
    - [ ] Add database schema diagram (optional)
    - [ ] Document how to use `uv` and `nix` for setup and development

10. **(Optional) Deployment**
    - [ ] Create Dockerfile for the app
    - [ ] Set up docker-compose for local dev
    - [ ] Add production settings (gunicorn, etc.)
    - [ ] Set up CI/CD pipeline (optional)
    - [ ] Deploy to cloud provider (optional)

---

...existing code...
