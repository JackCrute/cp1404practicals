"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    print(data)
    display_subject_details(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts = [parts[0], parts[1], int(parts[2])]
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject, lecturer, and number of students from data."""
    for record in data:
        print(f"{record[0]} is taught by {record[1]:12} and has {record[2]:3} students")


main()
