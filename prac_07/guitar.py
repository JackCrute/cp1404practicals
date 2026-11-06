"""
CP1404 Practical 6
Guitar class

Estimated time: 15 minutes
Actual time: 10 minutes
"""

import datetime


class Guitar:
    """Store information related to guitars."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise instance of Guitar with following variables."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        """Return developer-friendly representation of Guitar"""
        return f"{vars(self)}"

    def __lt__(self, other):
        """Determine if Guitar is younger than other based on year attribute."""
        return self.year < other.year

    def get_age(self):
        """Calculate current age of Guitar in years."""
        return int(datetime.datetime.now().year) - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage if it is older than 50 years."""
        if self.get_age() >= 50:
            return True
        else:
            return False
