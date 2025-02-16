def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    minimum_length = 5
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    print('*' * len(password))
    
main()
