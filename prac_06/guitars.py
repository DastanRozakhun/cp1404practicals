from guitar import Guitar

guitars = []
print("My guitars!")
while True:
    name = input("Name: ")
    if not name:
        break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} added. ({year}) : ${cost:,.2f} added.")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:>10,.2f}{vintage}")
