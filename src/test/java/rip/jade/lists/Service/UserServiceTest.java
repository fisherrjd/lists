package rip.jade.lists.Service;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.security.crypto.password.PasswordEncoder;

import rip.jade.lists.dto.RegisterRequest;
import rip.jade.lists.model.User;
import rip.jade.lists.repository.UserRepository;
import rip.jade.lists.service.UserService;

class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    private UserService userService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        // FIX: Pass both mocks to the constructor
        userService = new UserService(userRepository, passwordEncoder);
    }

    @Test
    void registerUser_throwsIfUsernameExists() {
        RegisterRequest req = new RegisterRequest();
        req.setUsername("existing");
        req.setEmail("new@email.com");
        req.setPassword("Password1!");

        when(userRepository.findByUsername("existing")).thenReturn(new User());

        assertThrows(IllegalArgumentException.class, () -> userService.registerUser(req));
    }

    @Test
    void registerUser_throwsIfEmailExists() {
        RegisterRequest req = new RegisterRequest();
        req.setUsername("newuser");
        req.setEmail("existing@email.com");
        req.setPassword("Password1!");

        when(userRepository.findByUsername("newuser")).thenReturn(null);
        when(userRepository.findByEmail("existing@email.com")).thenReturn(new User());

        assertThrows(IllegalArgumentException.class, () -> userService.registerUser(req));
    }

    @Test
    void registerUser_savesUserIfValid() {
        RegisterRequest req = new RegisterRequest();
        req.setUsername("newuser");
        req.setEmail("new@email.com");
        req.setPassword("Password1!");

        when(userRepository.findByUsername("newuser")).thenReturn(null);
        when(userRepository.findByEmail("new@email.com")).thenReturn(null);
        when(passwordEncoder.encode(anyString())).thenReturn("hashed");

        userService.registerUser(req);

        ArgumentCaptor<User> userCaptor = ArgumentCaptor.forClass(User.class);
        verify(userRepository).save(userCaptor.capture());
        User saved = userCaptor.getValue();
        assertEquals("newuser", saved.getUsername());
        assertEquals("new@email.com", saved.getEmail());
        assertEquals("hashed", saved.getPassword());
        assertNotNull(saved.getId());
    }
}