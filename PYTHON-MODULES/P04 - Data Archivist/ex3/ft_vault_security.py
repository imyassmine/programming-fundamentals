#!/usr/bin/env python3


def secure_archive(
        filename: str, operation: str = "read", content: str = ""
        ):
    try:
        if operation == "read":
            with open(filename, 'r') as f:
                file_content = f.read()
            return (True, file_content)
        elif operation == "write":
            with open(filename, 'w') as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid operation")
    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", "read")
    print(result)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd", "read")
    print(result)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    test_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    secure_archive("test_archive.txt", "write", test_content)
    result = secure_archive("test_archive.txt", "read")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    new_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    result = secure_archive("preservation_archive.txt", "write", new_content)
    print(result)
