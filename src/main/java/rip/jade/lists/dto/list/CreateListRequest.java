package rip.jade.lists.dto.list;

import lombok.Data;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

@Data
public class CreateListRequest {
    @NotBlank(message = "List name is required")
    @Size(max = 100, message = "List name must be 100 characters or fewer")
    private String name;

    @Size(max = 500, message = "Description must be 500 characters or fewer")
    private String description;
}
