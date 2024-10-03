from Window import Window
import glfw

class GLFWWindow(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def Init(self):
        """Initialize GLFW."""
        if not glfw.init():
            return False
        return True

    def CreateWindow(self):
        """Create a GLFW window."""
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
        """Swap front and back buffers."""
        glfw.swap_buffers(self.m_Window)

    def PollEvents(self):
        """Poll for and process events."""
        glfw.poll_events()

    def CloseWindow(self):
        """Clean up and close the GLFW window."""
        glfw.terminate()
