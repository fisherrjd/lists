package rip.jade.lists.dto.user;

import lombok.Data;

@Data
public class UserUpdateRequest {
    private String username;
    private String email;
    private String password; // Optional: only if user wants to update password
    // Add other fields as needed (e.g., profile info)
}
