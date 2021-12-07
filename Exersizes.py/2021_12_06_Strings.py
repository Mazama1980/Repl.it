""" Strings: Splitting and Joining Exercise 58
       1. Take the quote of your choice and assign it to the variable quote. Split it into a list of words (seperated by whitespace) and print the result.

       2. Assign this string to the variable flavors:
        "banana split;hot fudge;cherry;malted;black and white"
        Split it into a list on the deliter ";".

       3. Look up the word of the day and assign it to the variable word. Convert it to a list of characters and print it.

       4.Make a list with every letter in the current day of the week and assign it to the variable day. Turn it into a string (join it using a blank string as the delimiter) and print it.

       5.Make a list of three dinosaurs. Join it on a newline delimiter then print it.

"""
"""2021-12-06 Fundamentals -- Strings Review, Joining and Splitting

Attendance
----------
- Nila
"""

# raw strings and backslashes

r"What kind of string is this?"

print("line one\nline two")

path = "C:\\Documents\\Nodes"
print(path)

path = r"C:\Documents\Nodes"
print(path)

# f-strings

day = "Friday"
print(f"Happy {day}!")

# concatenation

color = "red"
print("Roses are " + color)

print("For he's a jolly good fellow\n" * 3 )

# splitting and joining

line = "Monday: Fundamentals"

line = "Wednesday: Data and More"
words = line.split()

weekday = words.pop(0)

# weekday = weekday[:-1]
weekday = weekday.rstrip(":")
class_name = " ".join(words)

print(repr(weekday), repr(class_name))

password = "abc123"
letters = list(password)
letters[0] = letters[0].upper()
letters.append("!")
better_password = "".join(letters)
print(better_password)






quote = "Whether you think you can or you think you can't; You're right."
quoteable = quote.split()
print(quoteable)
print("~" * 20)

flavors = "banana split;hot fudge;cherry;malted;black and white"
flavorite = flavors.split(";")
print(flavorite)
print("~" * 20)

word = "eysome"
day_word = list(word)
print(day_word)
print("~" * 20)

day = ["m", "o", "n", "d", "a", "y"]
still_day = "".join(day)
print(still_day)
print("~" * 20)

dinosaurs = ["stegosaurus", "triceratops", "velociraptor"]
dino = "\n".join(dinosaurs)
print(dino)
