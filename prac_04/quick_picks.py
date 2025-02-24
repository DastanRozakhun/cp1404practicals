import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    pick = []
    while len(pick) < NUMBERS_PER_LINE:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in pick:
            pick.append(num)
    pick.sort()
    print(" ".join(f"{num:2}" for num in pick))
