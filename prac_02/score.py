"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Get user score and random score and print their status."""
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(f"User score {score:.1f} is {score_status}")
    if score_status == "Excellent":
        print("You get a prize!")
    score = generate_random_integer(0, 100)
    score_status = determine_score_status(score)
    print(f"Random: {score} = {score_status}")


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


def generate_random_integer(low, high):
    """Return a random integer between low and high values"""
    return random.randint(low, high)


main()
