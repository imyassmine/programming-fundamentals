#!/usr/bin/env python3

import sys
import os
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:
        venv_name = "None detected"
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print()
        print("WARNING: You’re in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        venv_name = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print()
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You’re in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
