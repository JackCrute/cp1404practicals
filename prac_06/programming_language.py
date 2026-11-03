"""
CP1404 Practical 6
Class for programming languages
Started at 2:34pm
Estimated time: 20 minutes
Actual time: 24 minutes
"""


class ProgrammingLanguage:
    """Group programming language related values together."""

    def __init__(self, name="", typing="", has_reflection=False, year=0):
        """Initialise instance of ProgrammingLanguage with below variables."""
        self.name = name
        self.typing = typing
        self.has_reflection = has_reflection
        self.year = year

    def __str__(self):
        """Return string of ProgrammingLanguage values."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.has_reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Represent object values as system-view of string."""
        return str(self)

    def is_dynamic(self):
        """Check if ProgrammingLanguage is of "Dynamic" typing."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
