from typing import Dict


class ProviderClient:
    """Placeholder for integration with external grocery services."""

    def compare_prices(
        self, grocery_list: Dict[str, int]
    ) -> Dict[str, Dict[str, float]]:
        """Compare prices across providers.

        This stub returns dummy pricing data. Integrate with real
        provider APIs (Uber Eats, Safeway, Walmart) for production use.
        """
        sample_price = 5.0
        return {
            "uber_eats": {item: sample_price for item in grocery_list},
            "safeway": {item: sample_price for item in grocery_list},
            "walmart": {item: sample_price for item in grocery_list},
        }
