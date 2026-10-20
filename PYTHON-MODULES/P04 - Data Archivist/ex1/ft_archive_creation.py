#!/usr/bin/env python3


import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        content = None
        try:
            f = open(filename, 'r')
            print("---")
            print()
            content = f.read()
            print(content)
            print("---")
            f.close()
            print(f"File '{filename}' closed.")
            print()
        except OSError as e:
            print(f"Error opening file '{filename}': {e}")
        if content:
            lines = content.splitlines()
            transformed_content = ""
            for line in lines:
                line += "#\n"
                transformed_content += line
            print("Transform data:")
            print("---")
            print()
            print(transformed_content)
            print("---")
            new_filename = input("Enter new file name (or empty): ")
            if new_filename:
                out = None
                try:
                    out = open(new_filename, 'w')
                    out.write(transformed_content + "\n")
                    print(f"Saving data to '{new_filename}'")
                    print(f"Data saved in file '{new_filename}'.")
                except OSError as e:
                    print(f"Error saving file '{new_filename}': {e}")
                finally:
                    if out is not None:
                        out.close()
            else:
                print("Not saving data.")
