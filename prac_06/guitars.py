"""
CP1404 Practical 6
Program to play guitars from Guitar class

Start time: 3:42pm
Estimated time: 20 minutes
Actual time: 14 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Program to print guitars and their details."""
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
