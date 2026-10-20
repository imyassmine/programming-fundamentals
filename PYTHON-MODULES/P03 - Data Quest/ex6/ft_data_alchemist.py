#!/usr/bin/env python3


import random
from typing import Dict


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    players = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
        ]
    print(f"Initial list of players: {players}")
    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")
    print()
    score_dict: Dict[str, int] = {name: random.randint(54, 907)
                                  for name in all_capitalized}
    print(f"Score dict: {score_dict}")
    avg_score = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {avg_score:.2f}")
    high_scores = {name: score for name, score in score_dict.items()
                   if score > avg_score}
    print(f"High scores: {high_scores}")
