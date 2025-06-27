package rip.jade.lists.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import rip.jade.lists.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);

    User findByEmail(String email);
}
