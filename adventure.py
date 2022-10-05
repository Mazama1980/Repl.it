"""Textbased adventure game. https://alissa-huskey.github.io/python-class/exercises/adventure.html 

"""

from pprint import pprint
from sys import stderr
import textwrap
from console import fg, bg, fx
from shlex import split

WIDTH = 60
MARGIN = 2
DEBUG = True
PLAYER = {
    "place": "home",
    "inventory": {"gems": 50},

}

ITEMS = {
# Crystal Ball      faintly glowing ball       5
    "crystal ball": {
        "key": "crystal ball",
        "name": "Crystal ball",
        "summary": "a faintly glowing ball",
        "description": "all it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "new crystal ball": {
        "key": "crystal ball",
        "name": "Crystal ball",
        "summary": "a faintly glowing ball",
        "description": "all it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "short dagger": {
        "key": "short dagger",
        "name": "Short dagger",
        "summary": "double edged blade",
        "description": "hardened steel, the blade is sharp on both sides, polished antler bone handle, about 10 inches in length, comes with a sheath",
        "price": -22,
    },
    "green potion": {
        "key": "potion",
        "name": "Green potion",
        "summary": "a health potion ",
        "description": "it will return half your life",
        "price": -30,
    },
    "waybread": {
        "key": "waybread",
        "name": "Waybread",
        "summary": "food for travel",
        "description": "A bread like food that nourishes. It doesn't spoil so it works well for traveling.",
        "price": -5,
    },
    "fishing tackle": {
        "key": "tackle",
        "name": "Fishing tackle",
        "summary": "gear for catching fish",
        "description": "Gear needed for catching fish from streams and lakes. Hooks, lines, folding pole, bobbers, weights. It is all contained in its own bag.",
        "price": -10,
    },
    "book": {
        "key": "book",
        "name": "Book",
        "summary": "Diary of a wimpy dragon",
        "description": "A soft leather bound book laying on the desk at home. There may be useful information in it.",
        "can_take": True,
    },
    "desk": {
        "key": "desk",
        "name": "Desk",
        "summary": "writing desk",
        "description": "A smallish wooden desk with 5 drawers. There is a large book laying on the top.",
    },
    "stick": {
        "key": "stick",
        "name": "Stick",
        "summary": "walking stick",
        "description": "a staff made from osage orange. It's about 4 feet tall. It has curious carvings on it.",
        "can_take": True,
    },
    "bag": {
        "key": "bag",
        "name": "Bag",
        "summary": "a bag",
        "description": "A bag made of rough cloth that appears to be strong. It is about 12 inches long and 8 inches wide.",
        "can_take": True,
    },
    "gems": {
        "key": "gems",
        "name": "Gems",
        "summary": "various sized  gems",
        "description": "A pile of sparkling gems of different sizes and colors.",
    },
}

#############################################
# Map
# -------------------------------------------
#               lake
#                \
#              home <-> town-square <-> market
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
        "east": "market",
        "description": "An obelisk sits on a platform in the center of the square. The obelisk is about three feet tall and made of a shiny, black material much like obsidian.",
        "items": []
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
    "market": {
        "key": "market",
        "name": "Town Square Market",
        "west": "town-square",
        "description": "A store with a flower boxed window and brick pavers leading to the front door. Inside there are many things to buy.",
        "items": ["crystal ball", "short dagger", "green potion", "waybread", "fishing tackle",],
        "can": ["shop", "buy"],
    },
}

def debug(message: str):
    """If the Global Variable DEBUG is True then the message will print in colors for the Player"""
    if DEBUG == True:
        # fg = foreground; bg = background
        # breakpoint()
        debug_color = fg.gray + bg.lightblack
        print(MARGIN*" ", debug_color("Debug:"), message)

def error(message: str):
    """Print the error message in colors for the Player"""
    # fg = foreground; bg = background
    style = fg.white + bg.red
    print(style("Error:"), message)

def get_place(key: str =None) -> dict:
    """Getting (returns the current place) where the Player is at currently in the game"""
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
    if PLAYER["inventory"][key] <= 0:
        PLAYER["inventory"].pop(key)

def place_can(spc_key: str) -> bool:
    """Return True if the place dictionary for the players current place contains
     a special command key 'can', otherwise return False.

        Args:
        * item_key (str): Key from the ITEMS dictionary to look for in the place
          "items" list
    """
    place = get_place()
    if spc_key in place.get("can", []):
        return True
    else:
        return False


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

def place_remove(key: str):
    """Remove an item from a current place"""
    # Get the current place
    place = get_place()

    # Making sure that the item key is in the current place items list
    if not place_has(key):
        return

    # Remove the item from current place if the item is in that current place
    place["items"].remove(key)

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

def do_buy(args: list):
    """Player can buy an item, if any, in the current place using the 'buy' command.
    
    Args:
    * args (list[str]): input from player will be turned into a list
    """
    debug(f'Trying to buy {args}.')
    # Check if you can buy things in the current place
    if not place_can("buy"):
        error("Sorry, you can't buy things here.")
        return
    # Check if args is falsy...if the Player typed an item
    if not args:
        error("What do you want to buy?")
        return
    # Does the current place have the item
    name = args[0].lower()
    if not place_has(name):
        error(f"Sorry, I don't see a {name} here.")
        return
    # Is the item for sale
    item = get_item(name)
    if not is_for_sale(item):
        error(f'Sorry, {name} is not for sale.')
        return
    # Can the Player afford the item
    price = abs(item["price"])
    if not player_has("gems", price):
        gems = PLAYER["inventory"]["gems"]
        error(f'Sorry, you can not afford {name} because it costs {price} gems and you only have {gems} gems.')
        return
    # Player buys the item - subtract gems from inventory and add item to inventory
    # breakpoint()
    inventory_change("gems", -price)
    inventory_change(name)
    place_remove(name)
    wrap(f"You bought a {name}.")



def do_shop():
    """Listing items that are for sale by using the "shop" command."""
    if not place_can("shop"):
        error("Sorry, you can't shop here.")
        return
    place = get_place()
    header("Items for sale")
    count_items = 0 
    for key in place.get('items', []):
        # breakpoint()
        item = get_item(key)
        # Checking to see if an item can be purchased with the is_for_sale() function
        if not is_for_sale(item):
            continue
        write(f'{item["name"]:<15} {item["summary"]:^25s} {abs(item["price"]):>4}')
        count_items += 1
    if count_items == 0:
        write("No items in this place.")
    print()

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

def do_take(args: list):
    """Player can take an item and add it to their inventory using the 't',
    'take' or 'grab' command"""
    debug(f"Trying to take {args}.")
    if not args:
        error("What are you trying to take?")
        return
    #Checking if the current place of the player has the item
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
    place_remove(name)
    #Adding the item to the player's inventory
    inventory_change(name)

    wrap(f"You pick up {name} and put it in your pack.")


def do_look():
    """Player can look around in their current place using the 'l' or 'look' command. Player can also look in a direction"""
    debug(f"Trying to look around.")

    # Getting the current place of the Player
    place = get_place()

    # Printing the name and description of the current place
    header(place["name"])
    wrap(place["description"])

    # Listing the items of the current place
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

    # Printing what can be seen in a north, south, east, or west direction
    # from the current place
    directions = ["north", "east", "south", "west"]
    for direction in directions:
        name = place.get(direction)
        if not name:
            continue
        destination = get_place(name)
        write(f"To the {direction} is {destination['name']}.")

def do_drop(args: str):
    """Player can drop an item from their inventory using the 'drop' command"""
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

def write(text: str):
    """Prints a single line of text indented."""
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
        args = split(reply)
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
        elif command == "buy":
            do_buy(args)
        else:
            error("No such command.")
            continue
      

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        ...
    
