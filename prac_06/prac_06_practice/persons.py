"""
CP1404 Practical 6 - Practice

Program to collect and display information about Person instances.
"""

from prac_06_practice.person import Person

MENU = "(A)dd person, (C)hange person details, (D)isplay people, (Q)uit"


def main():
    persons = []

    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":

        if choice == "A":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            age = int(input("Age: "))
            persons.append()

        elif choice == "C":
            pass

        elif choice == "D":
            pass

        else:
            print("Invalid choice.")





main()