"""UnreliableCar class module."""

from car import Car
from random import randint


class UnreliableCar(Car):
    """UnreliableCar class."""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Provide string representation of UnreliableCar."""
        return f"{super().__str__()}, with reliability of {self.reliability}"

    def drive(self, distance):
        """Drive normally only if reliability is higher than random number."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return super().drive(0)

