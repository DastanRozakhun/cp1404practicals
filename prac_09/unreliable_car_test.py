from unreliable_car import UnreliableCar

def main():
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Not So Reliable", 100, 30)

    reliable_success = 0
    unreliable_success = 0
    test_runs = 100

    for _ in range(test_runs):
        if reliable_car.drive(1) > 0:
            reliable_success += 1
        if unreliable_car.drive(1) > 0:
            unreliable_success += 1

    print(f"Reliable car succeeded {reliable_success} times out of {test_runs}")
    print(f"Unreliable car succeeded {unreliable_success} times out of {test_runs}")

if __name__ == "__main__":
    main()
