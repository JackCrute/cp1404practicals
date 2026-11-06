"""
CP1404 Practical 7
Project management program.

Estimated time: 2 hours
Actual time: 1 hr 15 min +
"""

from prac_07.project import Project

import datetime


def main():
    """Interact with file via menu and Project objects."""

    filename = "projects.txt"

    projects = load_projects(filename)
    display_projects(projects)
    add_project(projects)
    update_project(projects)
    save_projects(filename, projects)


def update_project(projects):
    """Update chosen project completion percentage and priority."""
    for project_index, project in enumerate(projects):
        print(f"{project_index} {project}")

    project_choice = int(input("Project choice: "))
    print(projects[project_choice])

    new_percentage = int(input("New Percentage: "))
    if new_percentage != "":
        projects[project_choice].completion_percentage = new_percentage

    new_priority = int(input("New Priority: "))
    if new_priority != "":
        projects[project_choice].priority = new_priority


def add_project(projects):
    """Add new Project to projects."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (d/m/yyyy): ")
    # Convert date string into datetime object.
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    # Create list for all projects below 100% completion.
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    incomplete_projects.sort()
    # Create list for all projects at 100% completion.
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
        # Convert datetime object into date string of correct format.
        formatted_start_date = project.start_date.strftime("%d/%m/%Y")
        line = f"{project.name}\t{formatted_start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}"
        print(line, file=out_file)
    out_file.close()


def load_projects(filename):
    """Load file as list of Project objects."""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()  # Skip header row
    for line in in_file:
        parts = line.strip().split('\t')
        # Convert parts[1] into datetime object.
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        projects.append(Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4])))
    in_file.close()
    return projects


main()
