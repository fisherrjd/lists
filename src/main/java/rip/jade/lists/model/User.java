package rip.jade.lists.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;
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

    @ManyToMany(mappedBy = "authorizedUsers")
    private List<TaskList> authorizedLists;
    // GOOGLE ID: google_id VARCHAR(255) UNIQUE NULL, -- For Google OAuth TODO

    @Override
    public String toString() {
        // Avoid accessing lazy collections in toString
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", email='" + email + '\'' +
                '}';
    }
}
