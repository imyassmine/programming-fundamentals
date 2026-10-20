#!/usr/bin/env python3

def display_plant_info(name: str, height: int, age: int) -> None:
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    display_plant_info("Rose", 25, 30)
    print()
    print("=== End of Program ===")
