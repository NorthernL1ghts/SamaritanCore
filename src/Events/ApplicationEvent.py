from Event import Event, EventCategory, EventType
from Core.SCPCH import *

class WindowResizeEvent(Event):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.m_Width = width
        self.m_Height = height

    def GetWidth(self) -> int:
        return self.m_Width

    def GetHeight(self) -> int:
        return self.m_Height

    def GetEventType(self) -> EventType:
        return EventType.WindowResize

    def GetName(self) -> str:
        return "WindowResizeEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value

    def __str__(self) -> str:
        return f"WindowResizeEvent: {self.m_Width}, {self.m_Height}"

class WindowMinimizeEvent(Event):
    def __init__(self, minimized: bool):
        super().__init__()
        self.m_Minimized = minimized

    def IsMinimized(self) -> bool:
        return self.m_Minimized

    def GetEventType(self) -> EventType:
        return EventType.WindowMinimize

    def GetName(self) -> str:
        return "WindowMinimizeEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value

class WindowCloseEvent(Event):
    def __init__(self):
        super().__init__()

    def GetEventType(self) -> EventType:
        return EventType.WindowClose

    def GetName(self) -> str:
        return "WindowCloseEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value

class WindowTitleBarHitTestEvent(Event):
    def __init__(self, x: int, y: int, hit: np.ndarray):
        super().__init__()
        self.m_X = x
        self.m_Y = y
        self.m_Hit = hit  # This should be a mutable structure

    def GetX(self) -> int:
        return self.m_X

    def GetY(self) -> int:
        return self.m_Y

    def set_hit(self, hit: bool):
        self.m_Hit[0] = int(hit)  # Set hit as an integer (0 or 1)

    def GetEventType(self) -> EventType:
        return EventType.WindowTitleBarHitTest

    def GetName(self) -> str:
        return "WindowTitleBarHitTestEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value


class AppTickEvent(Event):
    def __init__(self):
        super().__init__()

    def GetEventType(self) -> EventType:
        return EventType.AppTick

    def GetName(self) -> str:
        return "AppTickEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value


class AppUpdateEvent(Event):
    def __init__(self):
        super().__init__()

    def GetEventType(self) -> EventType:
        return EventType.AppUpdate

    def GetName(self) -> str:
        return "AppUpdateEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value


class AppRenderEvent(Event):
    def __init__(self):
        super().__init__()

    def GetEventType(self) -> EventType:
        return EventType.AppRender

    def GetName(self) -> str:
        return "AppRenderEvent"

    def GetCategoryFlags(self) -> int:
        return EventCategory.EventCategoryApplication.value
