from Globals import Globals

class Application:
    class ApplicationSpecification:
        def __init__(self, application_name, version):
            self.m_ApplicationName = application_name
            self.m_Version = version

    s_Instance = None

    def __init__(self):
        self.m_ApplicationSpecification = None

    def InitializeComponents(self):
        print("Initializing components...")

    def Run(self):
        self.m_ApplicationSpecification = Application.ApplicationSpecification("SamaritanCore", "1.0")
        self.InitializeComponents()
        
        print("Running the application...")
        print(f"Application Name: {self.m_ApplicationSpecification.m_ApplicationName}")
        
        while Globals.g_ApplicationRunning:
            print("Application is running...")

        print("Exiting the application...")

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
