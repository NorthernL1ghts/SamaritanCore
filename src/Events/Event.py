from Core.SCPCH import *

class EventType(Enum):
    NoneType = auto()
    WindowClose = auto()
    WindowMinimize = auto()
    WindowResize = auto()
    WindowFocus = auto()
    WindowLostFocus = auto()
    WindowMoved = auto()
    WindowTitleBarHitTest = auto()
    AppTick = auto()
    AppUpdate = auto()
    AppRender = auto()
    KeyPressed = auto()
    KeyReleased = auto()
    KeyTyped = auto()
    MouseButtonPressed = auto()
    MouseButtonReleased = auto()
    MouseButtonDown = auto()
    MouseMoved = auto()
    MouseScrolled = auto()
    SelectionChanged = auto()
    AssetReloaded = auto()

class EventCategory(Enum):
    NoneType = 0
    EventCategoryApplication = 1 << 0
    EventCategoryInput = 1 << 1
    EventCategoryKeyboard = 1 << 2
    EventCategoryMouse = 1 << 3
    EventCategoryMouseButton = 1 << 4
    EventCategoryScene = 1 << 5
    EventCategoryEditor = 1 << 6

class Event:
    def __init__(self):
        self.Handled = False
        self.Synced = False  # Queued events are only processed if this is true.

    def GetEventType(self) -> EventType:
        raise NotImplementedError

    def GetName(self) -> str:
        raise NotImplementedError

    def GetCategoryFlags(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.GetName()

    def IsInCategory(self, category: EventCategory) -> bool:
        return self.GetCategoryFlags() & category.value

class EventDispatcher:
    T = TypeVar('T', bound=Event)

    def __init__(self, event: Event):
        self.m_Event = event

    def dispatch(self, func: Callable[[T], bool]) -> bool:
        if self.m_Event.GetEventType() == self.m_Event.get_static_type() and not self.m_Event.Handled:
            self.m_Event.Handled = func(self.m_Event)  # Call the handler function
            return True
        return False
