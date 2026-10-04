"""
CP1404 - Practical 3
File size
"""


def main():
    """Loop and print number of lines in a file until filename is empty."""
    is_valid_input = False
    while not is_valid_input:
        try:
            filename = input("Enter filename: ")
            if filename != "":
                number_of_lines = get_number_of_lines(filename)
                print(f"{filename} has {number_of_lines} lines.")
            else:
                is_valid_input = True
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")


def get_number_of_lines(filename):
    """Load filename and return number of lines."""
    number_of_lines = 0
    with open(filename) as in_file:
        for line in in_file:
            number_of_lines += 1
    return number_of_lines


main()
