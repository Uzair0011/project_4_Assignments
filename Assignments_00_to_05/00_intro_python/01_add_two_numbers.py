# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

print("01_add_two_numbers")


def add():
    print("This application for add two numbers")
    first_number = int(input("Enter your first number "))
    second_number = int(input("Enter your second number "))
    total = int(first_number + second_number)
    print(f"the total sum of  {first_number} and {second_number} is {total}")


if __name__ == "__main__":
    add()
