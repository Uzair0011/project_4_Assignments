# Simulate rolling two dice, and prints results of each roll as well as the total.

import random
print("06_rolldice")


def dice():
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    total: int = int(die1 + die2)
    print("First die: " + str(die1))
    print("Second die: " + str(die2))
    print(f'Total of two dies: {total}')


if __name__ == "__main__":
    dice()
