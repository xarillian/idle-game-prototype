#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>

#include "shader.h"

/* Function Declarations */
GLFWwindow* initialize_glfw_and_create_window();
int initialize_glad();
void main_loop(GLFWwindow* window);
void cleanup();
void setup_data();

/* Constants */
const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;
const char* WINDOW_TITLE = "OpenGL :)";

/* Globals */
unsigned vao;
unsigned int shader_program;

int main(void) {
    GLFWwindow* window = initialize_glfw_and_create_window();
    if (!window) {
        return -1;
    }

    if (!initialize_glad()) {
        cleanup();
        return -1;
    }

    shader_program = create_shader_program();
    setup_data();

    main_loop(window);

    return 0;
}

/**
 * Initializes GLFW, creates a window, and sets the OpenGL context.
 * 
 * @return A pointer to the created GLFW window, or NULL if initialization fails.
 */
GLFWwindow* initialize_glfw_and_create_window() {
    if (!glfwInit()) {
        printf("Failed to initialize GLFW\n");
        return NULL;
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(
        SCREEN_WIDTH, 
        SCREEN_HEIGHT, 
        WINDOW_TITLE, 
        NULL, 
        0
    );
    if (!window) {
        printf("Failed to create GLFW window\n");
        cleanup();
    } else {
        glfwMakeContextCurrent(window);
    }

    return window;
}

/**
 * Initializes GLAD to load OpenGL function pointers.
 * 
 * @return 1 if initialization succeeds, 0 otherwise.
 */
int initialize_glad() {
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        printf("Failed to initialize GLAD\n");
        return 0;
    }
    return 1;
}

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
 * The main rendering loop.
 * 
 * @param window The GLFW window to render to.
 */
void main_loop(GLFWwindow* window) {
    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(shader_program);
        glBindVertexArray(vao);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    cleanup();
}

/**
 * Performs cleanup by terminating GLFW.
 */
void cleanup() {
    glfwTerminate();
}
