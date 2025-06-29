package rip.jade.lists.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/lists")
public class ListController {

    @PostMapping
    public ResponseEntity<?> createList() {
        return ResponseEntity.ok().body("100 WIP");
    }

    @GetMapping()
    public ResponseEntity<?> getUsersLists() {
        return ResponseEntity.ok().body("100 WIP");

    }

    @GetMapping("/{listId}")
    public ResponseEntity<?> getList(@PathVariable String listId) {
        return ResponseEntity.ok().body("101 ListId: " + listId);

    }

    @PostMapping("/{listId}")
    public ResponseEntity<?> updateList(@PathVariable String listId) {
        return ResponseEntity.ok().body("102 ListId: " + listId);

    }

    @DeleteMapping("/{listId}")
    public ResponseEntity<?> deleteList(@PathVariable String listId) {
        return ResponseEntity.ok().body("103 ListId: " + listId);

    }

}