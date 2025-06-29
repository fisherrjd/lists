package rip.jade.lists.repository;

import java.util.Optional;
import java.util.UUID;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import rip.jade.lists.model.TaskList;

public interface ListRepository extends JpaRepository<TaskList, UUID> {
    @Query("SELECT t FROM TaskList t LEFT JOIN FETCH t.authorizedUsers WHERE t.id = :id")
    Optional<TaskList> findByIdWithAuthorizedUsers(@Param("id") UUID id);
}
