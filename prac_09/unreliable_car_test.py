"""
CP1404 Practical 9 - Unreliable car test
"""
from unreliable_car import UnreliableCar


def main():
    """Test """
    my_car = UnreliableCar("ford fiesta", 1000, 50)
    # Reliability should print
    print(my_car)

    for i in range(100):
        # Final odometer reading should be around 500 if it only works half the time
        my_car.drive(10)
        print(my_car._odometer)


main()
