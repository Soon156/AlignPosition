import sys
from cx_Freeze import setup, Executable

# Replace "your_script.py" with the actual name of your Python script
script = "AlignPosition.py"
base = "Win32GUI" if sys.platform == "win32" else None

# Create an instance of the Executable class
executable = Executable(
    script,
    copyright="Copyright (C) 2023 cx_Freeze",
    # base=base,
    icon="Resources/logo.ico",
    shortcut_name="Align Position",
    shortcut_dir="AlignPosition",
)

# List of additional files or directories to be included
additional_files = [
    "Resources"
]

setup(
    name="Align Position",  # Replace "YourAppName" with your desired application name
    version="1.0.0",
    description="Align Position",
    executables=[executable],
    options={
        "build_exe": {
            "include_files": additional_files,
            # "packages": ["winotify", "multiprocessing"],
            "include_msvcr": True
        }
    }
)
