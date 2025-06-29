package rip.jade.lists.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Entity
@Data
@NoArgsConstructor
@Table(name = "users")
public class User {
    @Id
    private UUID id;
    private String username;
    private String password;
    private String email;

    // GOOGLE ID: google_id VARCHAR(255) UNIQUE NULL, -- For Google OAuth TODO
}
