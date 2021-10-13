"""Textbased adventure game. https://alissa-huskey.github.io/python-class/exercises/adventure.html 
continue with 2.3 D

"""

from pprint import pprint
from sys import stderr

# from console import fg, bg, fx

DEBUG = True
PLAYER = {
    "place": "home"
}

ITEMS = {
    "crystal ball": {
        "key": "crystal ball",
        "name": "it glows faintly",
        "description": "all it does is glow faintly; could be used in dark places",
        "price": -5,
    },
    "short dagger": {
        "key": "short dagger",
        "name": "antler handle with double edged blade",
        "description": "hardened steel, the blade is sharp on both sides, polished antler bone handle, about 10 inches in length, comes with a sheath",
        "price": -22,
    },
}

PLACES = {
    "home": {
        "key": "home",
        "name": "Sweet Cabin ",
        "east": "town-square",
        "description": "a cozy cabin nestled in the tall fir and pine trees",
    },
    "town-square": {
        "key": "town-square",
        "name": "Old Towne Square",
        "west": "home",
        "description": "A square with shops on all sides. The square has brick pavers with trees in front of the shops."
    },
}

def debug(message):
    if DEBUG == True:
        print("Debug: ", message)

def error(message):
    print("Error: ", message)

def do_shop():
    print("Items for sale")
    for k, item in ITEMS.items():
        print(k, item["name"], item["description"])
    
def do_go(args):
    print("Trying to go: ", args)

def do_quit():
    print("Goodbye!")
    quit()

def main():
    debug("Hello")
    print("Welcome!")
    while True:
        reply = input(">").strip()
        args = reply.split()
        if not args:
            continue
        command = args.pop(0) 
        debug(f"command: {command}")
        if command == "quit":
            do_quit()
        elif command == "shop":
            do_shop()
        elif command == "g" or command == "go":
        # elif command in ("g", "go"):
            do_go(args)
        else:
            print("No such command.")
            continue
      

if __name__ == "__main__":
    main()
    
