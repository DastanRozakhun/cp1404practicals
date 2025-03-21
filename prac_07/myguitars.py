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
    
    add_new_guitars(guitars)
    save_guitars(guitars, FILENAME)
    print("Guitars saved to file.")

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

def add_new_guitars(guitars):
    """Add new guitars via user input."""
    print("\nEnter new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.\n")

def save_guitars(guitars, filename):
    """Save guitars to a CSV file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
