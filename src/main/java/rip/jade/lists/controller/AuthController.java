package rip.jade.lists.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @GetMapping("/test")
    public String test() {
        return "AuthController is working!";
    }

    @PostMapping("/register")
    public String register() {
        // Registration logic goes here
        return "User registered!";
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