#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "shader.h"

/* Globals */
unsigned int vao;
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

    unsigned int vbo;
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
 * The main rendering loop.
 * 
 * @param window The GLFW window to render to.
 */
void main_loop(GLFWwindow* window) {
    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        render_triangle();

        glfwSwapBuffers(window);
        glfwPollEvents();
    }
}

void initialize_renderer() {
    // Setup shaders and data
    shader_program = create_shader_program();
    setup_data();
}
