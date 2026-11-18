"""
SilverServiceTaxi class module.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness: float):
        """Initialise SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Provide string representation of SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Get fare amount including flagfall."""
        return super().get_fare() + self.flagfall
