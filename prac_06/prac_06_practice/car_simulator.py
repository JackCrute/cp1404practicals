"""
CP1404 Practical 6 - Practice

Program to
"""

from prac_06.car import Car

MENU = ("Menu:\n"
        "d) drive\n"
        "r) refuel\n"
        "q) quit")


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name)

    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":

        if choice == "d":
            drive_car(car)

        elif choice == "r":
            refuel_car(car)

        else:
            print("Invalid choice")

        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()

    print()
    print(f"Good bye {car.name}'s driver.")


def refuel_car(car):
    refuel_amount = int(input("How many units of fuel do you want to add to the car? "))
    while refuel_amount < 0:
        print("Fuel amount must be >= 0")
        refuel_amount = int(input("How many units of fuel do you want to add to the car? "))
    car.add_fuel(refuel_amount)
    print(f"Added {refuel_amount} units of fuel.")
    return car


def drive_car(car):
    """Determine distance driven and if the car runs out of fuel during the drive."""
    distance_to_drive = int(input("How many km do you wish to drive? "))
    while distance_to_drive < 0:
        print("Distance must be >= 0")
        distance_to_drive = int(input("How many km do you wish to drive? "))
    distance_driven = car.drive(distance_to_drive)
    if car.fuel > 0:
        print(f"The car drove {distance_driven}km.")
    else:
        print(f"The car drove {distance_driven}km and ran out of fuel.")
    return car


main()
