
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
DELAY = .75
DEBUG = False
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
    "inventory": {"gems": 0},
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
    "crystal-ball": {
        "key": "crystal-ball",
        "name": "Crystal ball",
        "aliases": ["ball", "globe", "light"],
        "summary": "a faintly glowing ball",
        "description": "All it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "dagger": {
        "key": "dagger",
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
    "potion": {
        "key": "potion",
        "name": "Green potion",
        "aliases": ["green", "green drink", "health", "potion",],
        "summary": "a health potion ",
        "description": "Drinking this potion will make you feel refreshed.",
        "price": -30,
        "health_points": 50,
        "drink_message": (
            "You take the cork off the green flask.",
            "You try a small taste. It tastes light and fruity",
            "You drink the rest and you begin to feel refreshed.",
        ),
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
        "health_points": 70,
        "eat_message": (
            "You unwrap the bread from it's covering.",
            "You try a small bite.",
            "It is delicious.",
            "You eat the whole wafer.",
        ),
    },
    "fishing-tackle": {
        "key": "fishing-tackle",
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
        "description": "A soft leather bound book laying on the desk. There may be useful information in it.",
        "message": (
            "At the edge of the woods is a cave that is home to a three "
            "headed dragon, each with a different color and corresponding temperament. ",

            "Legend says that if you happen upon the dragon sleeping, the "
            "brave may pet one of its three heads; red, green, or blue. ",
            
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
    "waterskin": {
        "key": "waterskin",
        "name": "Waterskin",
        "aliases": ["water bottle", "pouch",],
        "summary": "a waterskin",
        "description": (
            "An oval shaped bag made of hide.",
            "It's water tight so it works well as a water bottle.",
        ),
        "can_take": True,
        "health_points": 30,
        "drink_message": (
            "You take off the wooden topper",
            "and take a long drink of the cool water.",
            "Your throat is no longer parched.",
        ),
    },
    "berries": {
        "key": "berries",
        "name": "Berries",
        "aliases": ["wild food", "fruit",],
        "summary": "wild fruit from the woods",
        "description": (
            "Berries that can be picked",
            "in the woods or near the lake.",
            "They are good to eat but it takes",
            "many, many of them to be filling."
        ),
        "can_take": True,
        "health_points": 70,
        "eat_message": (
            "You try a berry. It tastes tart but good.",
            "You feel better as if the berries",
            "are healthful and have healing properties."
        ),
    },
    "mushrooms": {
        "key": "mushrooms",
        "name": "Mushrooms",
        "aliases": ["toadstools", "fungus", "shrooms",],
        "summary": "various types of edible mushrooms",
        "description": ("Several types of fungus are available growing in the woods."
                        "All mushrooms that you see are edible."
                        "Some varieties may have different effects on you."),
        "can_take": True,
        "health_points": 30,
        "eat_message": ("You pop a mushroom in your mouth;",
                        "it tastes earthy.",
                        "you feel a little more healthful."),
    },
    "pebbles": {
        "key": "pebbles",
        "name": "pebbles",
        "aliases": ["rocks", "stones",],
        "summary": "pebbles that are various colors",
        "description": "the lake shore is made up of different"
        "colored pebbles. They are rounded as if already partly"
        "polished. You may want to put a few in your bag.",
        "can_take": True, 
    },
    "water":{
        "key": "water",
        "name": "water",
        "aliases": ["H2O","liquid",],
        "summary": "clear water from lake Pukaki",
        "description": "The water from Lake Pukaki"
        "is clear and delicious. You can fill your"
        "waterskin with the refreshing liquid.",
        "can_take": True,
    },
    "gems": {
        "key": "gems",
        "name": "Gems",
        "aliases": ["shiny", "jewels"],
        "summary": "various sized gems",
        "description": "Piles of sparkling gems of different sizes and colors.",
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
        "items": ["desk", "book", "stick", "bag", "waterskin",],
    },
    "town-square": {
        "key": "town-square",
        "name": "Old Towne Square",
        "west": "home",
        "east": "market",
        "description": (
            "An obelisk sits on a platform in the center of the square. " 
            "There are markings on the surface. You take note of what it says: "
            "l = look; e = examine; t = take; i = inventory; g = go; r = read; q = quit"
            " buy; shop; eat; drink; pet. " 
            "Items with two words are special and must be hyphenated. "
            "Use these commands wisely." 
        ),
        "items": [],
    },
    "woods": {
        "key": "woods",
        "name": "Deep, dark woods",
        "north": "home",
        "south": "cave",
        "description": (
            "There is a deep forest of Redwood trees with "
            "ferns and bushes growing on the forest floor. "
            "An inviting path is running through it. "
            "You notice that it's quiet and peaceful." 
        ),
        "persistent_items": ["berries", "mushrooms",],
        "can": ["pick"]
    },
    "lake": {
        "key": "lake",
        "name": "Lake Pukaki",
        "south": "home",
        "description": (
            "The lake is a deep blue in color but it will change "
            "to a purple hue when its mood is unsettled. "
            "There are mysteries to be found in Lake Pukaki's dark waters."
        ),
        "persistent_items": ["pebbles", "water",],
        "can": ["take"],
        "items": ["pebbles", "water",],
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
        "items": ["crystal-ball", "dagger", "potion", "waybread", "fishing-tackle",],
        "persistent_items": ["potion", "waybread",],
        "can": ["shop", "buy",],
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
        "can": ["pet",],
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
    item = ITEMS_ALIASES.get(key)
    if not item:
        abort(f"Woops! The information about the item {key} seems to be missing. (Check if the setup_aliases() needs to be called.)")
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
    # save Player's current health to a variable to use at the end of the function
    before = PLAYER["health"]
    # need to add (or subtract) Players current health from the argument (amount)
    fitness = before + amount
    PLAYER["health"] = fitness
    # setting Player's health to zero if it should become a negative number
    # and setting Player's health to a max of 100 if health should become greater than 100
    if PLAYER["health"] < 0:
        PLAYER["health"] = 0
    if PLAYER["health"] > MAX_HEALTH:
        PLAYER["health"] = MAX_HEALTH
    return PLAYER["health"] - before
    

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
    # changing the args from a list to a string
    key = args[0].lower()
    # Does the current place have the item
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

def do_consume(action: str, args: list): # make the consumable item set to zero; add then call inventory_change function
    """Player can eat or drink an item using the 'eat' or 'drink' command.
    
    Args:
    * action (str): "eat" or "drink"
    * args (list[str]): input from player will be turned into a list
    """

    debug(f'Trying to {action}: "a" {args}')
    # check if Player typed an args (item for the action)
    if not args:
        error(f'What would you like to {action}?')
        return
    # get the item entered by Player and make it lowercase
    name = " ".join(args).lower()
    # check if the item is in the Player's inventory
    if not player_has(name):
        error(f'Sorry, You do not have any {name} to {action}.')
        return
    # check if the item can be eaten or is drinkable
    item = get_item(name) 
    if not item.get(f'{action}_message'):
        error(f'Silly, you can not {action} this {name}.')
        return
    # set the consumable item to zero
    # call inventory_change to take item out of Player's inventory
    inventory_change(name, -1)
    print()
    sentences = item[f"{action}_message"]
    for sentence in sentences:
        wrap(sentence)
        print()
        sleep(DELAY)
    # check if the item has any health points 
    if not item.get("health_points"):
        print(f'The {name} has no health points.')
        return
    # change Player's health points after consuming an item
    new_health = health_change(item["health_points"])
    print(f'Your health is now {PLAYER["health"]} points.')
    
    
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
        error("What do you want to examine?")
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
    new_place = get_place(new_name)
    # check if a "persistent_item" exists in new_place. Add the empty list brackets as a second
    # argument so if a place doesn't have a 'persistent_items' key then it can continue instead
    # of getting a NONETYPE error
    items = new_place.get("persistent_items", [])
    for item in items:
      place_add(item)
    do_look()

# tweak the 'persistent_items' add more items; make them consumable; add health, etc.

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

# Add more persistent_items to PLACES. Try adding a function that can refill the waterskin and a fishing function.
# Try making a flow (a point) to playing the game.
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
        write(f"You see (a) {text}. \n")
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
    wrap(f"You pick up (a) {key} and put it in your pack.")
    # if new_place not in valid_place:

def do_warp(args: list):
    """Creator (Original Player) warps or jumps to another area."""
    # breakpoint()
    debug(f'Trying to warp to: {args}')
    # checking that a valid place has been asked
    if not args:
        error("Choose a place that you created.")
        return
    # putting args from a list to a string
    warp_place = args[0].lower()
    valid_warp = PLACES.get(warp_place)
    if not valid_warp:
        error(f"This place {args} does not exist. Choose from these places: ...")
        return
    # Update Player to new place and describe new place
    PLAYER["place"] = warp_place
    print(warp_place)
    do_look()

def main():
    """Game User interface (UI). The game starts here."""
    debug("Hello")
    setup_aliases()
    print(fg.lightyellow("Welcome!"))
    with fg.lightcyan:
           print("Take a look around;")
           print("you may find something")
           print("useful for your travels.")
    while True:
        debug(f"You are at: {PLAYER['place']}")
        reply = input("> ").strip()
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
        elif command in ("eat", "drink"):
            do_consume(command, args)
        elif command == "warp":
            do_warp(args)
        else:
            error("No such command.")
            continue
      

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        ...
    
