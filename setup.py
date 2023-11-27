from cx_Freeze import setup, Executable
import sys

# Include packages
build_exe_options = {
    "packages": ["os", "sys", "PyQt5", "openai", "json", "docx", "dotenv"],
    "excludes": ["tkinter"],
    "include_files": ['pr_generator/']
}

# Executable setup
setup(
    name = "PR_MA_generator",
    version = "0.1",
    description = "Generates press releases and media advisories via a ChatGPT framework",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py")]
)
