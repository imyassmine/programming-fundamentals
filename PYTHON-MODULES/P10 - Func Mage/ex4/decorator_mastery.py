#!/usr/bin/env python3


import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            power: int | None = None
            power_value = kwargs.get("power")
            if isinstance(power_value, int):
                power = power_value
            elif args:
                last_arg = args[-1]
                if isinstance(last_arg, int):
                    power = last_arg
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                            )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name.strip()) >= 3
            and all(char.isalpha() or char.isspace() for char in name)
            )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"
    result = fireball()
    print(f"Result: {result}")
    print()
    print("Testing retrying spell...")

    @retry_spell(3)
    def failing_spell() -> str:
        raise RuntimeError("Spell exploded")
    print(failing_spell())

    @retry_spell(3)
    def successful_spell() -> str:
        return "Waaaaaaagh spelled !"
    print(successful_spell())
    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Alice"))
    print(MageGuild.validate_mage_name("Bob"))
    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
