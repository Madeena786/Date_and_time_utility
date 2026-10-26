\# Date and Time Utility



\##  Project Title



\*\*Date and Time Utility using Python\*\*



\##  Description



This project is a Python-based Date and Time Utility developed using the built-in `datetime` module.



The program provides different operations for working with dates and time, such as calculating age, finding the number of days between two dates, calculating working days, displaying the current date and time, and checking whether a year is a leap year.



The project also includes input validation to handle invalid dates and years.



\##  Objective



The main objective of this project is to learn and practice practical date and time manipulation using Python's `datetime` module.



\##  Technologies Used



\- Python

\- datetime module



\##  Project File



```text

date\\\_utility.py

```



\##  Features



The program provides the following operations:



1\. Calculate Age

2\. Calculate Days Between Two Dates

3\. Calculate Working Days

4\. Display Current Date and Time

5\. Check Leap Year

6\. Exit the Program



\##  Python Concepts Used



\- Functions

\- User input

\- Conditional statements

\- `try-except`

\- `datetime`

\- `date`

\- `timedelta`

\- `strptime()`

\- `strftime()`

\- `weekday()`

\- Loops

\- Menu-driven programming

\- Date validation



\##  Python Modules Used



The project uses:



```python

from datetime import datetime, date, timedelta

```



\### datetime



Used for converting and working with date and time values.



\### date



Used to get the current date.



\### timedelta



Used to add or calculate differences between dates.



\##  How to Run



\### Step 1



Make sure Python is installed on your computer.



Check Python using:



```text

python --version

```



\### Step 2



Save the program as:



```text

date\\\_utility.py

```



\### Step 3



Open Command Prompt or Terminal in the project folder.



\### Step 4



Run:



```text

python date\\\_utility.py

```



\##  Program Menu



```text

==========================================

\&#x20;         DATE AND TIME UTILITY

==========================================

1\\. Calculate Age

2\\. Days Between Two Dates

3\\. Calculate Working Days

4\\. Current Date and Time

5\\. Check Leap Year

6\\. Exit

==========================================

```



\##  Sample Calculations



\### 1. Calculate Age



Input:



```text

Enter your date of birth (YYYY-MM-DD): 2005-05-16

```



Output:



```text

Date of Birth: 2005-05-16

Today's Date: 2026-10-26

Your Age: 21 years

```



\### 2. Days Between Two Dates



Input:



```text

Enter first date (YYYY-MM-DD): 2004-07-12

Enter second date (YYYY-MM-DD): 2005-05-16

```



Output:



```text

First Date: 2004-07-12

Second Date: 2005-05-16

Days Between: 308

```



\### 3. Working Days



Input:



```text

Enter start date (YYYY-MM-DD): 2025-10-12

Enter end date (YYYY-MM-DD): 2026-10-26

```



Output:



```text

Start Date: 2025-10-12

End Date: 2026-10-26

Working Days: 271

```



The program counts Monday to Friday as working days and excludes Saturday and Sunday.



\### 4. Leap Year



Input:



```text

Enter a year: 2005

```



Output:



```text

2005 is not a leap year.

```



Another example:



```text

Enter a year: 2004

2004 is a leap year.

```



\##  Input Validation



The program handles invalid input using `try-except`.



For example, if the user enters an incorrect date format:



```text

Invalid date.

Please enter date in YYYY-MM-DD format.

```



If the user enters an invalid menu option:



```text

Invalid choice.

Please select a number from 1 to 6.

```



\##  What I Learned



Through this project, I learned:



\- How to work with dates in Python

\- How to calculate age

\- How to find the difference between dates

\- How to calculate working days

\- How to format date and time

\- How to check leap years

\- How to validate user input

\- How to use Python's `datetime` module

\- How to create a menu-driven Python application



\##  Future Enhancements



The project can be improved by adding:



\- Holiday calculation

\- Countdown between dates

\- Add or subtract days from a date

\- Time zone conversion

\- Working hours calculation

\- Save results to a file

\- Graphical user interface

