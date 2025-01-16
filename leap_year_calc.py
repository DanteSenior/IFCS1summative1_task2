def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    try:
        year = int(input("Please enter a year: "))
        if is_leap_year(year):
            print(year, "Is a leap year.")
        else:
            print(year, "Is not a leap year.")
    except ValueError:
        print("Please enter a valid year")