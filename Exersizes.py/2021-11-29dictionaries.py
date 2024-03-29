"""Exercise 43 (Shapes Dictionary)

Create a dictionary assigned to the variable shapes that uses shape names (like "square" or "triangle") for keys and the number of sides (like 4 and 3) for values.

Print the dictionary. https://alissa-huskey.github.io/python-class/lessons/data-types/dictionaries.html#conditions"""

def objects():
    shapes= {
        "triangle": 3,
        "square": 4,
        "rectangle": 4,
        "pentagon": 5,
        "hexagon": 6,
        "octogon": 8,

    }
    # print("A square has", shapes["square"], "sides.")
    # print("A rectangle has", shapes["rectangle"], "sides.")
    answer = input("What shape would you like to know the number of sides for it? ")
    sides = shapes.get(answer)
    if sides:
        print("The shape", answer, "has", sides, "sides.")
    else:
        print("Sorry I do not know that shape:", answer)
#objects()

"""2021-11-29 

Attendees
- Nila
- Sean

"""

#######################################################################
# Order of Operation Rules
#
# - replace variables with values
# - */ before +-
# - inside to outside
# - left to right (except before =)
#
# Expression - any piece of code that evaluates to a value
#
#######################################################################

# 1. Make a list of seasons (lowercase). Print the first three characters of the 3rd season, title cased.
# 2. Make a dictionary where the key is the numbers 1-7 and the value is the days of the week: monday - sunday.
#    - Write a function that takes one argument, a number, and returns the day of the week associated with that number.
# 3. Make a dictionary named schedule where the key is a weekday and the value is another dictionary. 
#    - The inner dictionary should be the schedule for the day, where the key is the time in 24 hour format (ie: "14:30")
#      and the value is the thing scheduled
#    - Use a for loop to iterate over each day and print the day name,
#    - then use a nested for loop to iterate over the schedule and print the time and activity

def year():
    seasons = ["spring", "summer", "fall", "winter"]
    season = seasons[2][0:3].capitalize()
    print(season)
year()

weekdays = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
}
def days(day_number):
    day = weekdays[day_number]
    return day
    
print(days(5))

schedule = {
    "Monday": {
        "09:00": "Yoga",
        "17:00": "QCC Class",
        },
    "Tuesday": {
        "7:00": "Eliptical",
        "17:00": "QCC Class",
    }
}


"""
2022-01-03 -- Fundamentals: Datetime Objects

Attendees
---------
- Nila

See also
--------
* Format Codes: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

Agenda
------
- Expression exercises
"""


##################################################################################################################
# Expression exercises
# --------------------
#
# Order of operation rules:
# - replace variable names with values
# - left to right
# - inside to outside
# - */ before +-
# - and before or
#
##################################################################################################################

player = {"inventory": {"coins": 8}}

item = "sword"
qty = player.get("inventory", {}).get(item, 0)

print(f"You have {qty} {item}s.")

# player.get("inventory", {}).get(item, 0)
# player.get("inventory", {}).get("sword", 0)
# {"inventory": {"coins": 8}}.get("inventory", {}).get("sword", 0)
# {"coins": 8}.get("sword", 0)
# 0

# syntax meanings for parenthesis: 
#   description                                          example                  syntax
# - call functions, methods, types (str, int)            print(...)               callable_name(optional_arguments, args)
# - grouping and order of operation                                               (expression)
# - tuples                                               (1, 2, 3)                (value, value, ...)