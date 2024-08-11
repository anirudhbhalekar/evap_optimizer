import sys
import subprocess
import importlib

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    required_packages = ['PySide6', 'numpy', 'openpyxl', 'pyqt6']
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"{package} not found. Installing...")
            install(package)
    
    # Once all packages are installed, run the main script
    from eo_window  import open_window
    open_window()
if __name__ == "__main__":
    main()