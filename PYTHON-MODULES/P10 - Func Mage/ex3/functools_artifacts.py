#!/usr/bin/env python3


from collections.abc import Callable
import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)
    raise ValueError(f"Invalid operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, power=50, element="fire"),
        "ice": functools.partial(base_enchantment, power=50, element="ice"),
        "wind": functools.partial(base_enchantment, power=50, element="wind")
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    try:
        spell_reducer(spells, 'invalid')
    except ValueError as e:
        print(f"Caught expected exception: {e}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")
    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"{dispatcher(42)}")
    print(f"{dispatcher('fireball')}")
    print(f"{dispatcher([1, 2, 3])}")
    print(f"{dispatcher(None)}")


if __name__ == "__main__":
    main()
