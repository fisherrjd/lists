package rip.jade.lists.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import rip.jade.lists.dto.list.CreateListRequest;
import rip.jade.lists.dto.list.ListResponse;
import rip.jade.lists.model.TaskList;
import rip.jade.lists.model.User;
import rip.jade.lists.service.AuthSerivce;
import rip.jade.lists.service.ListService;
import rip.jade.lists.service.UserService;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import jakarta.validation.Valid;
import java.security.Principal;

import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;

@RestController
@RequestMapping("/lists")
public class ListController {

    private final ListService listService;
    private final UserService userService;

    public ListController(ListService listService, UserService userService) {
        this.listService = listService;
        this.userService = userService;
    }

    @PostMapping
    public ResponseEntity<?> createList(@Valid @RequestBody CreateListRequest request, Principal principal) {
        String username = extractUsername(principal);
        User ownerUser = userService.findByUsername(username);
        ListResponse response = listService.createList(request, ownerUser);
        return ResponseEntity.ok().body(response);
    }

    private String extractUsername(Principal principal) {
        if (principal instanceof UsernamePasswordAuthenticationToken token) {
            Object innerPrincipal = token.getPrincipal();
            if (innerPrincipal instanceof User user) {
                return user.getUsername();
            } else {
                return String.valueOf(innerPrincipal);
            }
        }
        return principal.getName();
    }

    @GetMapping()
    public ResponseEntity<?> getUsersLists(Principal principal) {
        String username = extractUsername(principal);
        User user = userService.findByUsername(username);
        // Fetch user with authorizedLists eagerly loaded
        java.util.Optional<User> userWithListsOpt = userService.getUserRepository()
                .findByIdWithAuthorizedLists(user.getId());
        if (userWithListsOpt.isEmpty()) {
            return ResponseEntity.status(404).body("User not found");
        }
        User userWithLists = userWithListsOpt.get();
        java.util.List<TaskList> lists = listService.getListsForUser(userWithLists);
        java.util.List<ListResponse> responses = lists.stream()
                .map(listService::mapToListResponse)
                .toList();
        return ResponseEntity.ok().body(responses);
    }

    @GetMapping("/{listId}")
    public ResponseEntity<?> getList(@PathVariable String listId, Principal principal) {
        String username = extractUsername(principal);
        User user = userService.findByUsername(username);
        TaskList list = listService.getListIfUserHasAccess(listId, user);
        if (list == null) {
            return ResponseEntity.status(403).body("Forbidden: You do not have access to this list");
        }
        ListResponse response = listService.mapToListResponse(list);
        return ResponseEntity.ok().body(response);
    }

    @PutMapping("/{listId}")
    public ResponseEntity<?> updateList(@PathVariable String listId,
            @Valid @RequestBody rip.jade.lists.dto.list.UpdateListRequest request, Principal principal) {
        String username = extractUsername(principal);
        User user = userService.findByUsername(username);
        try {
            ListResponse response = listService.updateList(listId, user, request);
            return ResponseEntity.ok().body(response);
        } catch (rip.jade.lists.exception.ResourceNotFoundException e) {
            return ResponseEntity.status(403).body("Forbidden: You do not have access to this list");
        }
    }

    @DeleteMapping("/{listId}")
    public ResponseEntity<?> deleteList(@PathVariable String listId) {
        listService.deleteList(listId);
        return ResponseEntity.ok().body("List deleted successfully");
    }

}