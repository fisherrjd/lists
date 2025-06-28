package rip.jade.lists.service;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import rip.jade.lists.dto.AuthResponse;
import rip.jade.lists.dto.LoginRequest;
import rip.jade.lists.dto.RegisterRequest;
import rip.jade.lists.repository.UserRepository;
import rip.jade.lists.dto.UserResponse;
import rip.jade.lists.dto.UserUpdateRequest;
import rip.jade.lists.model.User;
import rip.jade.lists.util.JwtUtil;
import rip.jade.lists.repository.BlacklistedTokenRepository;
import rip.jade.lists.model.BlacklistedToken;
import java.util.Date;

@Service
public class AuthSerivce {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;
    private final BlacklistedTokenRepository blacklistedTokenRepository;

    public AuthSerivce(UserRepository userRepository, PasswordEncoder passwordEncoder, JwtUtil jwtUtil,
            BlacklistedTokenRepository blacklistedTokenRepository) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtUtil = jwtUtil;
        this.blacklistedTokenRepository = blacklistedTokenRepository;
    }

    /**
     * Authenticates a user (login).
     * Steps:
     * 5. (Optional) Check if user is locked/disabled.
     * 7. (Optional) Log login event.
     */
    public AuthResponse authenticateUser(LoginRequest request) {
        User user = userRepository.findByUsername(request.getUsername());
        if (user == null) {
            throw new IllegalArgumentException("Invalid username or password");
        }
        if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            throw new IllegalArgumentException("Invalid username or password");
        }
        String token = jwtUtil.generateToken(user.getUsername());
        return new AuthResponse(token, user.getUsername(), user.getEmail());
    }

    /**
     * Logs out a user (if using sessions or tokens).
     * Steps:
     * 1. Invalidate session or token (remove from store or add to blacklist).
     * 2. (Optional) Log logout event.
     * * 3. (Optional) Clean up any user-specific resources.
     */
    public void logoutUser(String token) {
        // Add the token to the blacklist with its expiry date
        Date expiry = jwtUtil.extractAllClaims(token).getExpiration();
        BlacklistedToken blacklistedToken = new BlacklistedToken(token, expiry);
        blacklistedTokenRepository.save(blacklistedToken);
    }

    public boolean isTokenBlacklisted(String token) {
        return blacklistedTokenRepository.existsByToken(token);
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
