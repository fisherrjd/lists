package rip.jade.lists.dto;

import lombok.Data;
import java.util.UUID;

@Data
public class UserResponse {
    private UUID id;
    private String username;
    private String email;
    // Add other non-sensitive fields as needed
}
