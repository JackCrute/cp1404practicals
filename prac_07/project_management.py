"""
CP1404 Practical 7
Project management program.

Estimated time: 2 hours
Actual time:
"""

from prac_07.project import Project


def main():
    """Interact with file via menu and Project objects."""

    filename = "projects.txt"

    projects = load_projects(filename)
    print(projects)


def load_projects(filename):
    """Load file as list of Project objects."""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()  # Skip header row
    for line in in_file:
        parts = line.strip().split('\t')
        # TODO: convert parts[1] to datetime object later
        # start_date =
        projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    in_file.close()
    return projects


main()
