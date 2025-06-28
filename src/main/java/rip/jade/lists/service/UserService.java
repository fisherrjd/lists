package rip.jade.lists.service;

import java.util.UUID;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import rip.jade.lists.dto.LoginRequest;
import rip.jade.lists.dto.RegisterRequest;
import rip.jade.lists.dto.UserUpdateRequest;
import rip.jade.lists.model.User;
import rip.jade.lists.repository.UserRepository;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    /**
     * Registers a new user.
     * Implementation: Validate input, hash password, save user to DB.
     */
    public void registerUser(RegisterRequest request) {

        if (userRepository.findByUsername(request.getUsername()) != null) {
            throw new IllegalArgumentException("Username already exists");
        }
        if (userRepository.findByEmail(request.getEmail()) != null) {
            throw new IllegalArgumentException("Email already exists");
        }

        String hashedPassword = passwordEncoder.encode(request.getPassword());

        User user = new User();
        user.setEmail(request.getEmail());
        user.setUsername(request.getUsername());
        user.setPassword(hashedPassword);
        user.setId(UUID.randomUUID());
        userRepository.save(user);

        // 7. (TODO) Send a verification email or welcome message
        // 8. (TODO) Handle exceptions and return appropriate responses
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
