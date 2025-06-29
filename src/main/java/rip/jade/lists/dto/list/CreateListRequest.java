package rip.jade.lists.dto.list;

import lombok.Data;

@Data
public class CreateListRequest {
    private String name;
    private String description;
}
