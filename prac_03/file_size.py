"""
CP1404 - Practical 3
File size
"""

def main():
    """Loop until filename is empty."""
    filename = input("Filename: ")
    while filename != "":
        number_of_lines = get_number_of_lines(filename)
        filename = input("Filename: ")


main()