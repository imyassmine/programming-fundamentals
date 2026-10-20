#!/usr/bin/env python3


import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_ancient_text.py <file>")
    else:
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
        filename = sys.argv[1]
        sys.stdout.write(f"Accessing file '{filename}'\n")
        content = None
        try:
            f = open(filename, 'r')
            sys.stdout.write("---\n\n")
            content = f.read()
            sys.stdout.write(content)
            sys.stdout.write("\n")
            sys.stdout.write("---\n")
            f.close()
            sys.stdout.write(f"File '{filename}' closed.\n\n")
        except OSError as e:
            sys.stderr.write(
                f"[STDERR] Error opening file '{filename}': {e}\n"
                )
        if content:
            lines = content.splitlines()
            transformed_content = ""
            for line in lines:
                line += "#\n"
                transformed_content += line
            sys.stdout.write("Transform data:\n")
            sys.stdout.write("---\n\n")
            sys.stdout.write(transformed_content)
            sys.stdout.write("\n")
            sys.stdout.write("---\n")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_filename = sys.stdin.readline().strip()
            if new_filename:
                out = None
                try:
                    sys.stdout.write(f"Saving data to '{new_filename}'\n")
                    out = open(new_filename, 'w')
                    out.write(transformed_content + "\n")
                    sys.stdout.write(f"Data saved in file '{new_filename}'.\n")
                except OSError as e:
                    sys.stderr.write(
                        f"[STDERR] Error opening file '{new_filename}': {e}\n"
                        )
                    sys.stdout.write("Data not saved.\n")
                finally:
                    if out is not None:
                        out.close()
            else:
                sys.stdout.write("Not saving data.\n")
