package rip.jade.lists.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.web.servlet.MockMvc;

import rip.jade.lists.dto.auth.AuthResponse;
import rip.jade.lists.dto.user.UserResponse;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(AuthController.class)
@AutoConfigureMockMvc(addFilters = false)
class AuthControllerTest {

        @Autowired
        private MockMvc mockMvc;

        @MockitoBean
        private rip.jade.lists.service.UserService userService;
        @MockitoBean
        private rip.jade.lists.service.AuthSerivce authSerivce;
        @MockitoBean
        private rip.jade.lists.util.JwtUtil jwtUtil;
        @MockitoBean
        private rip.jade.lists.repository.UserRepository userRepository;

        @Test
        void testAuthControllerTestEndpoint() throws Exception {
                mockMvc.perform(get("/auth/test"))
                                .andExpect(status().isOk())
                                .andExpect(content().json("{}"));
        }

        @Test
        void testRegister() throws Exception {
                String json = "{" +
                                "\"username\": \"testuser\"," +
                                "\"email\": \"testuser@email.com\"," +
                                "\"password\": \"Password1!\"}";

                // Mock the service to return a UserResponse
                UserResponse mockResponse = new UserResponse();
                mockResponse.setId(java.util.UUID.randomUUID());
                mockResponse.setUsername("testuser");
                mockResponse.setEmail("testuser@email.com");
                org.mockito.Mockito.when(userService.registerUser(org.mockito.Mockito.any())).thenReturn(mockResponse);

                mockMvc.perform(post("/auth/register")
                                .contentType("application/json")
                                .content(json))
                                .andExpect(status().isOk())
                                .andExpect(jsonPath("$.username").value("testuser"))
                                .andExpect(jsonPath("$.email").value("testuser@email.com"))
                                .andExpect(jsonPath("$.id").exists());
        }

        @Test
        void testLogin() throws Exception {
                String json = "{" +
                                "\"username\": \"testuser\"," +
                                "\"password\": \"Password1!\"}";
                AuthResponse mockAuthResponse = new AuthResponse();
                mockAuthResponse.setToken("mock-token");
                mockAuthResponse.setUsername("testuser");
                mockAuthResponse.setEmail("testuser@email.com");
                org.mockito.Mockito.when(authSerivce.authenticateUser(org.mockito.Mockito.any()))
                                .thenReturn(mockAuthResponse);

                mockMvc.perform(post("/auth/login")
                                .contentType("application/json")
                                .content(json))
                                .andExpect(status().isOk())
                                .andExpect(jsonPath("$.token").value("mock-token"))
                                .andExpect(jsonPath("$.username").value("testuser"))
                                .andExpect(jsonPath("$.email").value("testuser@email.com"));
        }

        @Test
        void testLogout() throws Exception {
                org.mockito.Mockito.doNothing().when(authSerivce).logoutUser(org.mockito.Mockito.anyString());
                String token = "mock-token";
                mockMvc.perform(post("/auth/logout")
                                .header("Authorization", "Bearer " + token))
                                .andExpect(status().isOk())
                                .andExpect(content().string("User logged out!"));
        }
}
