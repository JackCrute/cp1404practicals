"""
CP1404 Practical 5 - Practice

Program to make and modify a dictionary mapping friends to addresses.
"""
MENU = "(A)dd\n(C)hange\n(D)isplay\n(Q)uit"


def main():
    """Allow interaction with friend to address dictionary via menu."""
    friend_to_address = {}

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            add_friend_to_address(friend_to_address)

        elif choice == "C":
            if not friend_to_address:   # Check if dictionary is empty
                print("No friends :(")
            else:
                change_friend_address(friend_to_address)

        elif choice == "D":
            if not friend_to_address:   # Check if dictionary is empty
                print("No friends :(")
            else:
                display_friend_address(friend_to_address)

        else:
            print("Invalid input.")

        print(MENU)
        choice = input(">>> ").upper()


def display_friend_address(friend_to_address):
    """Display address of friend."""
    friend = get_valid_name(friend_to_address)
    print(f"{friend}'s address is {friend_to_address[friend]}.")


def change_friend_address(friend_to_address):
    """Change address of friend."""
    friend = get_valid_name(friend_to_address)
    address = input("New address: ")
    friend_to_address[friend] = address
    print(f"Changed {friend}'s address to {friend_to_address[friend]}.")
    return friend_to_address


def add_friend_to_address(friend_to_address):
    """Add new entry of friend to address dictionary."""
    friend = input("Name of friend: ")
    address = input("Address of friend: ")
    friend_to_address[friend] = address
    print(f"Added {friend} who lives at {friend_to_address[friend]}.")
    return friend_to_address


def get_valid_name(friend_to_address):
    """Get name that exists in friend to name."""
    friend = input("Name of friend: ")
    while friend not in friend_to_address:  # Check if key friend exists
        print("Friend does not exist")
        friend = input("Name of friend: ")
    return friend


main()
