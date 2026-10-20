#!/usr/bin/env python3


import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        try:
            f = open(filename, 'r')
            print("---")
            print()
            print(f.read())
            print("---")
            f.close()
            print(f"File '{filename}' closed.")
        except OSError as e:
            print(f"Error opening file '{filename}': {e}")
