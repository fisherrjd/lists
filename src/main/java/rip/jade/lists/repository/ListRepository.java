package rip.jade.lists.repository;

import java.util.UUID;
import org.springframework.data.jpa.repository.JpaRepository;
import rip.jade.lists.model.User;

public interface ListRepository extends JpaRepository<User, UUID> {
    User findByUsername(String username);

    User findByEmail(String email);
}
