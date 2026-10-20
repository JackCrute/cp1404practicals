"""
CP1404 - Practical 5
Hex Colours
"""

COLOUR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff", "amber": "#ffbf00",
                  "aqua": "#00ffff", "asparagus": "#87a96b", "baby blue": "#89cff0", "bistre": "#3d2b1f",
                  "bleu de france": "#318ce7", "boysenberry": "#873260"}

colour_name = input("Enter name of colour_name: ").lower()
while colour_name != "":
    try:
        print(f"Code for {colour_name} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour_name")
    colour_name = input("Enter name of colour_name: ").lower()
