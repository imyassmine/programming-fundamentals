#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    test_values = ["25", "abc"]

    for input_temp in test_values:
        try:
            print(f"Input data is '{input_temp}'")
            temp = input_temperature(input_temp)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
