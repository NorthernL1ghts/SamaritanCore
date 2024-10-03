from Globals import Globals
from Logger import *
from ApplicationSettings import ApplicationSettings
from Base import Base
from GLFWWindow import GLFWWindow

from SCPCH import *

class Application(Base):
    class ApplicationSpecification:
        def __init__(self, application_name, version):
            self.m_ApplicationName = application_name
            self.m_Version = version

    s_Instance = None
    s_MainThreadID = None

    def __init__(self):
        self.m_ApplicationSpecification = None
        self.m_ApplicationSettings = None

        self.m_Base = Base()
        self.m_Base.SetApplication(self)
        Application.s_Instance = self
        Application.s_MainThreadID = threading.get_ident()

        # Create GLFW window
        self.m_GLFWWindow = GLFWWindow(800, 600, "SamaritanCore.exe")

    def InitializeCore(self):
        self.m_Base.InitializeCore()
        self.m_ApplicationSettings = ApplicationSettings()

        if self.m_ApplicationSettings.Deserialize():
            Logger.GetCoreLogger().Log(SC_CORE_INFO, "Loaded application settings.")
        else:
            Logger.GetCoreLogger().Log(SC_CORE_WARNING, "Failed to load application settings. Using defaults.")

        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Running the application...")
        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Application Name: %s, Version: %s", 
                       self.m_ApplicationSpecification.m_ApplicationName,
                       self.m_ApplicationSpecification.m_Version)

    def Run(self):
        self.m_ApplicationSpecification = Application.ApplicationSpecification("SamaritanCore", "1.0")
        self.InitializeCore()

        # Run GLFW window
        self.m_GLFWWindow.Run()

        while Globals.g_ApplicationRunning:
            Logger.GetCoreLogger().Log(SC_CORE_DEBUG, "Application is running...")

        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Exiting the application...")
        self.ShutdownCore()
        self.m_Base.ShutdownCore()

    def ShutdownCore(self):
        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Cleaning up application resources...")
        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Application shutdown complete.")

    @staticmethod
    def CreateApplication(argc, argv):
        if Application.s_Instance is None:
            Application.s_Instance = Application()  # Heap allocation of Application instance
        return Application.s_Instance

    @staticmethod
    def GetMainThreadID():
        return Application.s_MainThreadID

    @staticmethod
    def IsMainThread():
        return threading.get_ident() == Application.s_MainThreadID

class EntryPoint:
    @staticmethod
    def Main(argc, argv):
        application = Application.CreateApplication(argc, argv)
        application.Run()

if __name__ == "__main__":
    EntryPoint.Main(len(sys.argv), sys.argv)