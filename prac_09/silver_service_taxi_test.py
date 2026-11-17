"""CP1404 Practical 9 - SilverServiceTaxi test."""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    my_taxi = SilverServiceTaxi("green machine", 100, 2)
    # Should print the added flagfall amount at the end
    print(my_taxi)

    # Expected value with fanciness of 2
    assert my_taxi.price_per_km == 2.46

    my_taxi.drive(18)
    assert my_taxi.get_fare() == 48.78


main()
