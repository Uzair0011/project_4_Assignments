# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

print("06_seconds_in_year")

days_in_year: int = 365
hours_per_year: int = 24
minutes_per_hour: int = 60
seconds_per_minute: int = 60


def seconds():
    print(
        f'There are {days_in_year * hours_per_year * minutes_per_hour * seconds_per_minute} seconds in a year')


if __name__ == "__main__":
    seconds()
