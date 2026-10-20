#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        coordinates_list = coordinates.split(",")
        if len(coordinates_list) != 3:
            print("Invalid syntax")
            continue
        try:
            player_pos: list[float] = []
            for coordinate in coordinates_list:
                player_pos.append(float(coordinate))
            break
        except ValueError as e:
            print(f"Error on parameter '{coordinate}': {e}")
    return (player_pos[0], player_pos[1], player_pos[2])


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return math.sqrt(
        (b[0] - a[0]) ** 2
        + (b[1] - a[1]) ** 2
        + (b[2] - a[2]) ** 2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    print(f"Got a first tuple: {coordinates}")
    print(
        f"It includes: X={coordinates[0]}, "
        f"Y={coordinates[1]}, Z={coordinates[2]}"
    )
    print(
        "Distance to center: "
        f"{round(distance((0, 0, 0), coordinates), 4)}"
    )
    print("Get a second set of coordinates")
    new_coordinates = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance(coordinates, new_coordinates), 4)}"
    )
