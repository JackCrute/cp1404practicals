"""
CP1404 - Practical 3
File size
"""


def main():
    """Loop until filename is empty."""
    filename = input("Filename: ")
    while filename != "":
        number_of_lines = get_number_of_lines(filename)
        print(number_of_lines)
        filename = input("Filename: ")


def get_number_of_lines(filename):
    """Load filename and return number of lines."""
    number_of_lines = 0
    with open(filename) as in_file:
        for line in in_file:
            number_of_lines += 1
    return number_of_lines


main()
