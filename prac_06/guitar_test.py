"""
CP1404 Practical 6
Program for testing Guitar class

Start time: 3:24pm
Estimated time: 10 minutes
Actual time: 8 minutes
"""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    jibson = Guitar("Another Guitar", 2013, 12000.3)

    print(f"{gibson.name} get_age() - Expected 104. Got {gibson.get_age()}")
    print(f"{jibson.name} get_age() - Expected 13. Got {jibson.get_age()}")

    print()

    print(f"{gibson.name} is_vintage - Expected True. Got {gibson.is_vintage()}")
    print(f"{jibson.name} is_vintage - Expected False. Got {jibson.is_vintage()}")


main()
