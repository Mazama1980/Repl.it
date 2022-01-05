"""Textbased adventure game. https://alissa-huskey.github.io/python-class/exercises/adventure.html 
continue with 5.3A1: Exmine Items

"""

from pprint import pprint
from sys import stderr
import textwrap
from console import fg, bg, fx

WIDTH = 60
MARGIN = 2
DEBUG = True
PLAYER = {
    "place": "home"
}

ITEMS = {
    "crystal ball": {
        "key": "crystal ball",
        "name": "it glows faintly -",
        "description": "all it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "short dagger": {
        "key": "short dagger",
        "name": "antler handle with double edged blade",
        "description": "hardened steel, the blade is sharp on both sides, polished antler bone handle, about 10 inches in length, comes with a sheath",
        "price": -22,
    },
    "green potion": {
        "key": "green potion;",
        "name": "a health potion; ",
        "description": "it will return half your life",
        "price": -30,
    },
    "book": {
        "key": "book",
        "name": "Diary of a flying squirrel",
        "description": "A soft leather bound book laying on the desk at home. There may be useful information in it.",
    },
    "desk": {
        "key": "desk",
        "name": "writing desk",
        "description": "A smallish wooden desk with 5 drawers. There is a large book laying on the top.",
    },
}

#############################################
# Map
# -------------------------------------------
#               lake
#                \
#              home <-> town-square
#                /
#              woods
#
#
#############################################

PLACES = {
    "home": {
        "key": "home",
        "name": "Sweet Cabin ",
        "east": "town-square",
        "south": "woods",
        "north": "lake",
        "description": "a cozy cabin nestled in the tall trees",
        "items": ["book", "desk"],
    },
    "town-square": {
        "key": "town-square",
        "name": "Old Towne Square",
        "west": "home",
        "description": "A square with shops on all sides. The square has brick pavers with trees in front of the shops."
    },
    "woods": {
        "key": "woods",
        "name": "Deep, dark woods",
        "north": "home",
        "description": "A deep forest of Redwood trees. Ferns and bushs growing on the forest floor. A path running through it. It's quiet and peaceful." 
    },
    "lake": {
        "key": "lake",
        "name": "Lake Pukaki",
        "south": "home",
        "description": "Deep blue in color but will change to a purple hue when its mood is unsettled. There are mysteries to be found in it's dark waters."
    },
}

def debug(message):
    if DEBUG == True:
        debug_color = fg.blue + bg.green
        print(debug_color("Debug:"), message)

def error(message):
    style = fg.white + bg.red
    print(style("Error:"), message)

def do_shop():
    header("Items for sale")
    for k, item in ITEMS.items():
        if "price" not in item:
            continue
        write(f'{k}--> {item["name"]}')

def do_examine(args):
    debug(f'Trying to examine {args}')
    if not args:
        error("What do you want to exam?")
        return
    place_name = PLAYER["place"]
    place = PLACES[place_name]
    name = args[0].lower()
    items = place.get("items", [])
    if name not in items:
       error(f"Sorry, I don't know what this is:{name}")
       return
    item = ITEMS[name]
    header(item["name"])
    wrap(item["description"])
    
def do_look():
    debug(f"Trying to look around.")
    place_name = PLAYER["place"]
    place = PLACES[place_name]
    header(place["name"])
    wrap(place["description"])
    items = place.get("items", [])
    
def wrap(text):
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent = MARGIN * " ",
        subsequent_indent = MARGIN * " "
    )
    print(paragraph)

def write(text):
    print(f"{MARGIN * ' '} {text}")

def header(title):
    print()
    header_title = fx.bold(title)
    write(header_title)
    print()
    
def do_go(args):
    debug(f"Trying to go: {args}")
    if not args:
        error("Which way do you want to go?")
        return
    direction = args[0].lower()
    compass = ["north", "south", "east", "west"]
    if direction not in compass:
        error(f"sorry, I don't know how to go : {direction}")
        return
    old_name = PLAYER["place"]
    old_place = PLACES[old_name]
    new_name = old_place.get(direction)
    if not new_name:
        error(f"Sorry, you can't go {direction} from here.")
        return
    new_place = PLACES.get(new_name)
    if not new_place:
        error(f"Woops! The information about {new_name} seems to be missing.")
        return
    PLAYER["place"] = new_name
    header(new_place["name"])
    wrap(new_place["description"])


def do_quit():
    write(fg.lightyellow("Goodbye!"))
    quit()


def main():
    debug("Hello")
    header(fg.lightyellow("Welcome!"))
    while True:
        debug(f"You are at: {PLAYER['place']}")
        reply = input(">").strip()
        args = reply.split()
        if not args:
            continue
        command = args.pop(0)
        # .pop(0) removes the first element from the list
        debug(f"command: {command}")
        debug(f"command: {args}")
        if command in ("q", "quit"):
            do_quit()
        elif command == "shop":
            do_shop()
        elif command in ("g", "go"):
            do_go(args)
        elif command in ("x", "exam", "examine"):
            do_examine(args)
        elif command in ("l", "look"):
            do_look()
        else:
            error("No such command.")
            continue
      

if __name__ == "__main__":
    main()
    
