package rip.jade.lists.model;

import java.util.UUID;

public class User {

    UUID id;
    String username;
    String password; // Handle Hashing?
    String email;

    // GOOGLE ID: google_id VARCHAR(255) UNIQUE NULL, -- For Google OAuth
    // integration
}
