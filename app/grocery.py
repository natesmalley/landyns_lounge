from typing import List, Dict


class GroceryListBuilder:
    """Build grocery lists from recipes."""

    def __init__(self):
        # Example mapping of recipes to ingredients
        self.ingredients = {
            "Neapolitan Pizza": ["dough", "tomato", "mozzarella"],
            "Margherita Pizza": ["dough", "tomato", "basil"],
            "Classic Cheeseburger": ["bun", "ground beef", "cheese"],
            "BBQ Bacon Burger": ["bun", "ground beef", "bacon", "bbq sauce"],
            "Caesar Salad": ["romaine", "croutons", "parmesan"],
            "Greek Salad": ["lettuce", "feta", "olives"],
            "California Roll": ["rice", "crab", "avocado"],
            "Spicy Tuna Roll": ["rice", "tuna", "spicy mayo"],
            "Spaghetti Carbonara": ["spaghetti", "egg", "pancetta"],
            "Pesto Pasta": ["pasta", "basil", "parmesan"],
        }

    def build_grocery_list(self, recipes: List[str]) -> Dict[str, int]:
        """Create a grocery list counting ingredient usage."""
        grocery = {}
        for recipe in recipes:
            for item in self.ingredients.get(recipe, []):
                grocery[item] = grocery.get(item, 0) + 1
        return grocery
