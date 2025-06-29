package rip.jade.lists.service;

import java.util.ArrayList;
import java.util.UUID;

import org.springframework.stereotype.Service;

import rip.jade.lists.dto.list.CreateListRequest;
import rip.jade.lists.dto.list.ListResponse;
import rip.jade.lists.model.TaskList;
import rip.jade.lists.repository.ListRepository;
import rip.jade.lists.exception.ResourceNotFoundException;
import rip.jade.lists.model.User;
import rip.jade.lists.repository.UserRepository;

@Service
public class ListService {

    private final ListRepository listRepository;
    private final UserRepository userRepository;

    public ListService(ListRepository listRepository, UserRepository userRepository) {
        this.listRepository = listRepository;
        this.userRepository = userRepository;
    }

    public ListResponse createList(CreateListRequest request, User ownerUser) {
        TaskList taskList = createTaskListFromRequest(request, ownerUser);
        ListResponse response = mapToListResponse(taskList);
        listRepository.save(taskList);
        return response;
    }

    // Possibly move to mapper class depending on needs
    // TODO look into using an object mapper
    public TaskList createTaskListFromRequest(CreateListRequest request, User ownerUser) {
        TaskList taskList = new TaskList();
        taskList.setName(request.getName());
        taskList.setDescription(request.getDescription());
        taskList.setId(UUID.randomUUID());
        taskList.setAuthorizedUsers(new ArrayList<>()); // Initialize the list of authorized users
        taskList.getAuthorizedUsers().add(ownerUser); // Add the owner as authorized
        return taskList;
    }

    // Possibly move to mapper class depending on needs
    // TODO look into using an object mapper
    public ListResponse mapToListResponse(TaskList taskList) {
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

    public void deleteList(String listId) {
        TaskList taskList = listRepository.findByIdWithAuthorizedUsers(UUID.fromString(listId))
                .orElseThrow(() -> new ResourceNotFoundException("List not found"));
        // Remove this list from each user's authorizedLists
        if (taskList.getAuthorizedUsers() != null) {
            for (User user : taskList.getAuthorizedUsers()) {
                // Fetch user with authorizedLists initialized
                User managedUser = userRepository.findByIdWithAuthorizedLists(user.getId())
                        .orElse(user);
                if (managedUser.getAuthorizedLists() != null) {
                    managedUser.getAuthorizedLists().remove(taskList);
                }
            }
            // Remove all users from the list
            taskList.getAuthorizedUsers().clear();
        }
        listRepository.delete(taskList);
    }

    public ListResponse getList(String listId) {
        return null;
    }

    public TaskList getListIfUserHasAccess(String listId, User user) {
        TaskList taskList = listRepository.findByIdWithAuthorizedUsers(UUID.fromString(listId))
                .orElse(null);
        if (taskList == null) {
            return null;
        }
        if (taskList.getAuthorizedUsers() != null && taskList.getAuthorizedUsers().stream()
                .anyMatch(u -> u.getId().equals(user.getId()))) {
            return taskList;
        }
        return null;
    }
}
