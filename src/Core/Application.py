from Globals import Globals
from Logger import *
from ApplicationSettings import ApplicationSettings  # Import the ApplicationSettings class
from Base import Base  # Import the Base class

class Application(Base):
    class ApplicationSpecification:
        def __init__(self, application_name, version):
            self.m_ApplicationName = application_name
            self.m_Version = version

    s_Instance = None

    def __init__(self):
        self.m_ApplicationSpecification = None
        self.m_ApplicationSettings = None  # Create an instance of ApplicationSettings
        self.m_Base = Base()  # Create an instance of Base
        self.m_Base.SetApplication(self)  # Pass this Application instance to Base

    def InitializeCore(self):
        self.m_Base.InitializeCore()  # Call Base class InitializeCore
        self.m_ApplicationSettings = ApplicationSettings()

        # Load settings if needed
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
        self.InitializeCore()  # Initialize components

        while Globals.g_ApplicationRunning:
            Logger.GetCoreLogger().Log(SC_CORE_DEBUG, "Application is running...")

        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Exiting the application...")
        self.ShutdownCore()  # Call the shutdown method in Application
        self.m_Base.ShutdownCore()  # Call the shutdown method from Base

    def ShutdownCore(self):
        # Add any cleanup logic here
        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Cleaning up application resources...")
        # You can perform any other necessary cleanup operations here
        Logger.GetCoreLogger().Log(SC_CORE_INFO, "Application shutdown complete.")

    @staticmethod
    def CreateApplication():
        if Application.s_Instance is None:
            Application.s_Instance = Application()
        return Application.s_Instance

class EntryPoint:
    @staticmethod
    def Main():
        application = Application.CreateApplication()
        application.Run()

if __name__ == "__main__":
    EntryPoint.Main()
