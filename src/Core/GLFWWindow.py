import glfw
from Window import Window

class GLFWWindow(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.m_Window = None

    def Init(self):
        """Initialize GLFW and create the window."""
        if not glfw.init():
            return False
        return True

    def CreateWindow(self):
        """Create the GLFW window and OpenGL context."""
        self.m_Window = glfw.create_window(self.m_Width, self.m_Height, self.m_Title, None, None)
        if not self.m_Window:
            glfw.terminate()
            return False
        
        glfw.make_context_current(self.m_Window)
        glfw.set_framebuffer_size_callback(self.m_Window, self.FramebufferSizeCallback)
        
        return True

    def ShouldClose(self):
        """Check if the window should close."""
        return glfw.window_should_close(self.m_Window)

    def SwapBuffers(self):
        """Swap the front and back buffers."""
        glfw.swap_buffers(self.m_Window)

    def PollEvents(self):
        """Poll for and process events."""
        glfw.poll_events()

    def CloseWindow(self):
        """Cleanup and close the window."""
        glfw.destroy_window(self.m_Window)
        glfw.terminate()

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
