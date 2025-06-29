package rip.jade.lists.repository;

import java.util.Optional;
import java.util.UUID;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import rip.jade.lists.model.User;

public interface UserRepository extends JpaRepository<User, UUID> {
    User findByUsername(String username);

    User findByEmail(String email);

    @Query("SELECT u FROM User u LEFT JOIN FETCH u.authorizedLists WHERE u.id = :id")
    Optional<User> findByIdWithAuthorizedLists(@Param("id") UUID id);
}
