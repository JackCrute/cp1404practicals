"""
CP1404 Practical 7
Program to allow interaction with file containing guitar details using the Guitar class.
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load file of guitar details as objects, add, display, and save guitars to file."""
    guitars = load_guitars(FILENAME)
    get_guitar(guitars)
    display_guitars(guitars)
    save_guitars(guitars)


def save_guitars(guitars):
    """Save guitars to file."""
    out_file = open(FILENAME, 'w')
    for guitar in guitars:
        line = f"{guitar.name}, {guitar.year}, {guitar.cost}"
        print(line, file=out_file)
    out_file.close()


def display_guitars(guitars):
    """Display guitars sorted by year."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_guitar(guitars):
    """Get new guitar details and add it to guitars."""
    name = input("Enter name of new guitar: ")
    while name != "":
        year = int(input("Enter the year the new guitar was produced: "))
        cost = float(input("Enter cost of new guitar: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter name of new guitar: ")


def load_guitars(filename):
    """Load file of guitar details as list of Guitar objects."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
