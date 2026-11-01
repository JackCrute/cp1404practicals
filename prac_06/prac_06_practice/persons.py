"""
CP1404 Practical 6 - Practice

Program to collect and display information about Person instances.
"""

from prac_06.prac_06_practice.person import Person

MENU = "(A)dd person, (D)isplay people, (Q)uit"


def main():
    persons = []

    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":

        if choice == "A":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            age = int(input("Age: "))
            persons.append(Person(first_name, last_name, age))

        elif choice == "D":
            print(persons)
            max_first_name_length = max(len(person.first_name) for person in persons)
            max_last_name_length = max(len(person.last_name) for person in persons)
            max_age_length = max(len(str(person.age)) for person in persons)
            print("-" * (max_first_name_length + max_last_name_length + max_age_length + 22))
            for i, person in enumerate(persons, 1):
                print(f"{i}    Name: {person.first_name:{max_first_name_length}} {person.last_name:{max_last_name_length}}     Age: {person.age:{max_age_length}}")

        else:
            print("Invalid choice.")

        print(MENU)
        choice = input(">>>").upper()


main()
