package rip.jade.lists.dto.list;

import java.util.UUID;

import lombok.Data;

@Data
public class ListResponse {
    private UUID id;
    private String name;
    private String description;
}
