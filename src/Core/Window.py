import numpy as np
from OpenGL.GL import *

class Window:
    def __init__(self, width, height, title):
        self.m_Width = width
        self.m_Height = height
        self.m_Title = title
        self.m_Window = None

        # Vertex data for a triangle
        self.m_Vertices = np.array([
            0.0,  0.5, 0.0,  # Top vertex
           -0.5, -0.5, 0.0,  # Bottom left vertex
            0.5, -0.5, 0.0   # Bottom right vertex
        ], dtype='float32')

        # OpenGL handles
        self.m_VAO = None
        self.m_VBO = None
        self.m_ShaderProgram = None

    def Init(self):
        """Initialize the platform-specific window system (to be overridden)."""
        raise NotImplementedError("Init method must be implemented by subclasses.")

    def CreateWindow(self):
        """Create the window (to be overridden)."""
        raise NotImplementedError("CreateWindow method must be implemented by subclasses.")

    def FramebufferSizeCallback(self, window, width, height):
        """Resize the framebuffer when the window is resized."""
        glViewport(0, 0, width, height)

    def CompileShader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise RuntimeError(glGetShaderInfoLog(shader).decode())
        return shader

    def CreateShaderProgram(self):
        """Create and compile the shaders."""
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
            // Set the color based on the fragment position for a rainbow effect
            color = vec4(gl_FragCoord.x / 800.0, gl_FragCoord.y / 600.0, 0.5, 1.0);  // Example for rainbow-like effect
        }
        """

        vertex_shader = self.CompileShader(vertex_shader_source, GL_VERTEX_SHADER)
        fragment_shader = self.CompileShader(fragment_shader_source, GL_FRAGMENT_SHADER)

        self.m_ShaderProgram = glCreateProgram()
        glAttachShader(self.m_ShaderProgram, vertex_shader)
        glAttachShader(self.m_ShaderProgram, fragment_shader)
        glLinkProgram(self.m_ShaderProgram)

        # Clean up shaders as they're linked into the program now
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def SetupBuffers(self):
        """Set up vertex buffers and vertex array objects."""
        self.m_VAO = glGenVertexArrays(1)
        glBindVertexArray(self.m_VAO)

        self.m_VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.m_VBO)
        glBufferData(GL_ARRAY_BUFFER, self.m_Vertices.nbytes, self.m_Vertices, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def RenderTriangle(self):
        """Render a triangle."""
        glUseProgram(self.m_ShaderProgram)  # Ensure the shader program is active
        glBindVertexArray(self.m_VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def OnRender(self):
        """Clear the screen and render the triangle."""
        glClearColor(0.1, 0.1, 0.1, 1.0)  # Clear to dark background
        glClear(GL_COLOR_BUFFER_BIT)
        self.RenderTriangle()  # Render the triangle

    def OnUpdate(self):
        """Update logic (can be overridden)."""
        pass

    def Run(self):
        """Main loop handling update, render, and events."""
        if not self.Init():
            return
        if not self.CreateWindow():
            return

        self.CreateShaderProgram()  # Create the shader program
        self.SetupBuffers()  # Set up vertex buffers and VAO

        while not self.ShouldClose():
            self.OnUpdate()
            self.OnRender()  # Render the triangle
            self.SwapBuffers()
            self.PollEvents()

        self.CloseWindow()

    def ShouldClose(self):
        """Check if the window should close (to be overridden)."""
        raise NotImplementedError("ShouldClose method must be implemented by subclasses.")

    def SwapBuffers(self):
        """Swap buffers (to be overridden)."""
        raise NotImplementedError("SwapBuffers method must be implemented by subclasses.")

    def PollEvents(self):
        """Poll for and process events (to be overridden)."""
        raise NotImplementedError("PollEvents method must be implemented by subclasses.")

    def CloseWindow(self):
        """Cleanup and close the window (to be overridden)."""
        raise NotImplementedError("CloseWindow method must be implemented by subclasses.")
