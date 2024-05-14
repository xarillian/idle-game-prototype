#ifndef INIT_H
#define INIT_H

#include <GLFW/glfw3.h>

GLFWwindow* initialize(int width, int height, const char* title);
void cleanup();

#endif
