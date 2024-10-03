from Core.SCPCH import *
from Event import Event
from Input.KeyCodes import KeyCode  # Assuming you have a KeyCode class similar to MouseButton

class KeyEvent(Event):
    def __init__(self, keycode):
        super().__init__("KeyEvent")
        self.m_KeyCode = keycode

    def GetKeyCode(self):
        return self.m_KeyCode

    def GetEventType(self):
        return "KeyEvent"

class KeyPressedEvent(KeyEvent):
    def __init__(self, keycode, repeat_count):
        super().__init__(keycode)
        self.m_RepeatCount = repeat_count

    def GetRepeatCount(self):
        return self.m_RepeatCount

    def __str__(self):
        return f"KeyPressedEvent: {self.m_KeyCode} ({self.m_RepeatCount} repeats)"

    def GetEventType(self):
        return "KeyPressed"

class KeyReleasedEvent(KeyEvent):
    def __init__(self, keycode):
        super().__init__(keycode)

    def __str__(self):
        return f"KeyReleasedEvent: {self.m_KeyCode}"

    def GetEventType(self):
        return "KeyReleased"

class KeyTypedEvent(KeyEvent):
    def __init__(self, keycode):
        super().__init__(keycode)

    def __str__(self):
        return f"KeyTypedEvent: {self.m_KeyCode}"

    def GetEventType(self):
        return "KeyTyped"
