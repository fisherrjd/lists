package rip.jade.lists.service;

import java.util.ArrayList;
import java.util.UUID;

import org.springframework.stereotype.Service;

import rip.jade.lists.dto.list.CreateListRequest;
import rip.jade.lists.dto.list.ListResponse;
import rip.jade.lists.model.TaskList;
import rip.jade.lists.repository.ListRepository;
import rip.jade.lists.exception.ResourceNotFoundException;

@Service
public class ListService {

    private final ListRepository listRepository;

    ListService(ListRepository listRepository) {
        this.listRepository = listRepository;
    }

    public ListResponse createList(CreateListRequest request) {
        TaskList taskList = createTaskListFromRequest(request);
        ListResponse response = mapToListResponse(taskList);
        listRepository.save(taskList);
        return response;
    }

    // Possibly move to mapper class depending on needs
    // TODO look into using an object mapper
    public TaskList createTaskListFromRequest(CreateListRequest request) {
        TaskList taskList = new TaskList();
        taskList.setName(request.getName());
        taskList.setDescription(request.getDescription());
        taskList.setId(UUID.randomUUID());
        taskList.setAuthorizedUsers(new ArrayList<>()); // Initialize the list of authorized users
        // Assuming 'ownerUser' is available in the context, otherwise, it should be
        // passed as a parameter
        // taskList.getAuthorizedUsers().add(ownerUser); // Add the owner as authorized
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

    public ListResponse getlist(String listId) {
        TaskList taskList = listRepository.findById(UUID.fromString(listId))
                .orElseThrow(() -> new ResourceNotFoundException("List not found"));
        return mapToListResponse(taskList);
    }
}
