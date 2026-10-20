#!/usr/bin/env python3

import random
from typing import Generator, Tuple, List


def gen_event() -> Generator[Tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
        ]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        events_list: List[Tuple[str, str]]
        ) -> Generator[Tuple[str, str], None, None]:
    while events_list:
        event = random.choice(events_list)
        events_list.remove(event)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(1000):
        name, action = next(event_gen)
        if i < 15 or i >= 992:
            print(f"Event {i}: Player {name} did action {action}")
        elif i == 15:
            print("[...]")
    event_list = [next(gen_event()) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        name, action = event
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
