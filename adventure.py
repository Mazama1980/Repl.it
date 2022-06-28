"""Textbased adventure game. https://alissa-huskey.github.io/python-class/exercises/adventure.html 

[x] Write a test for the place_add() function
[x] continue with 9.6A...
[x] write annotations and docstrings for two functions
[x] continue with 9.6B

[x] Write a test for the place_remove() function
[x] continue with 9.6A...


future to learn / do
[ ] add annotations to all functions
[ ] write docstrings for all functions
"""

from pprint import pprint
from sys import stderr
import textwrap
from console import fg, bg, fx

WIDTH = 60
MARGIN = 2
DEBUG = True
PLAYER = {
    "place": "home",
    "inventory": {},
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
        "can_take": True,
    },
    "desk": {
        "key": "desk",
        "name": "writing desk",
        "description": "A smallish wooden desk with 5 drawers. There is a large book laying on the top.",
    },
    "stick": {
        "key": "stick",
        "name": "walking stick",
        "description": "a staff made from osage orange. It's about 4 feet tall. It has curious carvings on it.",
        "can_take": True,
    },
    "bag": {
        "key": "bag",
        "name": "a bag",
        "description": "A bag made of rough cloth that appears to be strong. It is about 12 inches long and 8 inches wide.",
        "can_take": True,
    }
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
        "items": ["book", "desk", "stick", "bag"],
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

def get_place(key: str =None) -> dict:
    """Getting (returns the current place) where the Player is at currently at in the game"""
    # Getting the current Player place if there is no key 
    if not key:
        key = PLAYER["place"]
    # Making sure that the key is in the PLACES dictionary
    place = PLACES.get(key)
    if not place:
        abort(f"Woops! The information about the place {key} seems to be missing.")
    return place

def get_item(key: str) -> dict:
    """Getting (or returning) an item from the ITEMS dictionary"""
    item = ITEMS.get(key)
    if not item:
        abort(f"Woops! The information about the item {key} seems to be missing.")
    return item

def player_has(key: str, qty: int=1) -> bool:
    """Determining (return True/False) if there is an item in the PLAYER inventory"""
    if key in PLAYER["inventory"] and PLAYER["inventory"][key] >= qty:
        return True
    else:
        return False

def inventory_change(key: str, quantity: int=1):
    """Add item to player inventory"""
    PLAYER["inventory"].setdefault(key,0)
    PLAYER["inventory"][key] += quantity
    # Remove from inventory dictionary if quantity is zero
    if not key in PLAYER["inventory"] or quantity <= 0:
        PLAYER["inventory"].pop(key)

def place_has(item_key: str) -> bool:
    """"Return True if the place dictionary for the players current place
        contains item_key in its "items" list, otherwise return False.

        Args:
        * item_key (str): Key from the ITEMS dictionary to look for in the place
          "items" list
        """
    place = get_place()
    if item_key in place.get("items", []):
        return True
    else:
        return False

def place_add(key: str):
    """Add an item to a current place"""
    # Get the current place
    place = get_place()

    # Add the item key to the current place items list
    place.setdefault("items", [])
    if key not in place["items"]:
        place["items"].append(key)


def do_inventory():
    """Listing the Player's current inventory. Called when the player types the
    "inventory" or "i" command. """
    debug("Trying to show inventory.")
    header("Inventory")
    # If the Player's inventory is empty then print the message "Empty"
    if not PLAYER["inventory"]:
        write("Empty")
    # Listing the Player's item name with the quantity of each item
    for name, qty in PLAYER["inventory"].items():
        item = get_item(name)
        write(f'{qty}, {item["name"]}')
    print()

def do_shop():
    """Listing items that are for sale by using the "shop" command."""
    header("Items for sale")
    for k, item in ITEMS.items():
    # Checking to see if an item can be purchased with the is_for_sale() function
        if not is_for_sale(item):
            continue
        write(f'{k}--> {item["name"]}')

def is_for_sale(item: dict) -> bool:
    """Checking (returning True or False) to see if an item has a price attached to it"""
    if "price" in item:
        return True
    else:
        return False

def do_examine(args: list):
    """Player can examine an item using the 'x', 'exam' or 'examine' command"""
    debug(f'Trying to examine {args}')
    if not args:
        error("What do you want to exam?")
        return
    #Checking if the current place of the player has the item or the player has the item.
    place = get_place()
    name = args[0].lower()
    items = place.get("items", [])
    if not place_has(name) or player_has(name):
       abort(f"Sorry, I don't know what this is:{name}")
    #Listing the item and description for the player.
    item = get_item(name)
    header(item["name"])
    wrap(item["description"])

def do_take(args):
    """Player can take an item and add it to their inventory using the 't',
    'take' or 'grab' command"""
    debug(f"Trying to take {args}.")
    if not args:
        error("What are you trying to take?")
        return
    #Checking if the current place of the player has the item
    place = get_place()
    name = args[0].lower()
    if not place_has(name):
        error(f"Sorry, I don't see a {name} here.")
        return
    #Checking if the item is available to take by the player
    item = get_item(name)
    if not item.get("can_take"):
        wrap(f"You try to pick up {item['name']}, but you find you aren't able to lift it.")
        return
    #Removing the item from the current place
    place["items"].remove(name)
    #Adding the item to the player's inventory
    inventory_change(name)

    wrap(f"You pick up {name} and put it in your pack.")


def do_look():
    debug(f"Trying to look around.")
    place = get_place()
    header(place["name"])
    wrap(place["description"])
    items = place.get("items", [])
    if items:
        names = []
        for key in items:
            item = get_item(key)
            names.append(item["name"])
        
        # remove the last item from names and save it for later
        last = names.pop()

        # make text a comma seperated list of all names except the last
        text = ", ".join(names)

        # if text has any items, add the word " and "
        if text:
            text = text + " and " 
        
        # add the last item
        text = text + last

        print()
        write(f"You see {text}. \n")
    print()
    directions = ["north", "east", "south", "west"]
    for direction in directions:
        name = place.get(direction)
        if not name:
            continue
        destination = get_place(name)
        write(f"To the {direction} is {destination['name']}.")

def do_drop(args):
    debug(f'Trying to drop {args}')
    if not args:
        error("What do you want to drop?")
        return
    name = args[0].lower()
    if not player_has(name):
        error(f"You don't have any {name}.")
        return
    # NOTE -= is shorthand for:
    # PLAYER["inventory"][name] = PLAYER["inventory"][name] - 1
    PLAYER["inventory"][name] -= 1
    if not PLAYER["inventory"][name]:
        PLAYER["inventory"].pop(name)
    place_add(name)
    wrap(f'You set down the {name}')
    ...
             
def wrap(text):
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent = MARGIN * " ",
        subsequent_indent = MARGIN * " "
    )
    print(paragraph)
    print()

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
    old_place = get_place()
    new_name = old_place.get(direction)
    if not new_name:
        error(f"Sorry, you can't go {direction} from here.")
        return
    new_place = get_place(new_name)
    PLAYER["place"] = new_name
    header(new_place["name"])
    wrap(new_place["description"])


def do_quit():
    write(fg.lightyellow("Goodbye!"))
    quit()

def abort(message):
    error(message)
    exit(1)


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
        elif command in ("t", "take", "grab"):
            do_take(args)
        elif command in ( "i", "inventory"):
            do_inventory()
        elif command == "drop":
            do_drop(args)
        else:
            error("No such command.")
            continue
      

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        ...
    
