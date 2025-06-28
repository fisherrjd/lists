package rip.jade.lists.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import jakarta.validation.Valid;
import rip.jade.lists.dto.AuthResponse;
import rip.jade.lists.dto.RegisterRequest;
import rip.jade.lists.dto.LoginRequest;
import rip.jade.lists.dto.UserResponse;
import rip.jade.lists.dto.ErrorResponse;
import rip.jade.lists.service.AuthSerivce;
import rip.jade.lists.service.UserService;

@RestController
@RequestMapping("/auth")
public class AuthController {

    private final UserService userService;
    private final AuthSerivce authSerivce;

    public AuthController(UserService userService, AuthSerivce authSerivce) {
        this.userService = userService;
        this.authSerivce = authSerivce;
    }

    @GetMapping("/test")
    public String test() {
        return "AuthController is working!";
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@Valid @RequestBody RegisterRequest request) {
        try {
            UserResponse userResponse = userService.registerUser(request);
            return ResponseEntity.ok(userResponse);
        } catch (Exception e) {
            ErrorResponse error = new ErrorResponse(e.getMessage(), "REGISTER_ERROR");
            return ResponseEntity.badRequest().body(error);
        }
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@Valid @RequestBody LoginRequest request) {
        try {
            AuthResponse response = authSerivce.authenticateUser(request);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            ErrorResponse error = new ErrorResponse(e.getMessage(), "LOGIN_ERROR");
            return ResponseEntity.badRequest().body(error);
        }
    }

    @PostMapping("/logout")
    public ResponseEntity<?> logout(@RequestHeader("Authorization") String authHeader) {
        try {
            String token = authHeader.replace("Bearer ", "");
            authSerivce.logoutUser(token);
            return ResponseEntity.ok("User logged out!");
        } catch (Exception e) {
            ErrorResponse error = new ErrorResponse(e.getMessage(), "LOGOUT_ERROR");
            return ResponseEntity.badRequest().body(error);
        }
    }
}