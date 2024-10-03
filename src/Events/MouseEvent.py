from Core.SCPCH import *
from Event import Event
from Input.KeyCodes import MouseButton

class MouseMovedEvent(Event):
    def __init__(self, x, y):
        super().__init__("MouseMoved")
        self.m_MouseX = x
        self.m_MouseY = y

    def get_x(self):
        return self.m_MouseX

    def get_y(self):
        return self.m_MouseY

    def __str__(self):
        return f"MouseMovedEvent: {self.m_MouseX}, {self.m_MouseY}"

    def GetEventType(self):
        return "MouseMoved"

class MouseScrolledEvent(Event):
    def __init__(self, x_offset, y_offset):
        super().__init__("MouseScrolled")
        self.m_XOffset = x_offset
        self.m_YOffset = y_offset

    def GetXOffset(self):
        return self.m_XOffset

    def GetYOffset(self):
        return self.m_YOffset

    def __str__(self):
        return f"MouseScrolledEvent: {self.GetXOffset()}, {self.GetYOffset()}"

    def GetEventType(self):
        return "MouseScrolled"

class MouseButtonEvent(Event):
    def __init__(self, button):
        super().__init__("MouseButtonEvent")
        self.m_Button = button

    def GetMouseButton(self):
        return self.m_Button

    def GetEventType(self):
        return "MouseButtonEvent"

class MouseButtonPressedEvent(MouseButtonEvent):
    def __init__(self, button):
        super().__init__(button)

    def __str__(self):
        return f"MouseButtonPressedEvent: {self.m_Button}"

    def GetEventType(self):
        return "MouseButtonPressed"

class MouseButtonReleasedEvent(MouseButtonEvent):
    def __init__(self, button):
        super().__init__(button)

    def __str__(self):
        return f"MouseButtonReleasedEvent: {self.m_Button}"

    def GetEventType(self):
        return "MouseButtonReleased"

class MouseButtonDownEvent(MouseButtonEvent):
    def __init__(self, button):
        super().__init__(button)

    def __str__(self):
        return f"MouseButtonDownEvent: {self.m_Button}"

    def GetEventType(self):
        return "MouseButtonDown"
