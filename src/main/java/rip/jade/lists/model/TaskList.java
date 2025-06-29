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
@Table(name = "taskLists")
public class TaskList {
    @Id
    private UUID id;
    private String name;
    private String description;
    // TODO: Add a collection of authorized users (e.g., List<User> authorizedUsers)
    // GOOGLE ID: google_id VARCHAR(255) UNIQUE NULL, -- For Google OAuth TODO
}