#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>
#include "init.h"

const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;
const char* WINDOW_TITLE = "OpenGL :)";

int main(void) {
    GLFWwindow* window = initialize(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE);
    if (!window) {
        return -1;
    }

    initialize_renderer();
    main_loop(window);

    cleanup();
    return 0;
}
