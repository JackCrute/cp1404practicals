"""
CP1404 - Practical 5
Wimbledon
Estimate: 40 minutes
Actual: 1hr 40 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Program to read a file of wimbledon records, process its data, and display wimbledon champion information."""
    wimbledon_records = load_file(FILENAME)
    champion_to_wins, countries = process_records(wimbledon_records)
    display_champions(champion_to_wins, countries)


def load_file(filename):
    """Load and save file contents to wimbledon_records variable."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        wimbledon_records = []
        for line in in_file:
            wimbledon_records.append(line.rstrip().split(','))
        print(wimbledon_records)
        return wimbledon_records


def process_records(wimbledon_records):
    """Process records into a dictionary of champions and countries they come from."""
    champion_to_wins = {}
    countries = set()

    for record in wimbledon_records:
        if record[2] in champion_to_wins:
            champion_to_wins[record[2]] += 1
        else:
            champion_to_wins[record[2]] = 1
            countries.add(record[1])

    return champion_to_wins, countries


def display_champions(champion_to_wins, countries):
    """Displays champions, their number of wins, and the countries that have won wimbledon."""
    number_of_countries = len(countries)
    winning_countries = ", ".join(sorted(countries))

    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")
    print(f"These {number_of_countries} countries have won Wimbledon:")
    print(f"{winning_countries}")


main()
