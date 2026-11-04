"""
CP1404 Practical 7

"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to read guitars from file and display them sorted by year."""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Load a list of guitars from a csv file."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
