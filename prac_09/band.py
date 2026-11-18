"""Band class module."""

from operator import attrgetter


class Band:
    """Band class."""

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        print("band str")
        return f"{self.name} ({str(self.members).strip('[]')})"

    def add(self, member):
        """Add member to band."""
        self.members.append(member)

    def play(self):
        """Return a string showing the member playing their first (or no) instrument."""
        for member in self.members:
            if not member.instruments:
                print(f"{member.name} needs an instrument!")
            else:
                print(f"{member.name} is playing: {member.instruments[0]}")
