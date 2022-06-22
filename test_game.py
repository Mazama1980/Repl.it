from adventure import (
    is_for_sale,
    inventory_change,
    do_take,
    do_drop,
    place_has,
    get_place,
    place_add,
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

def test_inventory_change():
    # Given: Item and quantity Player's inventory
    adventure.PLAYER["inventory"]["lembas"] = 99

    # When: call inventory_change for item with no quantity argument
    inventory_change("lembas")

    # Then: should add one to quantity to Player's inventory
    assert adventure.PLAYER["inventory"]["lembas"] == 100, f'inventory_change() with no quantity argument shoud add 1.'

def test_inventory_change_with_quantity():
    # Given: Item and quantity to Player's inventory
    adventure.PLAYER["inventory"]["lembas"] = 99

    # When: call inventory_change with item and specific quantity
    inventory_change("lembas", 2)

    # Then: should add the specific quantity to the Player's inventory of that item
    assert adventure.PLAYER["inventory"]["lembas"] == 101

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

    
    
def fake_function(text):
    print("Fake function says:", text)


# To test printed output:
# 1. Pass capsys to your test function as a parameter
# 2. After the code that should print something, get the output with:
#    output = capsys.readouterr().out
# 3. Write an assertion like you normally would

def test_fake_thing(capsys):
    # WHEN: You call the fake_function() with a string
    fake_function("hello")

    # this gets the text that would have been printed to the screen
    output = capsys.readouterr().out

    # THEN: A message containing that string is printed
    assert "hello" in output, "the message is printed"


def test_teardown():
    assert "lembas" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."
 

