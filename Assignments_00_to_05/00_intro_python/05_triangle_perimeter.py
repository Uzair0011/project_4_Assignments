# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

print("05_triangle_perimeter")


def triangle():
    print("This code is about perimeter of triangle. ")
    side1: float = float(input("Enter your first side number of triangle: "))
    side2: float = float(input("Enter your second side number of triangle: "))
    side3: float = float(input("Enter your third side number of triangle: "))
    total: float = float(side1+side2+side3)
    print(f'The sum of {side1},{side2},{side3} is {total}')


if __name__ == "__main__":
    triangle()
