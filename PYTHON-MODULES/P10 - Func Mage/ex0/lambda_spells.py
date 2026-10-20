#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(mage["power"] for mage in mages) / len(mages), 2
            )
        }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92},
        {"name": "Ice Wand", "power": 78}
    ]
    mages = [
        {"name": "Gandalf", "power": 95},
        {"name": "Merlin", "power": 88},
        {"name": "Morgana", "power": 76}
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
        f"power) comes before {sorted_artifacts[1]['name']}"
        f"({sorted_artifacts[1]['power']} power)"
        )
    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))
    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    for key, value in stats.items():
        print(f"{key}: {value}")
    print()
    print("Testing power filter...")
    filtered_mages = power_filter(mages, 80)
    for mage in filtered_mages:
        print(f"{mage['name']} ({mage['power']} power)")


if __name__ == "__main__":
    main()
