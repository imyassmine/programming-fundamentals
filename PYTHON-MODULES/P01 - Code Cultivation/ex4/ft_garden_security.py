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

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        print(f"Height updated: {height}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print(f"Plant created: {rose}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-10)
    print()
    print(f"Current state: {rose}")
