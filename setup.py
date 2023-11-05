import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["ml_dtypes"],
    "include_files": ["Resources", "pose_landmarker_full.task", "posture_detection_model.keras"],
    "build_exe": "dist/AlignPosition"
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="AlignPosition",
    version="0.5",
    description="Align Position",
    options={"build_exe": build_exe_options},
    executables=[Executable("AlignPosition.py", base=base, icon="Resources/logo.ico", copyright="MSU")],
)
