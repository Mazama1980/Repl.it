from adventure import (
    is_for_sale,
    inventory_change,
    do_take,
    do_drop,
    place_has,
    get_place,
    place_add,
    place_remove,
    do_shop,
    place_can,
    do_buy,
    do_examine,
    do_read,
    place_add,
    wrap,
    do_go,
    get_item,
    player_has,
    do_inventory,
    do_look,
    do_quit,
    health_change,
    # setup_aliases,
)
# import pdbr
from copy import deepcopy

import pytest

import adventure

PLAYER_STATE = deepcopy(adventure.PLAYER)
PLACES_STATE = deepcopy(adventure.PLACES)
ITEMS_STATE = deepcopy(adventure.ITEMS)


def revert():
    """Revert game data to its original state."""
    adventure.PLAYER = deepcopy(PLAYER_STATE)
    adventure.PLACES = deepcopy(PLACES_STATE)
    adventure.ITEMS = deepcopy(ITEMS_STATE)


@pytest.fixture(autouse=True)
def teardown(request):
    """Auto-add teardown method to all tests."""
    request.addfinalizer(revert)

# GIVEN: some context
# WHEN: some action
# THEN: some result


def test_truth():
    assert True


def test_is_for_sale():
    # GIVEN: an item with a price
    fake_item = {
        "name": "art",
        "price": -20
    }

    # WHEN: you call is_for_sale()
    result = is_for_sale(fake_item)

    # THEN: it should return True
    assert result, "is_for_sale() should return True if the item has a price"

def test_get_item():
    # Given: an item is in the ITEMS dictionary
    adventure.ITEMS["sword"] = {"name": "sword"}
    # When: get_item is called with a key
    result = get_item("sword")
    # Then: the item is returned to be used for another function
    assert result

def test_get_item_no_item(capsys):
    # Given: an item is not in the ITEMS dictionary
    adventure.ITEMS = {}
    # When: call get_item("sword")
    with pytest.raises(SystemExit) as ex:
        get_item("sword")
    output = capsys.readouterr().out
    # Then: the statement "Woops! The information about the sword seems to be missing." should print
    assert "Woops! The information about the item sword seems to be missing." in output

def test_get_place_default():
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"
    # And: current place is in the PLACES dictionary
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
    }
    # When: call get_place() and no key is given
    result = get_place()
    # Then: the current place is returned to be used in other functions
    assert result["name"] == "somewhere"

# @pytest.mark.skip(reason="in progress")
def test_get_place_with_key():
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"
    # And: current place is in the PLACES dictionary
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
    }
    # And: another place exists
    adventure.PLACES["nowhere"] = {
        "name": "Anywhere but here",
    }
    # When: call get_place("nowhere") with a key other than Player's current place
    result = get_place("nowhere")
    # Then: the PLACES dictionary for that place should be returned, instead of the current place
    assert result["name"] == "Anywhere but here"

def test_get_place_missing_from_PLACES(capsys):
    # When: call get_place("nowhere") with a nonexistent place (key)
    with pytest.raises(SystemExit) as ex:
        get_place("nowhere")
    output = capsys.readouterr().out
    # Then: the statement beginning with "Woops!" should print 
    assert "Woops!" in output
    
def test_player_has_with_key_in_inventory():
    # Given: the Player has an item in inventory
    adventure.PLAYER["inventory"] = {"neurolizer": 1}
    # And: the item exists in the ITEMS dictionary
    adventure.ITEMS["neurolizer"] = {
        "name": "neurolizer",
        "description": "A gadget the size of a pen that erases memory in the set parameters",
    }
    # When: call player_has() with a key that is in inventory
    result = player_has("neurolizer")
    # Then: the function will return True
    assert result is True, "player_has should return True with the item neurolizer in inventory"

@pytest.mark.parametrize(["inventory", "message"], [
            ({}, 'without item neurolizer in inventory'),
            ({'neurolizer': 0}, 'when neurolizer has zero inventory'),
        ]
)
def test_player_has_with_key_not_in_inventory(inventory, message):
    # Given: the Player has nothing in inventory
    adventure.PLAYER["inventory"] = inventory
    # And: an item exists in the ITEMS dictionary
    adventure.ITEMS["neurolizer"] = {
        "name": "neurolizer",
    }
    # When: call player_has() with a particular key
    result = player_has("neurolizer")
    # Then: the function will return False
    assert result is False, f"player_has should return False {message}"

def test_do_inventory(capsys):
    # Given: the Player has an item in inventory
    adventure.PLAYER["inventory"] = {"quill": 3}
    # And: the item exists in the ITEMS dictionary
    adventure.ITEMS["quill"] = {
        "name": "quill",
    }
    # When: call do_inventory() without a key argument
    do_inventory()
    output = capsys.readouterr().out
    # Then: the statement should print out with the word "quill" in it
    assert "quill" in output
    # And: the statement should print a quantity of "3"
    assert " 3\n" in output

def test_do_inventory_if_empty(capsys):
    # Given: the Player has nothing in inventory
    adventure.PLAYER["inventory"] = {}
    # And: an item exists in the ITEMS dictionary
    adventure.ITEMS["quill"] = {
        "name": "quill",
    }
    # When: call do_inventory() without a key argument
    do_inventory()
    output = capsys.readouterr().out
    # Then:  the statement "Empty" should print
    assert "Empty" in output

@pytest.mark.parametrize(["items", "items_text", "message"], [
       (['sword'], "sword", 'one item in current place'),
       (['sword', 'book'], "sword and book", 'two items in current place'),
       (['sword', 'book', 'sack'], "sword, book and sack", 'three items in current place'),
    ]
)
def test_do_look(capsys, items, items_text, message):
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"
    # And: that place exists with items in the current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": items,
        "description": "Hard to tell where you are.",
        "east": "pit of despair",
        "north": "fire swamp",
    }
    # And: places exist in different directions from the current place
    adventure.PLACES["pit of despair"] = {
        "key": "the pit",
        "name": "pit of despair",
    }
    adventure.PLACES["fire swamp"] = {
        "key": "fire swamp",
        "name": "fire swamp",
    }
    # And: items with descriptions are in the ITEMS dictionary
    adventure.ITEMS["sword"] = {
        "name": "sword",
    }
    adventure.ITEMS["book"] = {
        "name": "book",
    }
    adventure.ITEMS["sack"] = {
        "name": "sack",
    }
    # When: call do_look() with no key arguments
    do_look()
    output = capsys.readouterr().out
    # Then: it should print the name of the place
    assert "somewhere" in output
    # And: it should print the description of the current place
    assert "Hard to tell where you are." in output
    # And: it should print a list of items in the place
    assert f"You see {items_text}." in output, message 
    # And: should print nearby places
    assert f"To the north is fire swamp." in output
    assert f"To the east is pit of despair." in output

def test_do_look_no_items(capsys):
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"
    # And: that place exists with no items in the current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": [],
        "description": "Hard to tell where you are.",
    }
    # When: call do_look() with no key arguments
    do_look()
    output = capsys.readouterr().out
    # Then: the statement "You see..." will not print out
    assert "You see" not in output

def test_do_quit(capsys):
    # Given: Player types "q" or "quit" to exit the game
    # When: call do_quit()
    with pytest.raises(SystemExit) as ex:
        do_quit()
    output = capsys.readouterr().out
    # Then: "Goodbye!" should print
    assert "Goodbye!" in output

def test_inventory_change_with_no_quantity_arg():
    # Given: Item and quantity Player's inventory
    adventure.PLAYER["inventory"]["lembas"] = 99

    # When: call inventory_change for item with no quantity argument
    inventory_change("lembas")

    # Then: should add one to quantity to Player's inventory
    assert adventure.PLAYER["inventory"]["lembas"] == 100, f'inventory_change() with no quantity argument shoud add 1.'

@pytest.mark.parametrize(
    ["current_qty", "add_qty", "result"], [
        (99, 2, 101),
        (99, -2, 97),
    ]
)
def test_inventory_change_with_quantity(current_qty, add_qty, result):
    # Given: Item and quantity to Player's inventory
    adventure.PLAYER["inventory"]["lembas"] = current_qty

    # When: call inventory_change with item and specific quantity
    inventory_change("lembas", add_qty)

    # Then: should add the specific quantity to the Player's inventory of that item
    assert adventure.PLAYER["inventory"]["lembas"] == result

def test_inventory_change_missing_key():
    # Given: The Player inventory does not contain an item
    adventure.PLAYER["inventory"] = {}

    # When: call inventory_change with item
    inventory_change("lembas")

    # Then: Should add missing key of the item to the Player's inventory
    assert "lembas" in adventure.PLAYER["inventory"], f"inventory_change() should add missing keys to the inventory."

    # And: Should add 1 to Player's inventory 
    assert adventure.PLAYER["inventory"]["lembas"] == 1, f"inventory_change() with no quantity argument should add 1."
    
def test_inventory_change_remove():
    # Given: Item and quantity in Player's inventory
    adventure.PLAYER["inventory"]["lembas"] = 5

    # When: calling inventory_change with item and a negative quantity
    inventory_change("lembas", -6)

    # Then: Should remove quantity of item from Player's inventory
    assert "lembas" not in adventure.PLAYER["inventory"], f"inventory_change() subtracting quantity <= 0 will remove key or item."

def test_do_go(capsys):
    # Given: Player is in the current place
    adventure.PLAYER["place"] = "somewhere"
    # And: Player moves to another place
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "east": "town-square",
    }
    adventure.PLACES["town-square"] = {
        "name": "town-square",
        "description": "the square",
    }
    # When: call do_go() with "east" for args and capture output
    do_go(["east"])
    output = capsys.readouterr().out
    # Then: the statement should print "town-square"
    assert "town-square" in output
    # And: Player should be in the new place
    assert adventure.PLAYER["place"] == "town-square", "Player should be in the new place 'town-square'."

def test_do_go_no_args(capsys):
    # Given: Player in current place
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
    }
    # When: call do_go()
    do_go([])
    output = capsys.readouterr().out
    # Then: Statement should print "Which way do you want to go?"
    assert "Which way do you want to go?" in output


def test_do_go_invalid_direction(capsys):
    # Given: Player in current place
    adventure.PLAYER["place"] = "somewhere"
    # When: call do_go(["up"])
    do_go(["up"])
    output = capsys.readouterr().out
    # Then: debug should say "Trying to go up"
    assert "Trying to go: ['up']" in output
    # And: error should say "Which way do you want to go?"
    assert "sorry, I don't know how to go: up" in output

def test_do_go_unallowed_direction(capsys):
    # Given: Player is in the current place
    adventure.PLAYER["place"] = "somewhere" 
    # And: current place does not have the key of a particular direction
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
    }
    # When: call do_go() with that direction
    do_go(["west"])
    output = capsys.readouterr().out
    # Then: statement should print "Sorry, you can't go west from here."
    assert "Sorry, you can't go west from here." in output


def test_do_take(capsys):
    # Given: Item and quantity in Player's inventory
    adventure.PLAYER["inventory"]["sword"] = 1

    # And: item is possible to take
    adventure.ITEMS["sword"] = {"name":"short sword", "can_take": True}

    # And: you have a place dictionary
    adventure.PLACES["somewhere"] = {"name": "Somewhere out there"}

    # And: the player is in that place
    adventure.PLAYER["place"] = "somewhere"

    # And: item is in the correct place
    adventure.PLACES["somewhere"]["items"] = ["sword"]

    # When: call do_take item
    do_take(["sword"])

    output = capsys.readouterr().out

    # Then: Should have two of item in Player's inventory
    assert adventure.PLAYER ["inventory"]["sword"] == 2, f"Player inventory should have a sword added to total 2 sword"

    # And: The item in that place should not be in that place anymore
    assert adventure.PLACES ["somewhere"]["items"] == [], "The items list should be empty when the sword is taken"

    # And: Print for player should say item was picked up
    assert "pick up sword" in output, "A message should be printed telling the Player that they took the item."


def test_do_drop(capsys):
    # Given: Item in Player's inventory
    adventure.PLAYER["inventory"]["sword"] = 1

    # When: call do_drop with item
    do_drop(["sword"])

    output = capsys.readouterr().out

    # Then: item should be gone from Player's inventory
    assert "sword" not in adventure.PLAYER["inventory"], "Player inventory should not have a sword."

    # And: item should be added to the place where the Player is currently
    assert place_has("sword"), "A sword should be added to the home items."

    # And: printed message for player should say item was dropped
    assert "You set down" in output, "A message should say that an item has been set down."

def test_place_add():
    # Given: That the Player is in a particular place
    current_place = get_place()

    # And: That item is not in the place items list
    current_place["items"] = []

    # When: Call place_add() with an item key
    place_add("sword")

    # Then: Item has been added to the place item list
    assert place_has("sword"), "A sword should be added to the place items list."

def test_place_remove():
    # Given: That the Player is in a particular place
    current_place = get_place()

    # And: The item is in the current place
    current_place["items"] = ["sword"]

    # When: Call place_remove() with an item key
    place_remove("sword")

    # Then: The item will be removed from the current place
    assert not place_has("sword"), "A sword should be removed from the current place."

def test_place_remove_missing_item():
    # Given: that the Player is in a particular place
    current_place = get_place()

    # And: The item is not in the current place
    current_place["items"] = []

    # When: Call place_remove() with an item key
    place_remove("sword")

    # Then: The item will be removed from the current place
    assert not place_has("sword"), "The item will not be in the current place items list."

def test_do_shop(capsys):
    # Given: There are no items initially
    adventure.ITEMS = {}

    # And: we add some items are for sale
    adventure.ITEMS["sword"] = {"name": "sword", "summary": "short sword", "price": -50}
    adventure.ITEMS["neurolizer"] = {"name": "neurolizer", "summary": "memory eraser", "price": -100}

    # And: we add an item not for sale
    adventure.ITEMS["quill"] = {"name": "quill", "summary": "writing utensil",}

    # And: items for sale and able to be purchased with the 'can':'shop' key in the current place
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["shop"],
        "items": ["sword", "quill"],
    }

    # And: the player is in that place
    adventure.PLAYER["place"] = "somewhere"

    # And: items for sale but not in current place
    adventure.PLACES["nowhere"] = {"name": "Anywhere but here"}
    adventure.PLACES["nowhere"]["items"] = ["neurolizer"]

    # When: Call do_shop() and capture the output
    do_shop()
    output = capsys.readouterr().out

    # Then: If the item is in the current place and is for sale it will be listed with price
    assert "short sword" in output, "For sale items that are in the current place will be listed."

    # And: If the item is in the current place and is not for sale will not be listed
    assert "quill" not in output, "Not For sale items that are in the current place will not be listed."

    # And: the item is for sale but not in the current place will not be listed
    assert "neurolizer" not in output, "The item is for sale but not in the current place will not be listed."

@pytest.mark.parametrize(["action", "message"],[
    ({}, "Current place has no 'can' key"),
    ({"can": []}, "Current place has no 'shop' key.")
])
def test_do_shop_with_no_shop_key(capsys, action, message):
    # Given: the Player is in a current place
    adventure.PLAYER["place"] = "somewhere"

    # And: the current place does not have the 'can':'shop' key
    adventure.PLACES["somewhere"] = {"name":"Somewhere out there"}

    adventure.PLACES["somewhere"].update(action)

    # When: call do_shop() and capture the output
    do_shop()
    output = capsys.readouterr().out

    # And an error message will print that shopping is not possible in current place
    assert "Sorry, you can't shop here." in output, message
    

def test_do_shop_place_with_no_items_key(capsys):
    # Given: Player is in a particular place
    adventure.PLAYER["place"] = "somewhere"

    # And: That the current place does not have an 'items' key
    adventure.PLACES["somewhere"] = {"name":"Somewhere out there"}

    # And: if items are able to be purchased with the 'can':'shop' key
    adventure.PLACES["somewhere"]["can"] = ["shop"]

    # When: call do_shop() and capture the output
    do_shop()
    output = capsys.readouterr().out

    # Then: heading title should print for the particulur place
    assert "Items for sale" in output, "The header for the current place should print"

    # And: a statement should say there are no 'items' for the current place
    assert "No items in this place." in output, "The statement should print under the header"

# @pytest.mark.skip(reason="to be implemented")
def test_place_can_when_true():
    # Given: Player is in a particular place
    adventure.PLAYER["place"] = "somewhere"

    # And: Place has a special command key
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["fly"],
    }

    # When: call place_can() with that key
    result = place_can("fly")

    # Then: The result will be True
    assert result is True, "place_can() should return True if there is a special command key where the Player is. "

def test_place_can_when_false():
    # Given: Player is in a particular place
    adventure.PLAYER["place"] = "somewhere"

    # And: Place does not have a special  key
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
    }

    # When: call place_can() with that key
    result = place_can("fly")

    # Then: The result will be False
    assert result is False, "place_can() should return False if there is no special command key where the Player is."

def test_do_buy_when_place_cannot_buy(capsys):
    # Given: the player is in a current place
    adventure.PLAYER["place"] = "somewhere"

    # And: the current place does not have the 'can':'buy' key
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": [],
    }

    # When: call do_buy and capture the output
    do_buy([])
    output = capsys.readouterr().out

    # Then: an error message saying you can't buy anything in the current place should print
    assert "Sorry, you can't buy things here." in output, "The statement should print"

def test_do_buy_when_args_is_falsy(capsys):
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["buy"]
    }
    # When: Player doesn't type an item and calls do_buy()
    do_buy([])
    output = capsys.readouterr().out

    # Then: Print "What do you want to buy?"
    assert "What do you want to buy?" in output, "The statement should print"

def test_do_buy_if_no_item_in_place(capsys):
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"
    # And: making sure the can buy command is available
    adventure.PLACES["somewhere"] = {
        "name": "somewhere out there",
        "can" : ["buy"],
    }
    # And: adding an item that is for sale but not available in the current place
    adventure.PLACES["nowhere"] = {
        "name": "Anywhere but here",
        "items": ["neurolizer"],
    }
    adventure.ITEMS["neurolizer"] = {
        "name": "neurolizer",
        "price": -100
    }
    # When: Player types an item but it's not there by calling do_buy("neurolizer")
    do_buy(["neurolizer"])
    output = capsys.readouterr().out

    # Then: Print "Sorry, I don't see a neurolizer here."
    assert ("Sorry, I don't see a neurolizer here.") in output, "The statement should print"

def test_do_buy_if_item_is_not_for_sale(capsys):
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"

    # And: making sure the 'buy' command is available
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["buy"],
        "items": ["quill"],
    }

    # And: adding an item that is in the current place but not for sale
    adventure.ITEMS["quill"] = {"name": "quill"}

    # When: Player types an item but it's not available to purchase 
    #       by calling do_buy("quill") and capture the output
    do_buy(["quill"])
    output = capsys.readouterr().out

    # Then: Print "Sorry, that item is not for sale."
    assert "Sorry, quill is not for sale." in output, "The statement should print"

def test_do_buy_player_does_not_have_enough_gems(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere" 

    # And: add an item that is for sale in the current place with a price and 'buy' command
    adventure.ITEMS["sword"] = {"name": "short sword", "price": -60}
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["buy"],
        "items": ["sword"],
    }

    # And: Player does not have enough gems
    adventure.PLAYER["inventory"]["gems"] = 50

    # When: call do_buy("sword") to see if Player can afford the item and capture output
    do_buy(["sword"])
    output = capsys.readouterr().out

    # Then: Print "Sorry, you can not afford that sword."
    assert "Sorry, you can not afford sword because it costs 60 gems and you only have 50 gems." in output, "The statement should print out"

def test_do_buy(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"

    # And: add an item that is for sale in the current place with a price and 'buy' command
    adventure.ITEMS["sword"] = {"name": "short sword", "price": -30}
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["buy"],
        "items": ["sword"],
    }
    # And: Player has enough gems
    adventure.PLAYER["inventory"]["gems"] = 50

    # When: call do_buy("sword") to buy the item and capture output
    do_buy(["sword"])
    output = capsys.readouterr().out

    # Then: print "You bought a sword"
    assert "You bought a sword" in output, "The statement should print"

    # And: item is in Player inventory
    assert adventure.PLAYER["inventory"]["sword"] == 1, "Player should have 1 sword in their inventory."
    
    # And: gems are subtracted from Player previous total
    assert adventure.PLAYER["inventory"]["gems"] == 20, "Player inventory should have 20 gems after buying a sword."

    # And: item is no longer in current place
    assert adventure.PLACES["somewhere"]["items"] == [], "The items list should be empty when the sword in bought."

@pytest.mark.parametrize(
    ["key", "description"], [
        ("quill", "a writing untensil"),
        ("belt buckle", "holds your belt together"),
    ]
)
def test_do_examine(capsys, key, description):
    # Given: Player is in a current place
    adventure.PLAYER["place"] = "somewhere"

    # And: adding an item to current place so Player can examine the item
    adventure.PLACES["somewhere"] = {
        "name": "somewhere out there",
        "items": [key],
    }
    adventure.ITEMS[key] = {
        "name": key,
        "description": description
    }

    # When: call do_examine with the key and capture the output
    do_examine([key])
    output = capsys.readouterr().out

    # Then: Print the description of the item
    assert description in output, "The statement should print"

def test_do_examine_item_in_inventory(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"

    # And: add the item to Player's inventory
    adventure.PLAYER["inventory"] = {"neurolizer": 1}

    # And: add the item to the ITEMS dictionary with description 
    adventure.ITEMS["neurolizer"] = {
        "name": "neurolizer",
        "description": "A gadget the size of a pen that erases memory in the set parameters"
    }
    # And: the item is not in the current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": [],
    }
    # When: call item with do_examine("item") from Player's inventory to examine and capture output
    do_examine(["neurolizer"])
    output = capsys.readouterr().out

    # Then: print item name and description
    assert "A gadget " in output, "The statement should print"

def test_do_examine_item_not_in_inventory_current_place(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"
    # breakpoint()
    # And: add an item not in current place
    adventure.PLACES["somewhere"] = {
        "name": "anywhere but here",
    }
    adventure.ITEMS["neurolizer"] = {"name": "neurolizer",}

    # When: call do_examine("item") and capture output
    do_examine(["neurolizer"])
    output = capsys.readouterr().out

    # Then: an error message should print that there it does not know what Player wants to examine
    assert "Sorry, I don't know " in output, "The error statement should print"

def test_do_examine_can_shop(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"

    # And: Player can shop in the current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere out there",
        "can": ["shop"],
        "items": ["sword"],
    }
    # And: items are for sale in current place
    adventure.ITEMS["sword"] = {"name": "short sword", "description": "leaf shaped double bladed", "price": -30}

    # When: call do_examine ["sword"] and capture output
    do_examine(["sword"])
    output = capsys.readouterr().out
    # breakpoint()
    # Then: price of each item will show up
    assert "30 gems" in output, "price -30 should print out"

def test_do_examine_item_not_for_sale(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"

    # And: there is an item that is in the current place but is not for sale
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["buy"],
        "items": ["quill"],
    }
    adventure.ITEMS["quill"] = {"name": "quill", "description": "a writing utensil that uses ink",}

    # When: call do_exanine ["quill"]
    do_examine(["quill"])
    output = capsys.readouterr().out

    # Then: the description should print
    assert "a writing utensil that uses ink" in output, "The description should print"

    # And: no price should print
    assert "gems" not in output, "No price should print"

def test_do_examine_player_inventory_item_quantity(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"

    # And: an item is in Player's inventory
    adventure.PLAYER["inventory"] = {"neurolizer": 99}

    # And: the inventory item exists
    adventure.ITEMS["neurolizer"] = {
        "name": "neurolizer",
        "description": "A gadget the size of a pen that erases memory in the set parameters"
    }

    # And: item is not in current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": [],
    }

    # When: the Player examines the item
    do_examine(["neurolizer"])
    output = capsys.readouterr().out
    # breakpoint()
    # Then: item description should be printed 
    assert "A gadget " in output, "The statement should print"

    # And: quantity in inventory should be printed
    assert "99" in output, "The quantity of the item should print"

# @pytest.mark.skip(reason="work in progress (12.2)")
def test_do_read_no_args(capsys):
    # Given: Player is in current place 
    adventure.PLAYER["place"] = "somewhere"
    # When: Player tries to read without any args
    do_read([])
    output = capsys.readouterr().out
    # Then: "Trying to read" should be in output
    assert "Trying to read" in output
    assert "What do you want to read?" in output

def test_do_read_missing_item(capsys):
    # Given: Player is in current place
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items":[],
    }
    # When: the item to read is missing
    do_read(["bottle"])
    output = capsys.readouterr().out
    # Then: a message should print "Trying to read"
    assert "Trying to read" in output
    # And: a message should print "Sorry, I don't know what this is"
    assert "Sorry, I don't know what this is:" in output

def test_do_read_unreadable_item(capsys):
    # Given: Player is in the current place
    adventure.PLAYER["place"] = "somewhere"
    # And: add an unreadable item to the current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": [],
    }
    # And: add a fake item to the current place
    adventure.ITEMS["bottle"] = {
        "name": "bottle",
    }
    place_add("bottle")

    # When: the item is unreadable
    do_read(["bottle"])
    output = capsys.readouterr().out

    # Then: a message should print "This item can't be read."
    assert "Sorry, I can't read bottle" in output

def test_do_read_in_place(capsys):
    # Given: Player is in the current place
    adventure.PLAYER["place"] = "somewhere"

    # And: add an item to the current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": [],
    }

    # And: add a fake item to the current place
    adventure.ITEMS["bottle"] = {
        "name": "bottle",
        "title": "Bottle Label",
        "message": (
            "Directions for use:",
            "Apply liberally to infected area.", 
            "If infected area gets worse discontinue use and break bottle over your enemy's head."
            ),
    }
    place_add("bottle")

    # When: the item is readable
    do_read(["bottle"])
    output = capsys.readouterr().out

    # Then: The statement "Bottle Label" should print
    assert "Bottle Label" in output
    # Then: The statement "Drink Me" should print
    assert "    Directions for use:" in output
    # Then: the statement "Directions for use:" should print with two blank lines and 4 indentation spaces.
    assert "\n\n    Directions for use:" in output

def test_do_read_in_inventory(capsys):
    # Given: Player in current place
    adventure.PLAYER["place"] = "somewhere"

    # And: item is not in current place
    adventure.PLACES["somewhere"] = {
        "name": "somewhere",
        "items": [],
    }
    # And: the inventory item exists
    adventure.ITEMS["bottle"] = {
        "name": "Bottle",
        "title": "Bottle Label",
        "message": "Drink Me",
    }

    # And: add an item to Player's inventory
    adventure.PLAYER["inventory"] = {"bottle": 1}

    # When: item is in inventory when Player reads it
    do_read(["bottle"])
    output = capsys.readouterr().out
    lines = output.splitlines()
    # breakpoint()
    # Then: the statement "Bottle Label" should print
    assert "Bottle Label" in output
    # Then: the statement "Drink Me" should print
    assert "Drink Me" in output
    # Then: the statement "    Drink Me" should print with the indent
    assert lines[-2].endswith("Drink Me")

@pytest.mark.parametrize(
        ["start", "amount", "result", "message"], [
        (50, 30, 80, "adding to current Player health"),
        (50, -30, 20, "subtracting from current Player health"),
        (50, -60, 0, "abort game when Player health is 0"),
        ]
)
def test_health_change(start, amount, result, message):
    # Given: Player's current quantity of health
    adventure.PLAYER["health"] = start
    # When: call health_change with a quantity arg
    health_change(amount)
    # Then: should add the health quantity to Player's health inventory
    assert adventure.PLAYER["health"] == result, message
    

# @pytest.mark.skip(reason="work in progress (12.6)")
def test_wrap(capsys):
    # Given: that you have a long string
    text = ("Directions for use: Apply liberally to infected area. if infected area gets worse discontinue use and break bottle over your enemy's head.")
    # When: you call the function on that string
    wrap(text) 
    # Then: the long string should be printed wrapped
    output = capsys.readouterr().out
    lines = output.splitlines()
    # Then: Length of the lines should be greater than 1
    assert len(lines) > 1
    # Then: the statement "Directions for use:" should print
    assert lines[0].startswith("  Directions for use:")
    # Then: the statement "over your enemy's head." should print
    assert lines[-2].startswith("  over your enemy's head.")

def test_wrap_with_indent(capsys):
    # Given: the item has a long string of text
    text = ("Directions for use: Apply liberally to infected area. if infected area gets worse discontinue use and break bottle over your enemy's head.")
    # When: you call the function on that string
    # breakpoint()
    wrap(text, indent = 2)
    output = capsys.readouterr().out
    lines = output.splitlines()
    # Then: the statement "Directions for use:" should print
    assert lines[0].startswith("    Directions for use:")
    # Then: the statement "bottle over your enemies head." should print
    assert lines[-2].startswith("    bottle over your enemy's head.")

def test_wrap_with_iterable(capsys):
    # Given: an item has iterable text
    message = (
        "This is the song that never ends",
        "It goes on and on my friend",

        "Some people started singing it not knowing what it was",
        "And they just kept on singing it forever just because",

        "This is the song that never ends",
    )

    # When: call wrap() with message as an argument
    wrap(message)
    output = capsys.readouterr().out

    # Then: the statement "This is the song that never ends" should print
    assert "This is the song that never ends" in output
    # Then: the statement "This is the song that never ends" should print without parentheses
    assert "(" not in output
    # Then: the statement "This is the song that never ends" should print with 2 blank lines and 4 indented spaces
    assert "\n\n  It goes on and on my friend" in output

# def test_setup_aliases():
    # ...
    # Given: there are aliases for each item in the ITEMS dictionary
    # When:
    # Then:

###############################################
# example of how to test an expected exception
###############################################

# a function that raises an exception sometimes
def func(something=None):
    if not something:
        # ValueError is the exception class
        raise ValueError("you can't do that!")
    return something

# a normal test, where the exception is not raised
def test_func():
    result = func("hello")
    assert result == "hello"
    
# test for the expected exception
def test_func_when_no_arg():
    # put the exception class inside the pytest.raises() parens
    # ex is an object containing the exception that was raised
    with pytest.raises(ValueError) as ex:  # "for the following code, we expect an exception to be raised"
        # the code that you expect to raise the exception goes here
        func()

    # ex.value is the actual exception that was raised
    # convert it to a string to see the exception message
    assert str(ex.value) == "you can't do that!"

#########################################################
# example of with statement to open a file
#########################################################

# without a with statement
# fp = open("something.txt")
# text = fp.read()
# fp.close()
# print(text)

# # using a with statement
# with open("something.txt") as fp:   # "for as long as this file is open"
#     text = fp.read()

# print(text)

    
def test_teardown():
    assert "lembas" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."
 

