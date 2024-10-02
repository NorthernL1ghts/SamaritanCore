from Globals import Globals
from Logger import *
from ApplicationSettings import ApplicationSettings  # Import the ApplicationSettings class

class Application:
    class ApplicationSpecification:
        def __init__(self, application_name, version):
            self.m_ApplicationName = application_name
            self.m_Version = version

    s_Instance = None

    def __init__(self):
        self.m_ApplicationSpecification = None
        self.m_ApplicationSettings = ApplicationSettings()  # Create an instance of ApplicationSettings

    def InitializeComponents(self):
        Logger.Init()

        # Load settings if needed
        if self.m_ApplicationSettings.Deserialize():
            SC_LOG_CORE(SC_CORE_INFO, "Loaded application settings.")
        else:
            SC_LOG_CORE(SC_CORE_WARNING, "Failed to load application settings. Using defaults.")

        SC_LOG_CORE(SC_CORE_INFO, "Running the application...")
        SC_LOG_CORE(SC_CORE_INFO, "Application Name: %s, Version: %s", 
                    self.m_ApplicationSpecification.m_ApplicationName,
                    self.m_ApplicationSpecification.m_Version)

    def Run(self):
        self.m_ApplicationSpecification = Application.ApplicationSpecification("SamaritanCore", "1.0")
        self.InitializeComponents()

        while Globals.g_ApplicationRunning:
            SC_LOG_CORE(SC_CORE_DEBUG, "Application is running...")

        SC_LOG_CORE(SC_CORE_INFO, "Exiting the application...")
        Logger.Shutdown()  # Move the shutdown here to ensure it executes after main loop

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
