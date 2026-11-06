"""
CP1404 Practical 7
Project class module.
"""


class Project:
    """Project class."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Project with attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Provide string representation of Project."""
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __repr__(self):
        """Provide developer-friendly represenation of Project"""
        return f"{vars(self)}"

    def __lt__(self, other):
        """Determine if Project is less than other based on priority attribute."""
        return self.priority < other.priority
