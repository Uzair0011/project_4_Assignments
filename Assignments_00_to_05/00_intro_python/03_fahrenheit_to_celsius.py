print("03_fahrenheit_to_celsius")


def temp():
    print("This code for converting fahrenheit to celsius")
    farhenheit_degree = float(input("Enter your fahrenheight degree "))
    celsius_degree = (farhenheit_degree - 32) * 5.0/9.0
    print(f'Temperature {farhenheit_degree} = {celsius_degree}')


if __name__ == "__main__":
    temp()
