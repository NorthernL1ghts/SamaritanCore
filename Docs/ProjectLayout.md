# Samaritan Core Framework Layout

# Layout:
    SamaritanCore/
    ├── src/
    │   ├── Core/
    │   │   ├── Application.py
    │   │   ├── Base.py                     # Base / Inheritance
    │   │   ├── EntryPoint.py               # Base / Inheritance
    │   │   ├── Logger.py
    │   │   ├── FileSystem.py
    │   │   ├── Timer.py
    │   │   ├── TimeStep.py
    │   │   └── UUID.py
    │   │
    │   ├── Debug/
    │   │   └── Instrumentor.py             # Instrumentation and debugging utilities
    │   │
    │   ├── Events/
    │   │   ├── ApplicationEvent.py
    │   │   ├── Event.py                    # Base / Inheritance
    │   │   ├── MouseEvent.py
    │   │   └── KeyEvent.py
    │   │
    │   ├── Math/
    │   │   └── MathF.py                    # Math functions and utilities
    │   │
    │   ├── Project/
    │   │   ├── Project.py                  # Main project class
    │   │   └── ProjectSerializer.py        # Serialization utilities for project data
    │   │
    │   ├── Scripting/
    │   │   ├── ScriptGlue.py               # Glue code for scripting integration
    │   │   └── ScriptingEngine.py          # Main scripting engine
    │   │
    │   ├── Utils/
    │   │   └── PlatformDetection.py        # Platform detection and utility functions
    │   │
    │   ├── Helper/
    │   │   └── HelperFunctions.py          # Reusable helper functions
    │   │
    │   ├── Input/
    │   │   ├── Input.py                    # Main input handling module
    │   │   ├── KeyCodes.py                 # Key codes and mappings
    │   │   └── MouseCodes.py               # Mouse codes and mappings
    │   │
    │   └── UI/
    │       ├── Interface.py                # Base / Inheritance for platform contexts
    │       │
    │       ├── Tkinter/
    │       │   ├── TkinterWindow.py        # Tkinter window implementation
    │       │   └── Components/             # Tkinter-specific UI components
    │       │       ├── Button.py
    │       │       ├── Label.py
    │       │       ├── Font.py
    │       │       ├── Text.py
    │       │       ├── Slider.py
    │       │       ├── Menu.py
    │       │       └── MenuBar.py
    │       │
    │       ├── GLFW/
    │       │   └── GLFWWindow.py           # GLFW window implementation
    │       │
    │       └── OpenGL/
    │           └── OpenGLContext.py        # OpenGL context setup
    │
    ├── Assets/                             # Assets for SamaritanCore, such as logo, icons, etc.
    │
    ├── docs/
    │   ├── Documentation.md                # Main documentation file
    │   └── Todo.md                         # To-do list and project planning
    │
    ├── ScriptCore/
    │   ├── Input.py                        # Input handling for scripting
    │   ├── Intercalls.py                   # Inter-process calls or API connections for scripting
    │   ├── KeyCodes.py                     # Key codes for scripting use
    │   ├── Vector2.py                      # 2D vector utility for scripting
    │   ├── Vector3.py                      # 3D vector utility for scripting
    │   └── Vector4.py                      # 4D vector utility for scripting
    │
    ├── Scripts/
    │   ├── Build.bat                       # Windows build script
    │   └── Build.sh                        # POSIX (Linux/Mac) build script
    │
    ├── .github/
    │   ├── ISSUE_TEMPLATE/
    │   │   ├── config.yml                  # Configuration file for issue templates
    │   │   ├── issue--bug-report.md        # Template for bug reports
    │   │   ├── issue--feature--request.md  # Template for feature requests
    │   │   └── other-issue-blank-template.md # Template for other issues
    │   ├── PULL_REQUEST_TEMPLATE.md        # Template for pull requests
    │   ├── CONTRIBUTING.md                 # Contribution guidelines
    │   ├── CODE_OF_CONDUCT.md              # Code of conduct
    │   └── SECURITY.md                     # Security policy and vulnerability reporting
    │
    └── SCPCH.py                            # Precompiled header for SamaritanCore