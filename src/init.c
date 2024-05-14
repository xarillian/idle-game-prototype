#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>
#include "init.h"
#include "renderer.h"

/**
 * Initializes GLFW, creates a window, and sets the OpenGL context.
 * 
 * @param width Width of the window.
 * @param height Height of the window.
 * @param title Title of the window.
 * @return A pointer to the created GLFW window, or NULL if initialization 
 *  fails.
 */
GLFWwindow* initialize(int width, int height, const char* title) {
        if (!glfwInit()) {
        printf("Failed to initialize GLFW\n");
        return NULL;
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(width, height, title, NULL, NULL);
    if (!window) {
        printf("Failed to create GLFW window\n");
        glfwTerminate();
        return NULL;
    }

    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        printf("Failed to initialize GLAD\n");
        glfwDestroyWindow(window);
        glfwTerminate();
        return NULL;
    }

    return window;
}

/**
 * Performs cleanup by terminating GLFW.
 */
void cleanup() {
    glfwTerminate();
}

