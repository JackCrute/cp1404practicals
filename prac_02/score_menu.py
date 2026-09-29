"""
CP1404 - Practical 2
Program to determine score status with menu.
"""

MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Program to get score, print result, and show stars."""
    user_score = get_valid_number(0, 100)
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            user_score = get_valid_number(0, 100)
        elif choice == "P":
            print(determine_score_status(user_score))
        elif choice == "S":
            print_symbol(user_score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("> ").upper()
    print("Goodbye.")


def get_valid_number(low, high):
    """Get a valid number between low and high values."""
    number = int(input("Enter number: "))
    while number <= low or number >= high:
        print("Invalid number.")
        number = int(input("Enter number: "))
    return number


def determine_score_status(score):
    """Determine score status from score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_symbol(length, symbol='*'):
    """Print line of symbols as long as length."""
    print(symbol * length)


main()
