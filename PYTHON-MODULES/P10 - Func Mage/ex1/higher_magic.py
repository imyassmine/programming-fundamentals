#!/usr/bin/env python3


from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        sequence = []
        for spell in spells:
            sequence.append(spell(target, power))
        return sequence
    return sequence_spell


def is_powerful(target: str, power: int) -> bool:
    return power >= 5


def main() -> None:
    print("Testing spell combiner...")
    combo_result = spell_combiner(fireball, heal)('Dragon', 10)
    print(f"Combined spell result: {', '.join(combo_result)}")
    print()

    print("Testing power amplifier...")
    original_power = 10
    multiplier = 3
    amplified_result = (
        power_amplifier(fireball, multiplier)('Dragon', original_power)
    )
    print(f"Original: {original_power},"
          f" Amplified: {original_power * multiplier}")
    print(f"Amplified spell result: {amplified_result}")
    print()

    print("Testing conditional caster...")
    print("Conditional spell result: "
          f"{conditional_caster(is_powerful, fireball)('Dragon', 10)}")
    print("Fizzled spell result: "
          f"{conditional_caster(is_powerful, fireball)('Dragon', 2)}")
    print()

    print("Testing spell sequence...")
    sequence_result = spell_sequence([fireball, heal])('Dragon', 10)
    print(f"Spell sequence result: {', '.join(sequence_result)}")


if __name__ == "__main__":
    main()
