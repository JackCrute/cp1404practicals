"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject subjects from file."""
    subjects = load_subject_details(FILENAME)
    display_subject_details(subjects)


def load_subject_details(filename=FILENAME):
    """Read subjects from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    records = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        records.append(parts)
    input_file.close()
    return records


def display_subject_details(subjects):
    """Display subject, lecturer, and number of students from subjects."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
