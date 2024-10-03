from Logger import *
from SCPCH import platform, sys

# Platform checks
if platform.system() == 'Windows':
    def SC_DEBUG_BREAK():
        import ctypes
        ctypes.windll.kernel32.DebugBreak()
elif platform.system() == 'Darwin':  # macOS
    def SC_DEBUG_BREAK():
        import signal
        signal.raise_signal(signal.SIGTRAP)
else:  # Other platforms
    def SC_DEBUG_BREAK():
        pass

# Debug mode check
SC_DEBUG = True  # NOTE: Set this to True to enable asserts

SC_ENABLE_VERIFY = True

if SC_DEBUG:
    def SC_CORE_ASSERT_MESSAGE_INTERNAL(message, *args):
        Logger.PrintAssertMessage("Core", "Assertion Failed: " + message % args)

    def SC_ASSERT_MESSAGE_INTERNAL(message, *args):
        Logger.PrintAssertMessage("Client", "Assertion Failed: " + message % args)

    def SC_CORE_ASSERT(condition, *args):
        if not condition:
            SC_CORE_ASSERT_MESSAGE_INTERNAL(*args)
            SC_DEBUG_BREAK()

    def SC_ASSERT(condition, *args):
        if not condition:
            SC_ASSERT_MESSAGE_INTERNAL(*args)
            SC_DEBUG_BREAK()
else:
    def SC_CORE_ASSERT(condition, *args):
        pass

    def SC_ASSERT(condition, *args):
        pass

if SC_ENABLE_VERIFY:
    def SC_CORE_VERIFY_MESSAGE_INTERNAL(message, *args):
        Logger.PrintAssertMessage("Core", "Verify Failed: " + message % args)

    def SC_VERIFY_MESSAGE_INTERNAL(message, *args):
        Logger.PrintAssertMessage("Client", "Verify Failed: " + message % args)

    def SC_CORE_VERIFY(condition, *args):
        if not condition:
            SC_CORE_VERIFY_MESSAGE_INTERNAL(*args)
            SC_DEBUG_BREAK()

    def SC_VERIFY(condition, *args):
        if not condition:
            SC_VERIFY_MESSAGE_INTERNAL(*args)
            SC_DEBUG_BREAK()
else:
    def SC_CORE_VERIFY(condition, *args):
        pass

    def SC_VERIFY(condition, *args):
        pass