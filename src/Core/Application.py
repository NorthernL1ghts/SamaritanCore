from Globals import Globals
from Logger import *

class Application:
    class ApplicationSpecification:
        def __init__(self, application_name, version):
            self.m_ApplicationName = application_name
            self.m_Version = version

    s_Instance = None

    def __init__(self):
        self.m_ApplicationSpecification = None

    def InitializeComponents(self):
        Logger.Init()

        # Core logger messages
        SC_LOG_CORE(SC_CORE_TRACE, "This is a core trace message.")
        SC_LOG_CORE(SC_CORE_DEBUG, "Debugging core application...")
        SC_LOG_CORE(SC_CORE_INFO, "This is a core info message.")
        SC_LOG_CORE(SC_CORE_WARNING, "This is a core warning message.")
        SC_LOG_CORE(SC_CORE_ERROR, "This is a core error message.")
        SC_LOG_CORE(SC_CORE_CRITICAL, "This is a core fatal message.")

        # Client logger messages
        SC_LOG_CLIENT(SC_CORE_DEBUG, "Debugging client application...")
        SC_LOG_CLIENT(SC_CORE_TRACE, "This is a client trace message.")
        SC_LOG_CLIENT(SC_CORE_INFO, "User: %s, Status: %s", "Alice", "active")
        SC_LOG_CLIENT(SC_CORE_WARNING, "This is a client warning message.")
        SC_LOG_CLIENT(SC_CORE_ERROR, "This is a client error message.")
        SC_LOG_CLIENT(SC_CORE_CRITICAL, "This is a client fatal message.")

        # Shutdown the logger
        Logger.Shutdown()
        

    def Run(self):
        self.m_ApplicationSpecification = Application.ApplicationSpecification("SamaritanCore", "1.0")
        self.InitializeComponents()

        SC_LOG_CORE(SC_CORE_INFO, "Running the application...")
        SC_LOG_CORE(SC_CORE_INFO, "Application Name: %s, Version: %s", 
                    self.m_ApplicationSpecification.m_ApplicationName,
                    self.m_ApplicationSpecification.m_Version)

        while Globals.g_ApplicationRunning:
            SC_LOG_CORE(SC_CORE_DEBUG, "Application is running...")

        SC_LOG_CORE(SC_CORE_INFO, "Exiting the application...")

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
