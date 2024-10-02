# Import necessary libraries
import glfw
from OpenGL.GL import *
import numpy as np

# STL
import threading
import sys
import os

class GLFWWindow:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.window = None

        # Vertex data for a triangle
        self.vertices = np.array([
            0.0,  0.5, 0.0,  # Top vertex
           -0.5, -0.5, 0.0,  # Bottom left vertex
            0.5, -0.5, 0.0   # Bottom right vertex
        ], dtype='float32')

        # Vertex Array Object and Vertex Buffer Object
        self.VAO = None
        self.VBO = None
        self.shader_program = None

    def Init(self):
        # Initialize the GLFW library
        if not glfw.init():
            return False
        return True

    def CreateWindow(self):
        # Create a windowed mode window and its OpenGL context
        self.window = glfw.create_window(self.width, self.height, self.title, None, None)
        if not self.window:
            glfw.terminate()
            return False
        
        # Make the window's context current
        glfw.make_context_current(self.window)
        # Set the framebuffer size callback
        glfw.set_framebuffer_size_callback(self.window, self.FramebufferSizeCallback)
        return True

    def FramebufferSizeCallback(self, window, width, height):
        glViewport(0, 0, width, height)

    def CompileShader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise RuntimeError(glGetShaderInfoLog(shader).decode())
        return shader

    def CreateShaderProgram(self):
        vertex_shader_source = """
        #version 330 core
        layout(location = 0) in vec3 position;
        void main()
        {
            gl_Position = vec4(position, 1.0);
        }
        """

        fragment_shader_source = """
        #version 330 core
        out vec4 color;
        void main()
        {
            color = vec4(0.3, 0.5, 0.8, 1.0);  // Light blue color
        }
        """

        vertex_shader = self.CompileShader(vertex_shader_source, GL_VERTEX_SHADER)
        fragment_shader = self.CompileShader(fragment_shader_source, GL_FRAGMENT_SHADER)

        self.shader_program = glCreateProgram()
        glAttachShader(self.shader_program, vertex_shader)
        glAttachShader(self.shader_program, fragment_shader)
        glLinkProgram(self.shader_program)

        # Clean up shaders as they're linked into the program now
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def SetupBuffers(self):
        # Generate and bind a Vertex Array Object
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # Generate and bind a Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)

        # Copy the vertex data to the buffer
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Define the vertex attribute
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        # Unbind the VBO and VAO
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def RenderTriangle(self):
        # Use the shader program and bind the VAO
        glUseProgram(self.shader_program)
        glBindVertexArray(self.VAO)

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def OnRender(self):
        # Render here
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Render the triangle
        self.RenderTriangle()

    def CloseWindow(self):
        # Clean up and close the window
        glfw.terminate()

    def Run(self):
        if not self.Init():
            return
        
        if not self.CreateWindow():
            return
        
        # Create shader program and set up buffers
        self.CreateShaderProgram()
        self.SetupBuffers()

        # Main loop
        while not glfw.window_should_close(self.window):
            self.OnRender()
            # Swap front and back buffers
            glfw.swap_buffers(self.window)
            # Poll for and process events
            glfw.poll_events()
        
        self.CloseWindow()