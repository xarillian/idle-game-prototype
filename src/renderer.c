#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "shader.h"
#include "villager.h"

/* Globals */
unsigned int vao, vbo;
unsigned int shader_program;

/**
 * Sets up the vertex data and buffers.
 */
void setup_data() {
    float vertices[] = {
        // For visualization: each row is a vertex.
        // Each vertex has position [x, y, z] and color [r, g, b]
        -0.5f, -0.5f, 0.0f, 1.0, 0.0, 0.0,   // red color for this vertex
         0.5f, -0.5f, 0.0f, 0.0, 1.0, 0.0,   // green color
         0.0f,  0.5f, 0.0f, 0.0, 0.0, 1.0    // blue color for our top vertex
    };

    glGenVertexArrays(1, &vao);
    glBindVertexArray(vao);

    glGenBuffers(1, &vbo);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*) 0);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);
}

/**
 * Renders the triangle.
 */
void render_triangle() {
    glUseProgram(shader_program);
    glBindVertexArray(vao);
    glDrawArrays(GL_TRIANGLES, 0, 3);
}

/**
 * Renders the villagers as dots.
 */
void render_villagers(Villager* villagers, int count) {
    float vertices[6 * count]; // 2 coordinates per villager, 3 components (x, y, z)
    
    for (int i = 0; i < count; ++i) {
        vertices[6 * i]     = villagers[i].x / (SCREEN_WIDTH / 2) - 1.0f;
        vertices[6 * i + 1] = villagers[i].y / (SCREEN_HEIGHT / 2) - 1.0f;
        vertices[6 * i + 2] = 0.0f; // z coordinate
        vertices[6 * i + 3] = 1.0f; // r
        vertices[6 * i + 4] = 1.0f; // g
        vertices[6 * i + 5] = 1.0f; // b
    }

    glBindVertexArray(vao);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_DYNAMIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);

    glUseProgram(shader_program);
    glDrawArrays(GL_POINTS, 0, count);
}

void initialize_renderer() {
    // Setup shaders and data
    shader_program = create_shader_program();
    setup_data();
}
