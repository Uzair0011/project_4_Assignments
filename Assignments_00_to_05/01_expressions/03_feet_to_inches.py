# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

print("03_feet_to_inches")

inch: int = 12


def foot():
    feet: int = int(input("Enter Feet and i will convert into inches: "))
    print(f'There are {inch * feet} inches in {feet}.')


if __name__ == "__main__":
    foot()
