# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

print("06_square_number")


def square():
    print("This code is about square of given number")
    num1: int = int(
        input("Enter any number and i will give you a square value. "))
    print(f'The square of {num1} is {num1 ** 2}')


if __name__ == "__main__":
    square()
