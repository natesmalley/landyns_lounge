from typing import List


class RecipeFinder:
    """Stub for finding highly rated recipes."""

    def __init__(self):
        # In a real implementation, this might query a database or API
        self.recipe_db = {
            "pizza": ["Neapolitan Pizza", "Margherita Pizza"],
            "burger": ["Classic Cheeseburger", "BBQ Bacon Burger"],
            "salad": ["Caesar Salad", "Greek Salad"],
            "sushi": ["California Roll", "Spicy Tuna Roll"],
            "pasta": ["Spaghetti Carbonara", "Pesto Pasta"],
        }

    def find_recipes(self, meal_type: str) -> List[str]:
        """Return a list of recipes for the meal type."""
        return self.recipe_db.get(meal_type, [])
