def main():
    score = get_valid_score()
    
    while True:
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").strip().upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(determine_result(score))
        elif choice == 'S':
            print('*' * int(score))
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice")

def get_valid_score():
    while True:
        try:
            score = int(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
