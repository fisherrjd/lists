package rip.jade.lists.service;

import rip.jade.lists.dto.LoginRequest;

public class AuthSerivce {

    /**
     * Authenticates a user (login).
     * Steps:
     * 1. Retrieve user by username/email from DB.
     * 2. If user not found, throw authentication exception.
     * 3. Verify password matches (use password encoder).
     * 4. If password invalid, throw authentication exception.
     * 5. (Optional) Check if user is locked/disabled.
     * 6. Generate and return authentication token/session (JWT or session ID).
     * 7. (Optional) Log login event.
     */
    public void authenticateUser(LoginRequest request) {
        // TODO: Implement authentication logic
    }

    /**
     * Logs out a user (if using sessions or tokens).
     * Steps:
     * 1. Invalidate session or token (remove from store or add to blacklist).
     * 2. (Optional) Log logout event.
     * 3. (Optional) Clean up any user-specific resources.
     */
    public void logoutUser(String token) {
        // TODO: Implement logout logic
    }

    /**
     * Handles password reset or update.
     * Steps:
     * 1. Validate password reset request (token, email, etc.).
     * 2. Retrieve user by email.
     * 3. If user not found, throw exception.
     * 4. Hash new password (use password encoder).
     * 5. Update user's password in DB.
     * 6. (Optional) Invalidate old sessions/tokens.
     * 7. (Optional) Notify user of password change.
     */
    public void resetPassword(String email, String newPassword) {
        // TODO: Implement password reset logic
    }
}
