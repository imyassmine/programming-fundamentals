#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = float(height)
        self._age = age

    def show(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"

    def __str__(self) -> str:
        return self.show()

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")
