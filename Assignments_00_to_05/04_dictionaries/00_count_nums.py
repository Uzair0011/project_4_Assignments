# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
print("00_count_nums")
def count_numbers():
    count_dict = {}

    while True:
        user_input = input("Enter a number (or type Exit to quit): ")

        if user_input.title() == "Exit":
            break

        if user_input.isdigit():
            num = int(user_input)
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Invalid input. Please enter a number or 'Exit'.")

    return count_dict


def display_counts(count_dict):
    print("\nNumber Counts:")
    for key, value in count_dict.items():
        print(f"{key} appears {value} times")


if __name__ == "__main__":
    counts = count_numbers()
    display_counts(counts)
