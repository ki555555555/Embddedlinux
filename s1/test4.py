import calendar

def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

if __name__ == "__main__":
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        print_calendar(year, month)
    except ValueError:
        print("Invalid input. Please enter valid year and month.")
