from typing import List
from PIL import Image


class MealClassifier:
    """Simple meal classifier stub."""

    def __init__(self):
        # Placeholder for model or dataset initialization
        self.known_meals = [
            "pizza",
            "burger",
            "salad",
            "sushi",
            "pasta",
        ]

    def classify(self, image: Image.Image) -> str:
        """Classify the meal in the image.

        This implementation is a stub and always returns "pizza".
        Replace with a real model for production use.
        """
        return "pizza"

    def verify_with_similar_images(self, image: Image.Image) -> bool:
        """Verify the meal using similar images.

        This stub always returns True. Implement image similarity
        checks against a curated dataset for real verification.
        """
        return True
