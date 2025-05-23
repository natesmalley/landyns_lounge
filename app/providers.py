from typing import Dict
from random import Random


class ProviderClient:
    """Placeholder for integration with external grocery services."""

    def __init__(self, seed: int | None = 0) -> None:
        # Use a deterministic random generator for reproducible pricing.
        self.random = Random(seed)

    def compare_prices(
        self, grocery_list: Dict[str, int]
    ) -> Dict[str, Dict[str, float]]:
        """Compare prices across providers using randomly generated data."""

        providers = ["uber_eats", "safeway", "walmart"]
        result: Dict[str, Dict[str, float]] = {}
        for provider in providers:
            provider_prices: Dict[str, float] = {}
            for item in grocery_list:
                # Price between 2 and 10 dollars
                price = 2.0 + self.random.random() * 8.0
                provider_prices[item] = round(price, 2)
            result[provider] = provider_prices
        return result
