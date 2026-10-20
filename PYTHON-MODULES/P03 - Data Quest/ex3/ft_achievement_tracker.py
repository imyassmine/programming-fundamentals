#!/usr/bin/env python3

import random
from typing import Set


def gen_player_achievements() -> Set[str]:
    achievements_list = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder"
    ]
    count = random.randint(5, 9)
    return set(random.sample(achievements_list, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
        }
    for player_name, achievements in players.items():
        print(f"Player {player_name}: {achievements}")
    print()
    all_achievements = set[str]()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")
    print()
    common_achievements = players["Alice"].copy()
    for achievements in list(players.values())[1:]:
        common_achievements = common_achievements.intersection(achievements)
    print(f"Common achievements: {common_achievements}")
    print()
    for player_name, achievements in players.items():
        others_achievements = set[str]()
        for other_name, other_achiev in players.items():
            if other_name != player_name:
                others_achievements = others_achievements.union(other_achiev)
        unique = achievements.difference(others_achievements)
        print(f"Only {player_name} has: {unique}")
    print()
    for player_name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{player_name} is missing: {missing}")
