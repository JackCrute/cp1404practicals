"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Get a score float and display its status."""
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)


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


main()
