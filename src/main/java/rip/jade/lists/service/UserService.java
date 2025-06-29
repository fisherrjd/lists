package rip.jade.lists.service;

import java.util.UUID;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import rip.jade.lists.dto.auth.RegisterRequest;
import rip.jade.lists.dto.user.UserResponse;
import rip.jade.lists.dto.user.UserUpdateRequest;
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
    public UserResponse registerUser(RegisterRequest request) {
        validateRegisterRequest(request);
        User user = createUserFromRequest(request);
        userRepository.save(user);
        return mapToUserResponse(user);
    }

    private void validateRegisterRequest(RegisterRequest request) {
        if (userRepository.findByUsername(request.getUsername()) != null) {
            throw new IllegalArgumentException("Username already exists");
        }
        if (userRepository.findByEmail(request.getEmail()) != null) {
            throw new IllegalArgumentException("Email already exists");
        }
    }

    private User createUserFromRequest(RegisterRequest request) {
        User user = new User();
        user.setEmail(request.getEmail());
        user.setUsername(request.getUsername());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setId(UUID.randomUUID());
        return user;
    }

    // Possibly move to mapper class depending on needs
    // TODO look into using an object mapper
    private UserResponse mapToUserResponse(User user) {
        UserResponse response = new UserResponse();
        response.setId(user.getId());
        response.setUsername(user.getUsername());
        response.setEmail(user.getEmail());
        return response;

        // 7. (TODO) Send a verification email or welcome message
        // 8. (TODO) Handle exceptions
    }

    /**
     * Retrieves user details by username or ID.
     * Implementation: Query user repository for user info.
     * Should stay in UserService
     */
    public void getUserById(UUID id) {
        // TODO: Implement user retrieval logic
    }

    /**
     * Updates user profile information.
     * Implementation: Validate and update user fields in DB.
     * Should stay in UserService
     */
    public void updateUser(UUID id, UserUpdateRequest user) {
        // TODO: Implement user update logic
    }

    /**
     * Deletes or deactivates a user account.
     * Implementation: Remove or deactivate user in DB.
     * Should stay in UserService
     */
    public void deleteUser(UUID id) {
        // TODO: Implement user deletion logic
    }

    /**
     * Assigns roles or permissions to a user.
     * Implementation: Update user roles in DB.
     * Should move to RoleService or UserRoleService
     */
    public void assignRoleToUser(UUID userId, String role) {
        // TODO: Implement role assignment logic
    }

    /**
     * Sends email verification to user (optional).
     * Implementation: Generate token, send email with verification link.
     * Should move to EmailService
     */
    public void sendEmailVerification(String email) {
        // TODO: Implement email verification logic
    }

    /**
     * Locks or unlocks a user account (optional).
     * Implementation: Update user status in DB.
     * Should move to AccountService
     */
    public void lockUserAccount(UUID userId) {
        // TODO: Implement account locking logic
    }
}
