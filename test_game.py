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

def test_do_shop_with_no_shop_key(capsys):
    # Given: the Player is in a current place
    adventure.PLAYER["place"] = "somewhere"

    # And: the current place does not have the 'can':'shop' key
    adventure.PLACES["somewhere"] = {"name":"Somewhere out there"}

    # TODO: we may want to add another test at some point that tests both if the
    # "can" key is missing AND if the "shop" key is missing from the "can" list
    # (like below). But we've tested it both ways manually for now, so that's
    # good for now.
    adventure.PLACES["somewhere"]["can"] = []

    # When: call do_shop() and capture the output
    do_shop()
    output = capsys.readouterr().out

    # And: an error message saying there are no items to shop for in the current place should print under the header
    assert "Sorry, you can't shop here." in output, "The statement should print"


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
    assert "No items in this place" in output, "The statement should print under the header"

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

# @pytest.mark.skip(reason="to be implemented")
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


def test_teardown():
    assert "lembas" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."
 

