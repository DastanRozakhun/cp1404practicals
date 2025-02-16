import random

# Smallest: 5, Largest: 20
print(random.randint(5, 20))  # line 1

# Smallest: 3, Largest: 9. No, it cannot produce 4.
print(random.randrange(3, 10, 2))  # line 2

# Smallest: 2.5, Largest: 5.5
print(random.uniform(2.5, 5.5))  # line 3

# Random number between 1 and 100
print(random.randint(1, 100))
