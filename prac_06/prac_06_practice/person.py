"""
CP1404 Practical 6 - Practice

Person class module.
"""


class Person:
    """Person class."""

    def __init__(self, first_name="", last_name="", age=0):
        """Define a Person object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Display Person variables as a string."""
        return f"{self.first_name} {self.last_name}, {self.age} year old"

    def __repr__(self):
        """Display Person variables as the system-view of a string."""
        return str(vars(self))
