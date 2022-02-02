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
print(f"The last solar eclipse in the USA was {count_years} years and {count_months} days ago.")

"""
2022-01-31

Agenda
------

* Expression exercise
* Problem solving exercise


"""

"""from workshops import section, div, stop, exercise

    section("A", "Expression Exercises")"""

# order of operation rules
#
# - replace variables with values
# - */ before +-
# - inside to out
# - left to right
# - and before or
#

from pathlib import Path

DEFAULT_CONFIG_DIR = Path.home() / "python_class_config"

options = {
    "url": "https://github.com/alissa-huskey/python-class"
}

options.get("config_dir", DEFAULT_CONFIG_DIR).name.replace("_", " ").title()
# options.get("config_dir", Path.home() / "python_class_config").name.replace("_", " ").title()
# options.get("config_dir", Path("/Users/alissa") / "python_class_config").name.replace("_", " ").title()
# options.get("config_dir", Path("/Users/alissa/python_class_config")).name.replace("_", " ").title()
# Path("/Users/alissa/python_class_config").name.replace("_", " ").title()
# "python_class_config".replace("_", " ").title()
# "python class config".title()
"Python Class Config"

# ----------------------------------------------------------

"""section("B", "Review datetimes")

    div("B.1", "get the current date and time")"""

from datetime import datetime
present = datetime.today()
print(present)

"""div("B.2", "add or subtract a timedelta to/from that datetime object")"""

from datetime import timedelta
hour = timedelta(hours=1)
future = present + hour
print(future)


"""div("B.3", "get a property from a datetime object")"""

print(future.day)

"""section("3", "Exercise")

div("3.1", "Print the schedule for today")

# Print every hour of the day in 12 hour format with AM/PM
# If there is an activity for that hour on your schedule,
#     print it after the hour
# 
# For example:
#
#  8 AM  Breakfast
# 12 PM  Lunch
#  6 PM  Dinner
# 
# Use datetime and time delta objects, and iterate using a for loop."""
#

schedule = {
    8: "Pilates",
    9: "yoga",
    11: "Brunch",
    16: "Dinner",
    17: "Coding Class",
    21: "Date night",
}


day = datetime.today()
hours = timedelta(hours=1)

# 18
    
    










"""8>>> today
datetime.datetime(2022, 1, 31, 19, 6, 5, 148849)

9>>> today.replace(hours=12)
---------------------------------------------------------------------------

10>>> today.replace(hour=12)
datetime.datetime(2022, 1, 31, 12, 6, 5, 148849)

11>>> today.replace(hour=12, minute=0, second=0, microsecond=0)
datetime.datetime(2022, 1, 31, 12, 0)

12>>> today.replace(hour=13, minute=0, second=0, microsecond=0)
datetime.datetime(2022, 1, 31, 13, 0)

13>>> 20 - 12
8"""
