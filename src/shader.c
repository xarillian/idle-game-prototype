#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stdio.h>

/* Shader Source */
const char* vertex_shader_source =
        "#version 330 core\n"
		"layout (location = 0) in vec3 position;\n"
		"layout (location = 1) in vec3 color;\n"
		"out vec3 vertexColor;\n"
		"void main()\n"
		"{\n"
		"    gl_Position = vec4(position, 1.0);\n"
		"    vertexColor = color;\n"
		"}\n";

const char* fragment_shader_source =
		"#version 330 core\n"
		"out vec4 fragColor;\n"
		"in vec3 vertexColor;\n"
		"void main()\n"
		"{\n"
		"     fragColor = vec4(vertexColor, 1.0f);\n"
		"}\n";


/**
 * Compiles and links the vertex and fragment shaders into a shader program.
 * 
 * @return The ID of the created shader program.
 */
unsigned int create_shader_program() {
    unsigned int vertex_shader, fragment_shader, shader_program;

    // Compile vertex shader
    vertex_shader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertex_shader, 1, &vertex_shader_source, NULL);
    glCompileShader(vertex_shader);

    // Compile fragment shader
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragment_shader, 1, &fragment_shader_source, NULL);
    glCompileShader(fragment_shader);

    // Link shaders
    shader_program = glCreateProgram();
    glAttachShader(shader_program, vertex_shader);
    glAttachShader(shader_program, fragment_shader);
    glLinkProgram(shader_program);

    // Delete shaders after linking
    glDeleteShader(vertex_shader);
    glDeleteShader(fragment_shader);

    return shader_program;
}
