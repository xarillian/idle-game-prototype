#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>

#include "init.h"
#include "villager.h"
#include "renderer.h"

#define MAX_VILLAGERS 100

const char* WINDOW_TITLE = "OpenGL :)";
int villager_count = 5;
Villager villagers[MAX_VILLAGERS];

int main(void) {
    GLFWwindow* window = initialize(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE);
    if (!window) {
        return -1;
    }

    initialize_renderer();
    initialize_villagers(5);
    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        update_villagers();
        render_villagers(villagers, 5);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    cleanup();
    return 0;
}
