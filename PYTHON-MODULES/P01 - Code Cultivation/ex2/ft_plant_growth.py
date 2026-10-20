#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self._age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self._age} days old"

    def __str__(self) -> str:
        return self.show()

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height

    print("=== Garden Plant Growth ===")
    print(rose)

    for i in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {i} ===")
        print(rose)

    print(f"Growth this week: {rose.height - initial_height:.1f}cm")
