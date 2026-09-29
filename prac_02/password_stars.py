"""Practical 2 - Password Star Program"""

MINIMUM_LENGTH = 10


def main():
    """Get and print a hidden password."""
    password = get_valid_password(MINIMUM_LENGTH)
    print(len(password) * '*')


def get_valid_password(minimum_length):
    """Get password longer than minimum length."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password too short.")
        password = input("Password: ")
    return password


main()
