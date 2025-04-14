from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_menu():
    """Display the main menu options."""
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    """Display available taxis with their details."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Let the user choose a taxi from the list."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(taxi):
    """Drive the selected taxi and calculate the fare."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0
    
    try:
        distance = float(input("Drive how far? "))
        if distance <= 0:
            print("Distance must be > 0")
            return 0.0
        
        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        taxi.start_fare()  # Reset for next trip
        return fare
    except ValueError:
        print("Invalid distance")
        return 0.0


def main():
    """Run the taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    
    current_taxi = None
    bill_to_date = 0.0
    
    print("Let's drive!")
    
    while True:
        print(f"Bill to date: ${bill_to_date:.2f}")
        display_menu()
        choice = input(">>> ").lower()
        
        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            fare = drive_taxi(current_taxi)
            bill_to_date += fare
        else:
            print("Invalid option")
    
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == '__main__':
    main()
