package rip.jade.lists.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import rip.jade.lists.model.BlacklistedToken;

public interface BlacklistedTokenRepository extends JpaRepository<BlacklistedToken, String> {
    boolean existsByToken(String token);
}
