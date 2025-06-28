package rip.jade.lists.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import jakarta.validation.Valid;
import rip.jade.lists.dto.RegisterRequest;
import rip.jade.lists.service.UserService;

@RestController
@RequestMapping("/auth")
public class AuthController {

    private final UserService userService;

    public AuthController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/test")
    public String test() {
        return "AuthController is working!";
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@Valid @RequestBody RegisterRequest request) {
        userService.registerUser(request);
        return ResponseEntity.ok("User registered!");
    }

    @PostMapping("/login")
    public String login() {
        // Registration logic goes here
        return "User registered!";
    }

    @PostMapping("/logout")
    public String logout() {
        // Registration logic goes here
        return "User registered!";
    }
}