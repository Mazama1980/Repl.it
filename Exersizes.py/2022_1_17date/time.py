"""
2022-01-17 Fundamentals

Attendees
---------
- Nila
- Sean
Link to follow and find this and other lessons:
https://github.com/alissa-huskey/python-class/tree/master/workshops

"""

################################################################################
# Dates and Times
################################################################################


# Exercises
# ---------
# 1. get the current date and time and assign it to a variable now then print it
# 2. get a datetime object for your birthday and print it

from datetime import datetime

now = datetime.today()
print(now)

birthday = datetime(1999, 12, 31)
print(birthday)
print(str(birthday))

# Exercises
# ---------
# 1. Print just the date of the current datetime object using the .date() method
# 2. Print just the time of the current datetime object using the .time() method
# 3. Print a sentence like:
#    The year of our lord YEAR, on the DAY day of the MONTHth month, something happened!
#    (Using the .year, .day, and .month properties.)

print(f"Today is {now.date()}.")
print(f"The current time is: {now.time()}.")
print(f"The year of our Lord {now.year}, on the {now.day} of the {now.month} month, I attended Alissa's coding class.")

# you can do math on timedelta objects

# workday 

# Exercises
# ---------
# 1. import timedelta type from the datetime module
# 2. make a timedelta for a year
# 3. multiply a year by ten to make a century

from datetime import timedelta
year = timedelta(days=365)
month = timedelta(weeks=4)
print(year)
decade = year * 10
century = year * 100
print(f"There are {decade} days in a decade and there are {century} days in a century.")


# Exercises
# ---------
# 1. Find out the date a week from now
# 2. Look up the date of the last solar eclipse. Print how many days it has been since then.
#    Bonus: Use timedelta objects to calculate how many years, months, and days it has been.

print(f"The date one week from today {now.date()} will be {now + timedelta(days=7)}.")
solar_eclipse = datetime(2017, 8, 21)
print(f"The last solar eclipse in the USA was {now - solar_eclipse}.")
total_solar = now - solar_eclipse
count_years = int(total_solar / year)
count_months = int((total_solar - (year * count_years)) / month)
print(f"The last solar eclipse in the USA was {count_years} years and {count_months} ago.")