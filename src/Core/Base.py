from Logger import *  # Import the Logger here for initialization
from SCPCH import platform

# Macros
def BIT(x):
    return 1 << x

# Platform checks
if not (platform.system() == 'Windows' or platform.system() == 'Linux'):
    raise RuntimeError("Unknown platform.")

class AtomicFlag:
    def __init__(self):
        self._flag = Lock()
        self.SetDirty()

    def SetDirty(self):
        with self._flag:
            self._dirty = True

    def CheckAndResetIfDirty(self):
        with self._flag:
            if self._dirty:
                self._dirty = False
                return True
            return False

# Simple flag implementation
class Flag:
    def __init__(self):
        self._flag = False

    def SetDirty(self):
        self._flag = True

    def CheckAndResetIfDirty(self):
        if self._flag:
            self._flag = False
            return True
        return False

    def IsDirty(self):
        return self._flag

# Base class
class Base:
    def __init__(self):
        self.m_Application = None  # Instance of Application

    def InitializeCore(self):
        Logger.Init()  # Initialize the logger or other core components

    def SetApplication(self, application):
        self.m_Application = application  # Set the Application instance

    def ShutdownCore(self):
        if self.m_Application:
            Logger.GetCoreLogger().Log(SC_CORE_INFO, "Shutting down the application...")
            self.m_Application.ShutdownCore()  # Call the application's shutdown method
            Logger.Shutdown()  # Ensure logger is also properly shut down
        else:
            Logger.GetCoreLogger().Log(SC_CORE_WARNING, "No application instance to shut down.")

    def Run(self):
        raise NotImplementedError("Derived classes must implement Run()")
