package rip.jade.lists.service;

import java.util.UUID;

import org.springframework.stereotype.Service;

import rip.jade.lists.dto.LoginRequest;
import rip.jade.lists.dto.RegisterRequest;
import rip.jade.lists.dto.UserUpdateRequest;

@Service
public class UserService {

    /**
     * Registers a new user.
     * Implementation: Validate input, hash password, save user to DB.
     */
    public void registerUser(RegisterRequest request) {
        // 1. Validate input (e.g., check for null/empty fields, valid email format)
        // 2. Check if username or email already exists in the database
        // 3. Hash the password securely (e.g., using BCrypt)
        // 4. Create a new User entity and set its fields from the request
        // 5. Assign a new UUID as the user's ID (if not auto-generated)
        // 6. Save the new user entity using userRepository.save(user)
        // 7. (Optional) Send a verification email or welcome message
        // 8. (Optional) Handle exceptions and return appropriate responses
    }

    /**
     * Authenticates a user (login).
     * Implementation: Verify credentials, return token/session if valid.
     */
    public void authenticateUser(LoginRequest request) {
        // TODO: Implement authentication logic
    }

    /**
     * Retrieves user details by username or ID.
     * Implementation: Query user repository for user info.
     */
    public void getUserById(UUID id) {
        // TODO: Implement user retrieval logic
    }

    /**
     * Updates user profile information.
     * Implementation: Validate and update user fields in DB.
     */
    public void updateUser(UUID id, UserUpdateRequest user) {
        // TODO: Implement user update logic
    }

    /**
     * Deletes or deactivates a user account.
     * Implementation: Remove or deactivate user in DB.
     */
    public void deleteUser(UUID id) {
        // TODO: Implement user deletion logic
    }

    /**
     * Handles password reset or update.
     * Implementation: Validate, hash new password, update in DB.
     */
    public void resetPassword(String email, String newPassword) {
        // TODO: Implement password reset logic
    }

    /**
     * Logs out a user (if using sessions or tokens).
     * Implementation: Invalidate session or token.
     */
    public void logoutUser(String token) {
        // TODO: Implement logout logic
    }

    /**
     * Assigns roles or permissions to a user.
     * Implementation: Update user roles in DB.
     */
    public void assignRoleToUser(UUID userId, String role) {
        // TODO: Implement role assignment logic
    }

    /**
     * Sends email verification to user (optional).
     * Implementation: Generate token, send email with verification link.
     */
    public void sendEmailVerification(String email) {
        // TODO: Implement email verification logic
    }

    /**
     * Locks or unlocks a user account (optional).
     * Implementation: Update user status in DB.
     */
    public void lockUserAccount(UUID userId) {
        // TODO: Implement account locking logic
    }
}
