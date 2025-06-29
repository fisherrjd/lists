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
    public ListResponse createList(@Valid @RequestBody CreateListRequest request, Principal principal) {
        String username = extractUsername(principal);
        User ownerUser = userService.findByUsername(username);
        ListResponse response = listService.createList(request, ownerUser);
        return response;
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
    public ResponseEntity<?> getUsersLists() {
        return ResponseEntity.ok().body("100 WIP");

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
    public ResponseEntity<?> updateList(@PathVariable String listId) {
        return ResponseEntity.ok().body("102 ListId: " + listId);

    }

    @DeleteMapping("/{listId}")
    public ResponseEntity<?> deleteList(@PathVariable String listId) {
        listService.deleteList(listId);
        return ResponseEntity.ok().body("List deleted successfully");
    }

}