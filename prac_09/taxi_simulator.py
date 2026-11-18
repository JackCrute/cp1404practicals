"""CP1404 Practical 9 - Taxi simulator"""

from taxi import Taxi

from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Menu for taxi simulator program."""
    current_taxi = None
    total_fare = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":

        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(current_taxi, taxis)

        elif choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                current_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip will cost you ${current_fare:.2f}")
                total_fare += current_fare
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(current_taxi, taxis):
    """Choose current taxi."""
    try:
        chosen_taxi = int(input("Choose taxi: "))
        current_taxi = taxis[chosen_taxi]
    except ValueError:
        print("Invalid distance value")
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    """Display all taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxis[i]}")


main()
