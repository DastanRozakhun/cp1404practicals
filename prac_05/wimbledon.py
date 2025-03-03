"""
Wimbledon
Estimate: 45 minutes
Actual:   60 minutes
"""

import csv

def main():
    """Process Wimbledon data."""
    filename = 'wimbledon.csv'
    champions = []
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            champions.append(row[2])  # Champion name
            countries.add(row[1])    # Champion country

    champion_to_count = {}
    for champion in champions:
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()
