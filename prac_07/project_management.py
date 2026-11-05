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
    display_projects(projects)
    # save_projects(filename, projects)


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    incomplete_projects.sort()
    completed_projects = [project for project in projects if project.completion_percentage == 100]
    completed_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"\t{project}")


def save_projects(filename, projects):
    """Save list of projects to file."""
    out_file = open(filename, "w")
    print("Name	Start Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)  # Re-add header row
    for project in projects:
        line = f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}"
        print(line, file=out_file)
    out_file.close()


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
