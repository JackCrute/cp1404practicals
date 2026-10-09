"""
CP1404 - Practical 4
Quick picks
"""
from random import randint

NUMBER_OF_LINES = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Program generate as many lines of random numbers as quick picks."""
    number_of_quick_picks = int(input("Number of quick picks: "))
    for i in range(number_of_quick_picks):
        numbers = []
        for j in range(NUMBER_OF_LINES):
            number = randint(MINIMUM, MAXIMUM)
            while number in numbers:
                number = randint(MINIMUM, MAXIMUM)
            numbers.append(number)
        # noinspection PyUnboundLocalVariable
        numbers.sort()
        print(" ".join(f"{number:2}" for number in numbers))


main()
