#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> str:
            return (f"Stats: {self.grow_count} grow, "
                    f"{self.age_count} age, {self.show_count} show")

    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name
        self._height = float(height)
        self._age = age
        self._stats = self.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self._height += 0.8
        self._stats.grow_count += 1

    def age(self) -> None:
        self._age += 1
        self._stats.age_count += 1

    def _format_info(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"

    def show(self) -> str:
        self._stats.show_count += 1
        return self._format_info()

    def __str__(self) -> str:
        return self.show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def _format_info(self) -> str:
        base = super()._format_info()
        color_info = f"Color: {self.color}"
        bloom_status = ("is blooming beautifully!"
                        if self._is_blooming
                        else "has not bloomed yet")
        bloom_info = f"{self.name} {bloom_status}"
        return f"{base}\n{color_info}\n{bloom_info}"


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_count = 0

        def display(self) -> str:
            base = super().display()
            return f"{base}\n{self.shade_count} shade"

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._stats = self.TreeStats()

    def produce_shade(self) -> str:
        self._stats.shade_count += 1
        return (f"Tree {self.name} now produces a shade of "
                f"{self._height:.1f}cm long and "
                f"{self.trunk_diameter:.1f}cm wide.")

    def _format_info(self) -> str:
        base = super()._format_info()
        trunk_info = f"Trunk diameter: {self.trunk_diameter}cm"
        return f"{base}\n{trunk_info}"


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

    def _format_info(self) -> str:
        base = super()._format_info()
        harvest_info = f"Harvest season: {self.harvest_season}"
        nutrition_info = f"Nutritional value: {self.nutritional_value}"
        return f"{base}\n{harvest_info}\n{nutrition_info}"


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def _format_info(self) -> str:
        base = super()._format_info()
        seeds_info = f"Seeds: {self.seeds}"
        return f"{base}\n{seeds_info}"


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(plant._stats.display())


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    print(rose)
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    print(rose)
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    print(oak)
    display_stats(oak)
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    print(sunflower)
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    print(sunflower)
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous_plant()
    print(unknown)
    display_stats(unknown)
