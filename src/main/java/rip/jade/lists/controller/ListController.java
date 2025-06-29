package rip.jade.lists.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import rip.jade.lists.dto.list.CreateListRequest;
import rip.jade.lists.dto.list.ListResponse;
import rip.jade.lists.model.TaskList;
import rip.jade.lists.service.AuthSerivce;
import rip.jade.lists.service.ListService;
import rip.jade.lists.service.UserService;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/lists")
public class ListController {

    private final ListService listService;

    public ListController(ListService listService) {
        this.listService = listService;
    }

    @PostMapping
    public ListResponse createList(CreateListRequest request) {
        ListResponse response = listService.createList(request);
        return response;
    }

    @GetMapping()
    public ResponseEntity<?> getUsersLists() {
        return ResponseEntity.ok().body("100 WIP");

    }

    @GetMapping("/{listId}")
    public ResponseEntity<?> getList(@PathVariable String listId) {
        return ResponseEntity.ok().body("101 ListId: " + listId);

    }

    @PutMapping("/{listId}")
    public ResponseEntity<?> updateList(@PathVariable String listId) {
        return ResponseEntity.ok().body("102 ListId: " + listId);

    }

    @DeleteMapping("/{listId}")
    public ResponseEntity<?> deleteList(@PathVariable String listId) {
        return ResponseEntity.ok().body("103 ListId: " + listId);

    }

}