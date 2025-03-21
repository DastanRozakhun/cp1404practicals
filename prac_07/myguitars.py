from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Load, display, and sort guitars."""
    guitars = load_guitars(FILENAME)
    print("Loaded guitars:")
    display_guitars(guitars)
    
    guitars.sort()  # Sort using __lt__
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display guitars with vintage status."""
    for guitar in guitars:
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage}")

if __name__ == "__main__":
    main()
