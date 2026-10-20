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

    def _format_info(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> str:
        base = super().show()
        color_info = f"Color: {self.color}"
        bloom_status = ("is blooming beautifully!"
                        if self._is_blooming
                        else "has not bloomed yet")
        bloom_info = f"{self.name} {bloom_status}"
        return f"{base}\n{color_info}\n{bloom_info}"

    def __str__(self) -> str:
        return self.show()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> str:
        return (f"Tree {self.name} now produces a shade of "
                f"{self._height:.1f}cm "
                f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> str:
        base = super().show()
        trunk_info = f"Trunk diameter: {self.trunk_diameter}cm"
        return f"{base}\n{trunk_info}"

    def __str__(self) -> str:
        return self.show()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self._height += 1.3
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()

    def show(self) -> str:
        base = super().show()
        harvest_info = f"Harvest season: {self.harvest_season}"
        nutrition_info = f"Nutritional value: {self.nutritional_value}"
        return f"{base}\n{harvest_info}\n{nutrition_info}"

    def __str__(self) -> str:
        return self.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    print(rose)
    print("[asking the rose to bloom]")
    rose.bloom()
    print(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    print(oak)
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    print(tomato)
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    print(tomato)
