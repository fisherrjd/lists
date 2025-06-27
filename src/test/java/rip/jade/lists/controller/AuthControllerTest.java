package rip.jade.lists.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(AuthController.class)
@AutoConfigureMockMvc(addFilters = false)
class AuthControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void testAuthControllerTestEndpoint() throws Exception {
        mockMvc.perform(get("/auth/test"))
                .andExpect(status().isOk())
                .andExpect(content().string("AuthController is working!"));
    }

    @Test
    void testRegister() throws Exception {
        mockMvc.perform(post("/auth/register"))
                .andExpect(status().isOk())
                .andExpect(content().string("User registered!"));
    }

    @Test
    void testLogin() throws Exception {
        mockMvc.perform(post("/auth/login"))
                .andExpect(status().isOk())
                .andExpect(content().string("User registered!"));
    }

    @Test
    void testLogout() throws Exception {
        mockMvc.perform(post("/auth/logout"))
                .andExpect(status().isOk())
                .andExpect(content().string("User registered!"));
    }
}
