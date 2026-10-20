"""
CP1404 - Practical 5
Emails
Estimate: 30 minutes
Actual: 15 minutes
"""


def main():
    """Program to fill a dictionary mapping emails to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
        print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email."""
    name = email.split('@')
    name = name[0]
    if '.' in name:
        name = " ".join(name.split('.'))
    name = name.title()
    return name


main()
