"""
CP1404 - Practical 2
Program for printing a number of stars equal to the length of a password.
"""

MINIMUM_LENGTH = 10


def main():
    """Get and print a hidden password."""
    password = get_valid_password(MINIMUM_LENGTH)
    print_stars(password)


def get_valid_password(minimum_length):
    """Get password longer than minimum length."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password too short.")
        password = input("Password: ")
    return password


def print_stars(password, symbol='*'):
    """Print a number of symbols equal to the length of password."""
    print(len(password) * symbol)


main()
