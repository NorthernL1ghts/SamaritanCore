from SCPCH import *

class LogLevel:
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

# Constants for log folder locations
c_LogsFolderLocation = r"C:\Dev\Samaritan\SamaritanCore\logs"  # Base log folder
c_SamaritanCoreLogFolder = os.path.join(c_LogsFolderLocation, "SamaritanCore")
c_APPLogFolder = os.path.join(c_LogsFolderLocation, "APP")

# Macros for logging levels
SC_CORE_TRACE = LogLevel.TRACE
SC_CORE_DEBUG = LogLevel.DEBUG
SC_CORE_INFO = LogLevel.INFO
SC_CORE_WARNING = LogLevel.WARNING
SC_CORE_ERROR = LogLevel.ERROR
SC_CORE_CRITICAL = LogLevel.CRITICAL

# Macros for logging messages with safe checking if loggers are initialized
SC_LOG_CORE = lambda level, msg, *args: Logger.s_CoreLogger.Log(level, msg, *args) if Logger.s_CoreLogger is not None else None
SC_LOG_CLIENT = lambda level, msg, *args: Logger.s_ClientLogger.Log(level, msg, *args) if Logger.s_ClientLogger is not None else None

class Logger:
    s_CoreLogger = None
    s_ClientLogger = None
    s_Pattern = "[{timestamp}] [{name}] - {level} - {message}"
    s_Lock = threading.Lock()  # Ensuring thread-safety for file writes

    @classmethod
    def Init(cls):
        cls.CreateLogFolder()  # Create log folder structure
        cls.s_CoreLogger = cls("SamaritanCore", os.path.join(c_SamaritanCoreLogFolder, "SamaritanCore.log"))
        cls.s_ClientLogger = cls("APP", os.path.join(c_APPLogFolder, "App.log"))
        cls.s_CoreLogger.SetLevel(LogLevel.TRACE)  # Default level for core logger
        cls.s_ClientLogger.SetLevel(LogLevel.DEBUG)  # Default level for client logger
        cls.SetPattern("[{timestamp}] [{name}] - {level} - {message}")  # Set log pattern

    @classmethod
    def CreateLogFolder(cls):
        # Create logs directory structure
        os.makedirs(c_SamaritanCoreLogFolder, exist_ok=True)
        os.makedirs(c_APPLogFolder, exist_ok=True)

    def __init__(self, name, file_name):
        self.m_Name = name
        self.m_Level = LogLevel.TRACE  # Default log level
        self.m_FileName = file_name

    def SetLevel(self, level):
        self.m_Level = level

    def Log(self, level, message, *args):
        if level >= self.m_Level:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
            formatted_message = message % args if args else message
            log_message = self.s_Pattern.format(
                timestamp=timestamp,
                name=self.m_Name,
                level=self.GetLevelName(level),
                message=formatted_message
            )
            self.WriteToFile(log_message)

    def WriteToFile(self, message):
        try:
            with self.s_Lock:
                with open(self.m_FileName, 'a') as log_file:
                    log_file.write(message + '\n')
        except Exception as e:
            if self.m_Level <= LogLevel.ERROR:
                print(f"Error writing to log file: {e}")

    def Trace(self, message, *args):
        self.Log(LogLevel.TRACE, message, *args)

    def Debug(self, message, *args):
        self.Log(LogLevel.DEBUG, message, *args)

    def Info(self, message, *args):
        self.Log(LogLevel.INFO, message, *args)

    def Warning(self, message, *args):
        self.Log(LogLevel.WARNING, message, *args)

    def Error(self, message, *args):
        self.Log(LogLevel.ERROR, message, *args)

    def Critical(self, message, *args):
        self.Log(LogLevel.CRITICAL, message, *args)

    def GetLevelName(self, level):
        if level == LogLevel.TRACE:
            return "TRACE"
        elif level == LogLevel.DEBUG:
            return "DEBUG"
        elif level == LogLevel.INFO:
            return "INFO"
        elif level == LogLevel.WARNING:
            return "WARNING"
        elif level == LogLevel.ERROR:
            return "ERROR"
        elif level == LogLevel.CRITICAL:
            return "CRITICAL"
        return "UNKNOWN"

    @classmethod
    def GetCoreLogger(cls):
        return cls.s_CoreLogger

    @classmethod
    def GetClientLogger(cls):
        return cls.s_ClientLogger

    @classmethod
    def SetPattern(cls, pattern):
        cls.s_Pattern = pattern

    @classmethod
    def ResetLogger(cls, logger):
        if logger:
            logger.DropAll()
        return None

    def DropAll(self):
        try:
            self.Info(f"Dropping all logs for {self.m_Name}.")
            # Additional cleanups can be added here
        except Exception as e:
            self.Error(f"Failed to drop logs: {e}")

    @classmethod
    def Shutdown(cls):
        core_logger = cls.GetCoreLogger()
        if core_logger:
            core_logger.Info("Shutting down core logger...")
        client_logger = cls.GetClientLogger()
        if client_logger:
            client_logger.Info("Shutting down client logger...")

        cls.s_CoreLogger = cls.ResetLogger(core_logger)
        cls.s_ClientLogger = cls.ResetLogger(client_logger)

        if core_logger:
            core_logger.Info("Core logger has been reset and dropped.")
        if client_logger:
            client_logger.Info("Client logger has been reset and dropped.")

    @classmethod
    def PrintAssertMessage(cls, log_type, message, *args):
        if log_type == "Core":
            SC_LOG_CORE(LogLevel.ERROR, message, *args)
        elif log_type == "Client":
            SC_LOG_CLIENT(LogLevel.ERROR, message, *args)
