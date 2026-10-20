#!/usr/bin/env python3


from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def count_calls() -> int:
        nonlocal count
        count += 1
        return count
    return count_calls


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate_power(power_add: int) -> int:
        nonlocal power
        power += power_add
        return power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store_memory(key: str, value: Any) -> None:
        vault[key] = value

    def recall_memory(key: str) -> Any:
        if key not in vault:
            return "Memory not found"
        return vault.get(key, None)
    return {"store": store_memory, "recall": recall_memory}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    spell_acc = spell_accumulator(100)
    print(f"Base 100, add 20: {spell_acc(20)}")
    print(f"Base 100, add 30: {spell_acc(30)}")
    print()
    print("Testing enchantment factory...")
    flaming_sword = enchantment_factory("Flaming")
    frozen_shield = enchantment_factory("Frozen")
    print(flaming_sword("Sword"))
    print(frozen_shield("Shield"))
    print()
    print("Testing memory vault...")
    memory = memory_vault()
    memory["store"]("secret", 42)
    print(f"Stored 'secret' = {memory['recall']('secret')}")
    print(f"Recall 'secret' : {memory['recall']('secret')}")
    print(f"Recall 'unknown' : {memory['recall']('unknown')}")


if __name__ == "__main__":
    main()
