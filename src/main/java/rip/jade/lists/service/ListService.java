package rip.jade.lists.service;

import java.util.UUID;

import org.springframework.stereotype.Service;

import rip.jade.lists.dto.auth.RegisterRequest;
import rip.jade.lists.dto.list.CreateListRequest;
import rip.jade.lists.dto.list.ListResponse;
import rip.jade.lists.dto.user.UserResponse;
import rip.jade.lists.model.TaskList;
import rip.jade.lists.model.User;
import rip.jade.lists.repository.ListRepository;

@Service
public class ListService {

    private final ListRepository listRepository;

    ListService(ListRepository listRepository) {
        this.listRepository = listRepository;
    }

    public ListResponse createList(CreateListRequest request) {
        validateListRequest(request);
        TaskList taskList = createTaskListFromRequest(request);
        ListResponse response = mapToListResponse(taskList);
        listRepository.save(taskList);
        return response;
    }

    // TODO: Move validation to annotations and use @Valid in controller
    private void validateListRequest(CreateListRequest request) {
        if (request.getName() == null || request.getName().trim().isEmpty()) {
            throw new IllegalArgumentException("List name is required");
        }
        if (request.getName().length() > 100) {
            throw new IllegalArgumentException("List name must be 100 characters or fewer");
        }
        if (request.getDescription() != null && request.getDescription().length() > 500) {
            throw new IllegalArgumentException("Description must be 500 characters or fewer");
        }
    }

    public TaskList createTaskListFromRequest(CreateListRequest request) {
        TaskList taskList = new TaskList();
        taskList.setName(request.getName());
        taskList.setDescription(request.getDescription());
        taskList.setId(UUID.randomUUID());
        return taskList;
    }

    // Possibly move to mapper class depending on needs
    // TODO look into using an object mapper
    private ListResponse mapToListResponse(TaskList taskList) {
        ListResponse response = new ListResponse();
        response.setId(taskList.getId());
        response.setName(taskList.getName());
        response.setDescription(taskList.getDescription());
        return response;

    }
}
