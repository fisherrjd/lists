package rip.jade.lists.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/lists")
public class ListController {

    @PostMapping
    public void createList() {
    }

    @GetMapping()
    public void getUsersLists() {
    }

    @GetMapping("/{listId}")
    public void getList(@PathVariable String listId) {
    }

    @PostMapping("/{listId}")
    public void updateList(@PathVariable String listId) {
    }

    @DeleteMapping("/{listId}")
    public void deleteList(@PathVariable String listId) {
    }

}