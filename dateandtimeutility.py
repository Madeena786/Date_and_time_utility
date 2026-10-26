from datetime import datetime, date, timedelta
def calculate_age():
    print("\n========== CALCULATE AGE ==========")
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
        today = date.today()
        if dob > today:
            print("Date of birth cannot be in the future.")
            return
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age = age - 1
        print("Date of Birth:", dob)
        print("Today's Date:", today)
        print("Your Age:", age, "years")
    except ValueError:
        print("Invalid date.")
        print("Please enter date in YYYY-MM-DD format.")
def days_between_dates():
    print("\n====== DAYS BETWEEN TWO DATES ======")
    first_input = input("Enter first date (YYYY-MM-DD): ")
    second_input = input("Enter second date (YYYY-MM-DD): ")
    try:
        first_date = datetime.strptime(first_input, "%Y-%m-%d").date()
        second_date = datetime.strptime(second_input, "%Y-%m-%d").date()
        difference = abs((second_date - first_date).days)
        print("First Date:", first_date)
        print("Second Date:", second_date)
        print("Days Between:", difference)
    except ValueError:
        print("Invalid date.")
        print("Please enter date in YYYY-MM-DD format.")
def calculate_working_days():
    print("\n========== WORKING DAYS ==========")
    start_input = input("Enter start date (YYYY-MM-DD): ")
    end_input = input("Enter end date (YYYY-MM-DD): ")
    try:
        start_date = datetime.strptime(start_input, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_input, "%Y-%m-%d").date()
        if start_date > end_date:
            print("Start date cannot be after end date.")
            return
        working_days = 0
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() < 5:
                working_days += 1
            current_date += timedelta(days=1)
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Working Days:", working_days)
    except ValueError:
        print("Invalid date.")
        print("Please enter date in YYYY-MM-DD format.")
def current_datetime():
    print("\n====== CURRENT DATE AND TIME ======")
    now = datetime.now()
    print("Current Date and Time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Formatted Date:")
    print(now.strftime("%d-%m-%Y"))
    print("Formatted Date with Month Name:")
    print(now.strftime("%B %d, %Y"))
    print("Day:")
    print(now.strftime("%A"))
    print("Time:")
    print(now.strftime("%H:%M:%S"))
def check_leap_year():
    print("\n========== LEAP YEAR CHECK ==========")
    year_input = input("Enter a year: ")
    try:
        year = int(year_input)
        if year % 400 == 0:
            print(year, "is a leap year.")
        elif year % 100 == 0:
            print(year, "is not a leap year.")
        elif year % 4 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    except ValueError:
        print("Please enter a valid year.")
while True:
    print("\n")
    print("==========================================")
    print("          DATE AND TIME UTILITY")
    print("==========================================")
    print("1. Calculate Age")
    print("2. Days Between Two Dates")
    print("3. Calculate Working Days")
    print("4. Current Date and Time")
    print("5. Check Leap Year")
    print("6. Exit")
    print("==========================================")
    choice = input("Enter your choice: ")
    if choice == "1":
        calculate_age()
    elif choice == "2":
        days_between_dates()
    elif choice == "3":
        calculate_working_days()
    elif choice == "4":
        current_datetime()
    elif choice == "5":
        check_leap_year()
    elif choice == "6":
        print("\nThank you for using Date and Time Utility!")
        print("Program ended.")
        break
    else:
        print("\nInvalid choice.")
        print("Please select a number from 1 to 6.")



