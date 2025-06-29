# Shared Lists API

## Define Goal

The primary goal is to develop a robust RESTful API for a collaborative list management application. This API will enable users to:

* **Create and manage personal lists**: Users can create new lists (e.g., grocery lists, to-do lists).
* **Add and modify list items**: Each list can contain multiple items, each with a name and quantity. Items can be updated (name, quantity, completion status) or removed.
* **Share lists**: Users can share their lists with other authenticated users, granting them view and modification access.
* **Authentication**: Secure user registration and login using traditional email/password and potentially third-party providers like Google.

## Define Endpoints

This section outlines the core API endpoints, their HTTP methods, and expected request/response structures.

### 1. Authentication

| Method | Path                 | Description                               | Request Body (Example)                               |
| :----- | :------------------- | :---------------------------------------- | :--------------------------------------------------- |
| `POST` | `/auth/register`     | Registers a new user account.             | `{ "name": "John Doe", "email": "john@example.com", "password": "securepassword" }` |
| `POST` | `/auth/login`        | Authenticates a user and returns a JWT.   | `{ "email": "john@example.com", "password": "securepassword" }` |
| `POST` | `/auth/logout`       | Invalidates the current user's session/JWT (if applicable). | (None)                                               |

### 2. User Management

| Method | Path                 | Description                               |
| :----- | :------------------- | :---------------------------------------- |
| `GET`  | `/users/me`          | Retrieves the profile of the currently authenticated user. |

### 3. List Management

| Method | Path                 | Description                               | Request Body (Example)                               |
| :----- | :------------------- | :---------------------------------------- | :--------------------------------------------------- |
| `POST` | `/lists`             | Creates a new list.                       | `{ "name": "My new grocery list" }`                  |
| `GET`  | `/lists`             | Retrieves all lists the authenticated user has access to (owned or shared). | (None)                                               |
| `GET`  | `/lists/:listId`     | Retrieves details of a specific list, including all its items. | (None)                                               |
| `PUT`  | `/lists/:listId`     | Updates properties of an existing list (e.g., name). | `{ "name": "Updated List Name" }`                    |
| `DELETE` | `/lists/:listId`   | Deletes a list. Only the owner can delete a list. | (None)                                               |

### 4. List Sharing

| Method | Path                 | Description                               | Request Body (Example)                               |
| :----- | :------------------- | :---------------------------------------- | :--------------------------------------------------- |
| `GET`  | `/lists/:listId/users` | Retrieves all users who have access to a specific list. | (None)                                               |
| `POST` | `/lists/:listId/users` | Shares a list with another user. The user can be identified by email or ID. | `{ "email": "collaborator@example.com" }` or `{ "userId": "some-uuid" }` |
| `DELETE` | `/lists/:listId/users/:userId` | Removes a user's access to a specific list. | (None)                                               |

### 5. List Items

| Method | Path                 | Description                               | Request Body (Example)                               |
| :----- | :------------------- | :---------------------------------------- | :--------------------------------------------------- |
| `POST` | `/lists/:listId/items` | Adds a new item to a specific list.       | `{ "name": "Apples", "quantity": 5 }`                |
| `PUT`  | `/lists/:listId/items/:itemId` | Updates an item's properties (name, quantity, completed status). | `{ "name": "Green Apples", "quantity": 3, "completed": true }` |
| `DELETE` | `/lists/:listId/items/:itemId` | Deletes an item from a specific list. | (None)                                               |

## Define DB Structure

The application will utilize a relational database with the following four tables to manage users, lists, items, and sharing relationships.

### `users`

Stores user account information, including authentication credentials.

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    google_id VARCHAR(255) UNIQUE NULL, -- For Google OAuth integration
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### `lists`

Stores the lists themselves.

```sql
CREATE TABLE lists (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    owner_id UUID NOT NULL REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### `list_items`

Stores the items within each list.

```sql
CREATE TABLE list_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    list_id UUID NOT NULL REFERENCES lists(id),
    name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### `list_users` (Junction Table)

Manages the many-to-many relationship between users and lists.

```sql
CREATE TABLE list_users (
    user_id UUID NOT NULL REFERENCES users(id),
    list_id UUID NOT NULL REFERENCES lists(id),
    PRIMARY KEY (user_id, list_id)
);
```

## Google Auth

This will be integrated into the `/auth` endpoints, likely with:

* `GET /auth/google` - Redirect to Google for OAuth.
* `GET /auth/google/callback` - Handle the callback from Google to log in or register the user.

The `users` table will need a `google_id` column to support this.
