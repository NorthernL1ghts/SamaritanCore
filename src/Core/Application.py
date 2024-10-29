import time
import threading
import sys
import os
from typing import Callable, List

class ApplicationCommandLineArgs:
    def __init__(self, args: List[str]):
        self.m_Args = args
        self.m_Count = len(args)

    def __getitem__(self, index: int) -> str:
        # FIXME: This will be an ASSERT to ensure that only one instance exists!
        assert index < self.m_Count, "Index out of range"
        return self.m_Args[index]

class ApplicationSpecification:
    def __init__(self, name: str = "SamaritanCore", working_directory: str = "", args: List[str] = None):
        self.m_Name = name
        self.m_WorkingDirectory = working_directory
        self.m_CommandLineArgs = ApplicationCommandLineArgs(args or [])

class Application:
    s_Instance = None  # Static instance of Application

    def __init__(self, specification: ApplicationSpecification):
        self.m_Specification = specification  # Store the specification
        self.m_IsRunning = False  # Flag to indicate if the application is running
        self.m_MainThreadQueue: List[Callable] = []  # Queue for main thread functions
        self.m_MainThreadQueueMutex = threading.Lock()  # Mutex for thread safety
        Application.s_Instance = self  # Set static instance to this

        # Set the working directory
        if self.m_Specification.m_WorkingDirectory:
            os.chdir(self.m_Specification.m_WorkingDirectory)

    @staticmethod
    def Get() -> 'Application':
        return Application.s_Instance

    def Run(self):
        self.m_IsRunning = True
        print(f"{self.m_Specification.m_Name} is starting...")
        # Main application logic goes here

        # Simulate some work
        while self.m_IsRunning:
            self.ExecuteMainThreadQueue()  # Execute any queued functions

    def Shutdown(self):
        print("Shutting down the application...")
        self.m_IsRunning = False

    def SubmitToMainThread(self, function: Callable):
        with self.m_MainThreadQueueMutex:
            self.m_MainThreadQueue.append(function)

    def ExecuteMainThreadQueue(self):
        with self.m_MainThreadQueueMutex:
            for func in self.m_MainThreadQueue:
                func()  # Execute the function
            self.m_MainThreadQueue.clear()  # Clear the queue

def CreateApplication(args: ApplicationCommandLineArgs) -> Application:
    # Create ApplicationSpecification based on command-line arguments
    specification = ApplicationSpecification(args=args.m_Args)
    return Application(specification)

class EntryPoint:
    def __init__(self, args):
        self.m_Args = ApplicationCommandLineArgs(args)

    def Main(self):
        app = CreateApplication(self.m_Args)
        try:
            app.Run()
        except KeyboardInterrupt:
            app.Shutdown()

if __name__ == "__main__":
    entry_point = EntryPoint(sys.argv[1:])  # Pass command-line arguments
    entry_point.Main()  # Call the Main method to run the application
