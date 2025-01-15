def is_leap_year(year):
    """
    Determine if a given year is a leap year.

    A year is a leap year if it is divisible by 4, except for years that are 
    divisible by 100. However, years divisible by 400 are leap years.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    try:
        year = int(input("Please enter a year: "))
        if is_leap_year(year):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    except ValueError:
        print("Please enter a valid year.")
        
# new line
