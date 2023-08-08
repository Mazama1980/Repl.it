"""Textbased adventure game. https://alissa-huskey.github.io/python-class/  https://alissa-huskey.github.io/python-class/exercises/adventure/intro.html

"""

from pprint import pprint
from sys import stderr
import textwrap
from console import fg, bg, fx
from shlex import split
from console.progress import ProgressBar
import random
from time import sleep 

WIDTH = 60
MARGIN = 2
DELAY = 2
DEBUG = True
COMPASS = ("north", "south", "east", "west")
COLORS = ["red", "blue", "green",]
MAX_HEALTH = 100
BAR = ProgressBar(
    total = (MAX_HEALTH + 0.1),
    clear_left = False,
    width = (WIDTH - len("Health") - len("100%")),
)
PLAYER = {
    "place": "home",
    "inventory": {"gems": 50},
    "health": MAX_HEALTH,

}

DRAGONS = [
        {
            "mood": "mischievous",
            "treasure": (30, 100,),
            "damage": (-15, -5),
            "message": ("throws {gems} gems at you causing you {health} damage."),
        },
        {   "mood": "affirming",
            "treasure": (20, 80,),
            "message": ("wants you to be happy and gives you {gems} gems.")
        },
        {   "mood": "skeptical",
            "damage": (-50, -5),
            "message": ("thinks you smell bad and gives you {health} damage when it sneezes.")
        },

]

ITEMS_ALIASES = {}
ITEMS = {
# Crystal Ball      faintly glowing ball       5
    "crystal ball": {
        "key": "crystal ball",
        "name": "Crystal ball",
        "aliases": ["ball", "globe", "light"],
        "summary": "a faintly glowing ball",
        "description": "All it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "short dagger": {
        "key": "short dagger",
        "name": "Short dagger",
        "aliases": ["knife", "sword", "stabby thing", "dagger",],
        "summary": "double edged blade",
        "description": (
            "The blade is hardened steel with a hollowed double edge. "
            " It has a polished antler bone handle. "
            "It is about 10 inches in length and comes with a sheath.",
        ),
        "price": -22,
    },
    "green potion": {
        "key": "green potion",
        "name": "Green potion",
        "aliases": ["green", "green drink", "health", "potion",],
        "summary": "a health potion ",
        "description": "Drinking this potion will return half your health.",
        "price": -30,
    },
    "waybread": {
        "key": "waybread",
        "name": "Waybread",
        "aliases": ["bread", "food", "travel food",],
        "summary": "food for travel",
        "description": (
            "A bread like food that nourishes. "
            "It doesn't spoil so it works well for traveling."
        ),
        "price": -5,
    },
    "fishing tackle": {
        "key": "fishing tackle",
        "name": "Fishing tackle",
        "aliases": ["tackle", "fishing gear", "fish stuff", "hook", "pole",],
        "summary": "gear for catching fish",
        "description": (
            "Gear needed for catching fish from streams and lakes. "
            " Hooks, lines, folding pole, bobbers, weights. "
            " It is all contained in its own bag.",
        ),
        "price": -10,
    },
    "book": {
        "key": "book",
        "name": "Book",
        "aliases": ["story", "hints", "diary",],
        "title": "My Adventures",
        "summary": "a book about a dragon's adventures.",
        "description": "A soft leather bound book laying on the desk at home. There may be useful information in it.",
        "message": (
            "At the edge of the woods is a cave that is home to a three "
            "headed dragon, each with a different temperament. ",

            "Legend says that if you happen upon the dragon sleeping, the "
            "brave may pet one of its three heads. ",
            
            "Choose the right head and you will be rewarded with great "
            "fortunes. ",

            "But beware, choose poorly and it will surely mean your doom! ",
        ),
        "can_take": True,
    },
    "desk": {
        "key": "desk",
        "name": "Desk",
        "aliases": ["table", "surface",],
        "summary": "writing desk",
        "description": (
            "A smallish wooden desk with 5 drawers. "
            "There is a large book laying on the top."
        ),
    },
    "stick": {
        "key": "stick",
        "name": "Stick",
        "aliases": ["walking stick", "staff", "trek pole",],
        "summary": "walking stick",
        "description": (
            "A staff made from osage orange. "
            "It's about 4 feet tall. "
            "It has curious carvings on it."
        ),
        "can_take": True,
    },
    "bag": {
        "key": "bag",
        "name": "Bag",
        "aliases": ["sack", "pack",],
        "summary": "a bag",
        "description": (
            "A bag made of rough cloth that appears to be strong."
            " It is about 12 inches long and 8 inches wide."
        ),
        "can_take": True,
    },
    "gems": {
        "key": "gems",
        "name": "Gems",
        "aliases": ["rocks", "stones", "jewels"],
        "summary": "various sized  gems",
        "description": "A pile of sparkling gems of different sizes and colors.",
    },
    "dragon": {
    "key": "dragon",
    "name": "The Belfry Dragon",
    "aliases": ["dragons", "three headed dragon","big guy"],
    "summary": "A three headed dragon",
    "description": (
        f"A three headed dragon that sits just inside the Deep Cave."
        f" It's unclear if the dragon is friendly."
        f" Each head has a different color which are {', ' .join(COLORS[0:-1])}"
        f" and {COLORS[2]}."
    ),
    }
}

#############################################
# Map
# -------------------------------------------
#               lake
#                \
#              home <-> town-square <-> market
#                /
#              woods
#               /
#             cave
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
        # "items": ["book", "desk", "stick", "bag"],
        "items": ["desk", "book", "stick","bag",]
    },
    "town-square": {
        "key": "town-square",
        "name": "Old Towne Square",
        "west": "home",
        "east": "market",
        "description": (
            "An obelisk sits on a platform in the center of the square. " 
            "The obelisk is about three feet tall and made of a shiny, "
            "black material much like obsidian." 
        ),
        "items": []
    },
    "woods": {
        "key": "woods",
        "name": "Deep, dark woods",
        "north": "home",
        "south": "cave",
        "description": (
            "There is a deep forest of Redwood trees with. "
            "ferns and bushs growing on the forest floor. "
            "An inviting path is running through it. "
            "You notice that it's quiet and peaceful." 
        ),
    },
    "lake": {
        "key": "lake",
        "name": "Lake Pukaki",
        "south": "home",
        "can": [],
        "description": (
            "The lake is a deep blue in color but it will change "
            "to a purple hue when its mood is unsettled. "
            "There are mysteries to be found in Lake Pukaki's dark waters."
        ),
    },
    "market": {
        "key": "market",
        "name": "Town Square Market",
        "west": "town-square",
        "description": (
            "A store with a flower boxed window and "
            "brick pavers leading to the front door. "
            "Inside there are many things to buy."
        ),
        "items": ["crystal ball", "short dagger", "green potion", "waybread", "fishing tackle",],
        "can": ["shop", "buy"],
    },
    "cave": {
        "key": "cave",
        "name": "Deep Cave",
        "north": "woods",
        "description": (
            "There is a cave in front of you that is deep"
            " and twists away out of sight in the back of the cave."
            " You can see something glinting in the sunlight - piles of gems!"
            " Resting on the biggest pile of gems is a dragon with three heads."
            " Each head is snoring peacefully.",
        ),
        "items": ["gems", "dragon",],
        "can": ["pet"],
    }
}

def abort(message: str):
    """Game will end if it encounters an error and cannot continue and
    an error message will print before the Player is exited from the game"""
    error(message)
    exit(1)

def debug(message: str):
    """If the Global Variable DEBUG is True then the message will print in colors for the Player"""
    if DEBUG == True:
        # fg = foreground; bg = background
        debug_color = fg.lightblack + fx.italic
        print(MARGIN*" ", debug_color("Debug:" + message), sep="")

def error(message: str):
    """Print the error message in colors for the Player"""
    # fg = foreground; bg = background
    style = fg.white + bg.red
    print(style("Error:"), message)

def get_item(key: str) -> dict:
    """Getting (or returning) an item from the ITEMS dictionary"""
    # breakpoint()
    item = ITEMS_ALIASES.get(key)
    if not item:
        abort(f"Woops! The information about the item {key} seems to be missing.")
    return item

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

def header(title: str):
    """A title prints in bold text by calling the header command"""
    print()
    header_title = fx.bold(title)
    write(header_title)
    print()

def health_bar():
    """Using a progress bar to show Player health"""
    write(f"Health {BAR(PLAYER['health'])}")

def health_change(amount: int):
    """Add or remove the Player's health quantity

       Arg:
       * amount (int): the quantity of health will get added or subtracted for the Player.
         If the quantity goes to 0 or less then the game will end as the Player has expired.
    """
    # need to determine the Player's current health 
    # breakpoint()
    energy = PLAYER["health"]
    # need to add (or subtract) Players current health from the argument (amount)
    fitness = energy + amount
    PLAYER["health"] = fitness
    # setting Player's health to zero if it should become a negative number
    # and setting Player's health to a max of 100 if health should become greater than 100
    if PLAYER["health"] < 0:
        PLAYER["health"] = 0
    if PLAYER["health"] > MAX_HEALTH:
        PLAYER["health"] = MAX_HEALTH
    

def inventory_change(key: str, quantity: int=1):
    """Add or remove an item to the Player's inventory

       Args:
       * key (str): the key looks up the item in the inventory dictionary
                    (this key also cooresponds to a key in the ITEMS dictionary)
       * qty (int): the player needs to have at least this much (default 1) in inventory. 
                    A negative quantity greater than the Player's current quantity
                    will remove items from the Player's inventory dictionary
    """
    # .setdefault() method returns the value of the key (if the key is in the dictionary).
    # if not, it inserts key with a value to the dictionary
    PLAYER["inventory"].setdefault(key,0)
    PLAYER["inventory"][key] += quantity
    # Remove from inventory dictionary if quantity is zero
    if PLAYER["inventory"][key] <= 0:
        PLAYER["inventory"].pop(key)

def is_for_sale(item: dict) -> bool:
    """Checking (returning True or False) to see if an item has a price attached to it"""
    if "price" in item:
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

def place_can(action: str) -> bool:
    """Return True if the action is in the 'can' list in the current place dictionary 
      otherwise return False.

        Args:
        * action (str): the name of a command
    """
    place = get_place()
    if action in place.get("can", []):
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
    if not place:
        return
    if item_key in place.get("items", []):
        return True
    else:
        return False

def place_remove(key: str):
    """Remove an item from a current place"""
    # Get the current place
    place = get_place()

    # Making sure that the item key is in the current place items list
    if not place_has(key):
        return

    # Remove the item from current place if the item is in that current place
    place["items"].remove(key)

def player_has(key: str, qty: int=1) -> bool:
    """Determining (return True/False) if there is an item (key) in the PLAYER inventory.
     The qty argument is used to see if any item (key) is >= 1 in the PLAYER inventory.
      It defaults to "1" if no other qty argument is given. 
    
      Args:
      * key (str): the key looks up the item in the inventory dictionary
                   (this key also cooresponds to a key in the ITEMS dictionary)
      * qty (int): the player needs to have at least this much in inventory to return True
    """
    if (key in PLAYER["inventory"]) and (PLAYER["inventory"][key] >= qty):
        return True
    else:
        return False

def setup_aliases():
    """Setting up ITEMS_ALIASES dictionary with alternate names or aliases that the Player could type for particular items of interest.
      There is no argument or returned value."""
    # A for loop will itirate over the items dictionary to aquire the key and item then iterate 
    # over the ITEMS_ALIASES dictionary to check for alternate names (aliases) for that item.
    # for key, value in dictionary(): *getting the key and value pair from a dictionary*
    global ITEMS_ALIASES
    ITEMS_ALIASES = {}
    for key, item in ITEMS.items():
        aliases = item.get('aliases', [])
        ITEMS_ALIASES[key] = item
        for alias in aliases:
            ITEMS_ALIASES[alias] = item
        # continue working on aliases from the Todo file line 81 and try using aliases in the game for 'take', 'drop', etc
        # Alissa continue fixing the ipython error message problem


def wrap(text: str, indent: int=1):
    """Formatted text and longer text will wrap and be readable to the Player by calling the wrap command"""
    # check if text is a string then making it a tuple
    if isinstance(text, str):
        text = (text,)
    blocks = []
    for stanza in text:
        paragraph = textwrap.fill(
            stanza,
            WIDTH,
            initial_indent = (MARGIN * " ") * indent,
            subsequent_indent = (MARGIN * " ") * indent
        )
        blocks.append(paragraph)
    print(*blocks, sep="\n\n")
    print()

def write(text: str):
    """Prints a single line of text indented."""
    print(f"{MARGIN * ' '}{text}")

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
    key = args[0].lower()
    if not place_has(key):
        error(f"Sorry, I don't see a {key} here.")
        return
    # Is the item for sale
    item = get_item(key)
    if not is_for_sale(item):
        error(f'Sorry, {key} is not for sale.')
        return
    # Can the Player afford the item
    price = abs(item["price"])
    if not player_has("gems", price):
        gems = PLAYER["inventory"]["gems"]
        error(f'Sorry, you can not afford {key} because it costs {price} gems and you only have {gems} gems.')
        return
    # Player buys the item - subtract gems from inventory and add item to inventory

    inventory_change("gems", -price)
    inventory_change(key)
    place_remove(key)
    wrap(f"You bought a {key}.")

def do_drop(args: list):
    """Player can drop an item from their inventory using the 'drop' command"""
    debug(f'Trying to drop {args}')
    if not args:
        error("What do you want to drop?")
        return
    key = args[0].lower()
    if not player_has(key):
        error(f"You don't have any {key}.")
        return
    # NOTE -= is shorthand for:
    # PLAYER["inventory"][name] = PLAYER["inventory"][name] - 1
    PLAYER["inventory"][key] -= 1
    if not PLAYER["inventory"][key]:
        PLAYER["inventory"].pop(key)
    place_add(key)
    wrap(f'You set down the {key}')
    ...

def do_examine(args: list):
    """Player can examine an item using the 'x', 'exam' or 'examine' command"""
    debug(f'Trying to examine {args}')
    if not args:
        error("What do you want to exam?")
        return
    #Checking if the current place of the player has the item or the player has the item.
    name = args[0].lower()
    if not (place_has(name) or player_has(name)):
       error(f"Sorry, I don't know what this is:{name}")
       return
    #Listing the item and description for the player.
    item = get_item(name)
    header(item["name"])
    if player_has(name):
        write(f'x{PLAYER["inventory"][name]} in inventory')
        print()
    elif place_can("shop") and is_for_sale(item):
        write(f'{abs(item["price"])} gems')
        print()
    wrap(item["description"])

def do_go(args: list):
    """Player is moving to another area"""
    debug(f"Trying to go: {args}")
    # checking that a valid direction has been asked
    if not args:
        error("Which way do you want to go?")
        return
    direction = args[0].lower()
    if direction not in COMPASS:
        error(f"sorry, I don't know how to go: {direction}")
        return
    # Look up where Player is currently and if Player can go in requested direction
    old_place = get_place()
    new_name = old_place.get(direction)
    if not new_name:
        error(f"Sorry, you can't go {direction} from here.")
        return
    # update Player to new place and describe new place
    PLAYER["place"] = new_name
    do_look()


def do_inventory():
    """Listing the Player's current health and inventory. Called when the player types the
    "inventory" or "i" command. """
    debug("Trying to show inventory.")
    health_bar()
    header("Inventory")
    # If the Player's inventory is empty then print the message "Empty"
    if not PLAYER["inventory"]:
        write("Empty")
    # Listing the Player's item name with the quantity of each item
    for name, qty in PLAYER["inventory"].items():
        item = get_item(name)
        write(f'{item["name"]:<15} {qty:>4}')
    print()


def do_look():
    """Player can look around in their current place using the 'l' or 'look' command. 
    Player can also look in a direction"""
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
        write(f"You see a {text}. \n")
    print()

    # Printing what can be seen in a north, south, east, or west direction
    # from the current place
    for direction in COMPASS:
        name = place.get(direction)
        if not name:
            continue
        destination = get_place(name)
        write(f"To the {direction} is {destination['name']}.")

def do_pet(args: list):
    """Player can pet an object in the current place using the 'pet' command.
     
    Args:
    * args (list[str]): input from the player will be turned into a list   
    """
    # Check if you can pet things in the current place
    if not place_can("pet"):
        error("Sorry, you can't pet things here.")
        return
    debug(f'Trying to pet a {args} dragon.')
    # Removing words from args 
    words = ["dragon", "head"]
    for word in words:
        # When the word is in args we want to remove it
        if word in args:
            args.remove(word)
    # Making sure the player typed an item to pet (args)
    if not args:
        error("What do you want to pet?")
        return
    # setting the remaining arg word to the variable 'color'
    color = args[0].lower()
    # making sure the color is valid
    if color not in COLORS:
        error("I don't see a dragon with that color here.")
        return
    # the dragon will be randomly selected
    dragon = random.choice(DRAGONS)
    # the color the Player chose will be added to the randomly selected dragon
    dragon["color"] = color
    debug(f"You picked the dragon's {dragon['mood']} {dragon['color']} head.")
    # getting the value of the treasure key
    possible_treasure = dragon.get("treasure", (0, 0))
    # randomly choosing a number of gems from the range assigned to that dragon mood
    dragon["gems"] = random.randint(*possible_treasure)
    # adding treasure to Player's inventory
    inventory_change("gems", dragon["gems"])
    # getting the amount of damage
    possible_damage = dragon.get("damage", (0,0))
    dragon["health"] = random.randint(*possible_damage)
    # reducing Player's health
    health_change(dragon["health"])
    # create a dramatic effect with timed (delayed) sentences
    sentences = [
        "You slowly creep forward...", 
        "...gingerly reach out your hand...",
        f"...and gently pat the dragon's {dragon['color']} head.",
        "...",
        "He blinks sleepy eyes and peers at you...",
    ]
    for text in sentences:
        print()
        write(text)
        sleep(DELAY)
    print()
    # print a message if gems are added or damage is done to Player's health
    tpl = ("The dragon's {mood} {color} head ") + dragon["message"]
    text = tpl.format(**dragon)
    wrap(text)

def do_quit():
    """If Player types 'q' or 'quit' the game will end and the the word "Goodbye!" will print"""
    write(fg.lightyellow("Goodbye!"))
    quit()

def do_read(args: list):
    """Player can read a particular item in the current place or in Player's inventory using the 'read' or 'r' command"""
    debug(f'Trying to read {args}.')
    if not args:
        error("What do you want to read?")
        return
    #Checking if the current place of the player has the item or the player has the item.
    name = args[0].lower()
    if not (place_has(name) or player_has(name)):
        error(f"Sorry, I don't know what this is: {name}")
        return
    item = get_item(name)
    if not item.get("message"):
        error(f"Sorry, I can't read {name}")
        return
    print()
    print("It reads.... ")
    header(item["title"])
    wrap(item["message"], indent=2)

def do_shop():
    """Listing items that are for sale by using the "shop" command."""
    if not place_can("shop"):
        error("Sorry, you can't shop here.")
        return
    place = get_place()
    header("Items for sale")
    count_items = 0 
    for key in place.get('items', []):
        item = get_item(key)
        # Checking to see if an item can be purchased with the is_for_sale() function
        if not is_for_sale(item):
            continue
        write(f'{item["name"]:<15} {item["summary"]:^25s} {abs(item["price"]):>4}')
        count_items += 1
    if count_items == 0:
        write("No items in this place.")
    print()

def do_take(args: list):
    """Player can take an item and add it to their inventory using the 't',
    'take' or 'grab' command"""
    debug(f"Trying to take {args}.")
    if not args:
        error("What are you trying to take?")
        return
    #Checking if the current place of the player has the item
    key = args[0].lower()
    if not place_has(key):
        error(f"Sorry, I don't see a {key} here.")
        return
    #Checking if the item is available to take by the player
    item = get_item(key)
    if not item.get("can_take"):
        wrap(f"You try to pick up {key}, but you find you aren't able to lift it.")
        return
    #Removing the item from the current place
    place_remove(key)
    #Adding the item to the player's inventory
    inventory_change(key)
    print()
    wrap(f"You pick up a {key} and put it in your pack.")

def main():
    """Game User interface (UI). The game starts here."""
    debug("Hello")
    setup_aliases()
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
        elif command == "buy":
            do_buy(args)
        elif command in ("r", "read"):
            do_read(args)
        elif command == "pet":
            do_pet(args)
        else:
            error("No such command.")
            continue
      

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        ...
    
