# Shared Lists API

## Overview

Shared Lists is a collaborative list management RESTful API built with Spring Boot. It enables users to create, manage, and share lists (such as grocery or to-do lists) with others. The API supports secure authentication via email/password and is designed for future integration with Google OAuth for third-party login.

## Features

- **User Registration & Authentication**: Secure registration and login using JWT tokens. Google OAuth login planned.
- **Personal Lists**: Users can create, update, and delete their own lists.
- **List Items**: Add, update, and remove items from lists, including marking items as completed.
- **List Sharing**: Share lists with other users, granting them view or edit access.
- **Collaborative Editing**: Multiple users can collaborate on shared lists in real time.

## API Endpoints

### Authentication

| Method | Path             | Description                                 |
|--------|------------------|---------------------------------------------|
| POST   | /auth/register   | Register a new user                         |
| POST   | /auth/login      | Authenticate and receive a JWT              |
| POST   | /auth/logout     | Invalidate the current user's session/JWT   |

### User Management

| Method | Path      | Description                                 |
|--------|-----------|---------------------------------------------|
| GET    | /users/me | Get the current user's profile               |

### List Management

| Method | Path                | Description                                 |
|--------|---------------------|---------------------------------------------|
| POST   | /lists              | Create a new list                           |
| GET    | /lists              | Get all accessible lists                    |
| GET    | /lists/:listId      | Get details of a specific list              |
| PUT    | /lists/:listId      | Update a list's properties                  |
| DELETE | /lists/:listId      | Delete a list (owner only)                  |

### List Sharing

| Method | Path                          | Description                                 |
|--------|-------------------------------|---------------------------------------------|
| GET    | /lists/:listId/users          | Get users with access to a list             |
| POST   | /lists/:listId/users          | Share a list with another user              |
| DELETE | /lists/:listId/users/:userId  | Remove a user's access to a list            |

### List Items

| Method | Path                                 | Description                                 |
|--------|--------------------------------------|---------------------------------------------|
| POST   | /lists/:listId/items                 | Add an item to a list                       |
| PUT    | /lists/:listId/items/:itemId         | Update an item's properties                 |
| DELETE | /lists/:listId/items/:itemId         | Delete an item from a list                  |

## Database Structure

The application uses a relational database with the following tables:

- **users**: Stores user accounts, including support for Google OAuth (`google_id` column).
- **lists**: Stores lists and their owners.
- **list_items**: Stores items within each list.
- **list_users**: Junction table for many-to-many user-list sharing.

## Google OAuth Integration (Planned)

- `GET /auth/google`: Redirects to Google for OAuth login.
- `GET /auth/google/callback`: Handles Google callback, logs in or registers the user.
- The `users` table includes a `google_id` column for this purpose.

## Technology Stack

- Java 21
- Spring Boot 3.x
- JWT for authentication
- Maven for build management
- Nix for development environment
- (Planned) Google OAuth2 integration

## Getting Started

1. **Clone the repository**
2. **Set up the environment** (Nix or install Java 21 & Maven)
3. **Run the backend**:

   ```bash
   ./mvnw spring-boot:run
   ```

4. **API Documentation**: See this README and `/TODO.md` for endpoint details.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements.

## License

This project is licensed under the MIT License.
