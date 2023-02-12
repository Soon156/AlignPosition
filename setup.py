import sys
from cx_Freeze import setup, Executable

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Align Position",  # Name that will be show on the link
     "TARGETDIR",  # Component_
     "[TARGETDIR]Align Position.exe",  # Target exe to execute
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

Files = ["Resources", "Readme.txt"]

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "packages": ['plyer'],
    "include_files": Files
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

target = Executable(
    script="Align Position.py",
    base=base,
    icon="Resources/logo.ico"
)

setup(
    name="Align Position",
    version="0.1",
    author="Soon Kok Seng",
    author_email='soonkokseng2015@gmail.com',
    description="Align Position",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    url="https://thearronproject.ddns.net/",
    download_url="https://thearronproject.ddns.net/Align%20Position-0.1-win64.msi?",
    license="apache-2.0",
    executables=[target]

)
