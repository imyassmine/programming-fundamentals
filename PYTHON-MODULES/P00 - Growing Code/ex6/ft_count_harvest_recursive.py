#!/usr/bin/env python3

def ft_count_harvest_recursive(days: int = 0, day: int = 1) -> None:
    if days == 0:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(days, day + 1)
