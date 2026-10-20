#!/usr/bin/env python3


from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()
    results = []
    for ingredient in allowed:
        results.append(ingredient in ingredients_lower)
    is_valid = any(results)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
