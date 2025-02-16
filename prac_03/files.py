# Part 1: Write name to file
name = input("Enter your name: ")
name_file = open('name.txt', 'w')
name_file.write(name)
name_file.close()

# Part 2: Read name from file
name_file = open('name.txt', 'r')
name = name_file.read()
print(f"Hi {name}!")
name_file.close()

# Part 3: Sum first two numbers
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
print(num1 + num2)

# Part 4: Sum all numbers
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print(total)
