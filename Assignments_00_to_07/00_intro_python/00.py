print("01_add_two_numbers")


def add():
    print("This application for add two numbers")
    first_number = int(input("Enter your first number"))
    second_number = int(input("Enter your second number"))
    total = int(first_number + second_number)
    print(f'the total sum of  {first_number} and {second_number} is {total}')


if __name__ == "__main__":
    add()
