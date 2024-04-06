"""
Pypet Game

    From the tutorial found at:

    https://alissa-huskey.github.io/python-class/lessons/tutorial.html
"""

# print to the screen by calling the print() function
print("Welcome to Pypet!")
# create variables with values for the pypet ie. name, age, etc.
# name = "Fluffy"
# age = 5
# weight = 9.5
# hungry = False
# color = "purple"
# pic = "(=^o.o^=)__"
# defining (or creating) a feed function
# create a dictionary with key:value pairs for an object (cat, mouse)
cat = {
    "name": "Fluffy",
    "age": 5,
    "weight": 9.5,
    "hungry": True,
    "color": "purple",
    "pic": "(=^o.o^=)__",
}
mouse = {
   "name": "Mouse",
   "age": 6,
   "weight": 1.5,
   "hungry": False,
   "pic": "<:3 )~~~~",
}
# make a list of the dictionary items cat and mouse
pets = [cat, mouse,
        ]
def feed(pet):
    if pet["hungry"] == True:
     print("I'm hungry")
     pet["hungry"] = False
     # add weight to the cat by one increment
     cat["weight"] = cat["weight"] + 1
    else:
       print("The Pypet,", (cat["name"]), "is not hungry right now.")
    # breakpoint()

# concatonate a string with a variable
print("Hello from " + cat["name"] + " and " + mouse["name"])
# print picture by calling the variable rather than printing the value (print("(=^o.o^=)__"))
print(cat["pic"],   mouse["pic"])
# print a debug statement before to make sure the feed function works
print("Before feeding:", (cat["weight"]),"lbs,", (cat["hungry"]))
# call the feed function to add weight to the cat after it eats
feed(cat)
# print a debug statement after to make sure the feed function works
print("After feeding:", (cat["weight"]),"lbs,", (cat["hungry"]))

for pet in pets:
    feed(pet)
    print(pet)
       
def hello():
    print("Hello World!")
hello()

def goodbye(name):
    print(f"Goodbye {name}!")

goodbye("Nila")
