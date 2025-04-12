# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

print("05_remainder_division")


def remainder():
    num1: int = int(input("Enter an integar to be divided: "))
    num2: int = int(input("Enter an integar to divided by: "))
    quotient: int = num1//num2
    rem: int = num1 % num2
    print(rem)
    print(
        f"the result of this division is {quotient} + with a remainder of {rem}")


if __name__ == "__main__":
    remainder()
