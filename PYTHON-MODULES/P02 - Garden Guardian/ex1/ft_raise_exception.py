#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_values = ["25", "abc", "100", "-50"]

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
