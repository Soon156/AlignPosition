import sys
from cx_Freeze import setup, Executable
from Env import current_version

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "packages": ["ml_dtypes", "pynput"],
    "include_files": ["Resources", "pose_landmarker_full.task", "posture_detection_model.keras", "pose_landmarker_lite.task"],
    "build_exe": "dist/AlignPosition"
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="AlignPosition",
    version=current_version,
    description="Align Position",
    options={"build_exe": build_exe_options},
    executables=[Executable("AlignPosition.py", base=base, icon="Resources/logo.ico", copyright="MSU")],
)
