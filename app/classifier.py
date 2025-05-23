from typing import Dict, Tuple
from PIL import Image
import numpy as np


class MealClassifier:
    """Naive meal classifier based on average image color."""

    def __init__(self):
        # Predefined average RGB color signatures for each meal type.
        # These values are approximate and serve only as a lightweight
        # heuristic in this example implementation.
        self.meal_signatures: Dict[str, Tuple[int, int, int]] = {
            "pizza": (220, 90, 60),
            "burger": (170, 120, 70),
            "salad": (80, 150, 90),
            "sushi": (180, 180, 190),
            "pasta": (220, 200, 150),
        }

    def _average_color(self, image: Image.Image) -> Tuple[float, float, float]:
        """Return the average RGB color of the provided image."""
        img = image.convert("RGB")
        arr = np.array(img)
        # Compute mean across height and width, preserving color channels
        mean_rgb = arr.mean(axis=(0, 1))
        return tuple(mean_rgb)

    def classify(self, image: Image.Image) -> str:
        """Classify the meal in the image using average color distance."""
        avg = self._average_color(image)
        distances = {
            meal: np.linalg.norm(np.array(avg) - np.array(signature))
            for meal, signature in self.meal_signatures.items()
        }
        # Return the meal with the smallest color distance
        return min(distances, key=distances.get)

    def verify_with_similar_images(self, image: Image.Image) -> bool:
        """Verify the meal by checking the color distance threshold."""
        meal_type = self.classify(image)
        avg = self._average_color(image)
        signature = self.meal_signatures[meal_type]
        distance = np.linalg.norm(np.array(avg) - np.array(signature))
        # Accept the classification if the distance is reasonably small
        return distance < 80.0
