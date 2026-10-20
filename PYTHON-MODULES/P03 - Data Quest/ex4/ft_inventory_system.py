#!/usr/bin/env python3

import sys
from typing import Dict

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: Dict[str, int] = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name, quantity_str = parts
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError:
            print(f"Quantity error for '{item_name}': ")
            print(f"invalid literal for int() with base 10: '{quantity_str}'")
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    for item, quantity in inventory.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")
    if inventory:
        most_item = max(inventory.items(), key=lambda x: x[1])
        least_item = min(inventory.items(), key=lambda x: x[1])
        print("Item most abundant: ")
        print(f"{most_item[0]} with quantity {most_item[1]}")
        print("Item least abundant: ")
        print(f"{least_item[0]} with quantity {least_item[1]}")
        new_item = "magic_item"
        inventory[new_item] = 1
        print(f"Updated inventory: {inventory}")
