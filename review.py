print("Hello")

weekday = "Monday"

year = 2020

day = 9
day = str(day)
month = "November"
print(weekday + ",", month, day + ",", year)
print()

allowance = 5.5
print("My chocolate allowance is", allowance, "pieces")

colors = [
  "Blue",
  "Red",
  "Purple",
  "Green"
]
size = len(colors)

print("There are", size, "colors to choose from.")

import random
index = random.randint(0,size-1)
#print(index)
print("Your color today is number", str(index) + ",", colors[index])

for index_colors in range(colors, index):
  if index_colors < index:
    print("I like that color.")
  else colors[index] = size
    print("That color is okay too.")
