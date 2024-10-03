# Import necessary libraries
import glfw
from OpenGL.GL import *
import numpy as np

# STL
import threading
import sys
import os

# Shader class to handle shader compilation and linking
class Shader:
    def __init__(self, vertex_source, fragment_source):
        self.m_ShaderProgram = None
        self.CompileShaders(vertex_source, fragment_source)

    def CompileShader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise RuntimeError(glGetShaderInfoLog(shader).decode())
        return shader

    def CompileShaders(self, vertex_source, fragment_source):
        vertex_shader = self.CompileShader(vertex_source, GL_VERTEX_SHADER)
        fragment_shader = self.CompileShader(fragment_source, GL_FRAGMENT_SHADER)

        self.m_ShaderProgram = glCreateProgram()
        glAttachShader(self.m_ShaderProgram, vertex_shader)
        glAttachShader(self.m_ShaderProgram, fragment_shader)
        glLinkProgram(self.m_ShaderProgram)

        # Check if the linking succeeded
        if glGetProgramiv(self.m_ShaderProgram, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(self.m_ShaderProgram).decode())

        # Clean up shaders as they're linked into the program now
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def Use(self):
        glUseProgram(self.m_ShaderProgram)

# GLFWWindow class handles OpenGL context and rendering
class GLFWWindow:
    def __init__(self, width, height, title):
        self.m_Width = width
        self.m_Height = height
        self.m_Title = title
        self.m_Window = None

        # Vertex data for a more visually appealing triangle (with color attributes)
        self.m_Vertices = np.array([
            # Positions       # Colors
            0.0,  0.5, 0.0,   1.0, 0.0, 0.0,  # Top vertex (Red)
           -0.5, -0.5, 0.0,   0.0, 1.0, 0.0,  # Bottom left vertex (Green)
            0.5, -0.5, 0.0,   0.0, 0.0, 1.0   # Bottom right vertex (Blue)
        ], dtype='float32')

        # Vertex Array Object and Vertex Buffer Object
        self.m_VAO = None
        self.m_VBO = None
        self.m_Shader = None

    def Init(self):
        # Initialize the GLFW library
        if not glfw.init():
            return False
        return True

    def CreateWindow(self):
        # Create a windowed mode window and its OpenGL context
        self.m_Window = glfw.create_window(self.m_Width, self.m_Height, self.m_Title, None, None)
        if not self.m_Window:
            glfw.terminate()
            return False
        
        # Make the window's context current
        glfw.make_context_current(self.m_Window)
        # Set the framebuffer size callback
        glfw.set_framebuffer_size_callback(self.m_Window, self.FramebufferSizeCallback)
        return True

    def FramebufferSizeCallback(self, window, width, height):
        glViewport(0, 0, width, height)

    def SetupShaders(self):
        # Vertex and fragment shader source code
        vertex_shader_source = """
        #version 330 core
        layout(location = 0) in vec3 position;
        layout(location = 1) in vec3 color;
        
        out vec3 vertexColor;

        void main()
        {
            gl_Position = vec4(position, 1.0);
            vertexColor = color;
        }
        """

        fragment_shader_source = """
        #version 330 core
        in vec3 vertexColor;
        out vec4 FragColor;

        void main()
        {
            FragColor = vec4(vertexColor, 1.0);  // Pass the interpolated color to the fragment shader
        }
        """

        # Create a Shader object
        self.m_Shader = Shader(vertex_shader_source, fragment_shader_source)

    def SetupBuffers(self):
        # Generate and bind a Vertex Array Object
        self.m_VAO = glGenVertexArrays(1)
        glBindVertexArray(self.m_VAO)

        # Generate and bind a Vertex Buffer Object
        self.m_VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.m_VBO)

        # Copy the vertex data to the buffer
        glBufferData(GL_ARRAY_BUFFER, self.m_Vertices.nbytes, self.m_Vertices, GL_STATIC_DRAW)

        # Define the vertex attributes for position (location = 0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * self.m_Vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Define the vertex attributes for color (location = 1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * self.m_Vertices.itemsize, ctypes.c_void_p(3 * self.m_Vertices.itemsize))
        glEnableVertexAttribArray(1)

        # Unbind the VBO and VAO
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def RenderTriangle(self):
        # Use the shader program and bind the VAO
        self.m_Shader.Use()
        glBindVertexArray(self.m_VAO)

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def OnUpdate(self):
        """
        This method will be used to handle logic updates. 
        You can include any updates you need to make before rendering, 
        such as input handling, object transformations, physics updates, etc.
        """
        # Example: Simple update logic (nothing to update in this basic example)
        # You can handle input here using glfw.get_key(), glfw.get_cursor_pos(), etc.
        pass

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
        self.SetupShaders()
        self.SetupBuffers()

        # Main loop
        while not glfw.window_should_close(self.m_Window):
            self.OnUpdate()  # Update logic here
            self.OnRender()  # Render frame
            
            # Swap front and back buffers
            glfw.swap_buffers(self.m_Window)
            
            # Poll for and process events
            glfw.poll_events()
        
        self.CloseWindow()

# Example usage
if __name__ == "__main__":
    app = GLFWWindow(800, 600, "OpenGL Triangle with OnUpdate")
    app.Run()
