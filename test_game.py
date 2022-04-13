from adventure import (
    is_for_sale,
    inventory_change,
    do_take
)
import pdbr
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


def test_truth():
    assert True


def test_is_for_sale():
    fake_item = {
        "name": "art",
        "price": -20
    }
    result = is_for_sale(fake_item)
    assert result, "is_for_sale() should return True if the item has a price"

def test_inventory_change():
    adventure.PLAYER["inventory"]["lembas"] = 99
    inventory_change("lembas")
    assert adventure.PLAYER["inventory"]["lembas"] == 100, f'inventory_change() with no quantity argument shoud add 1.'

def test_inventory_change_with_quantity():
    adventure.PLAYER["inventory"]["lembas"] = 99
    inventory_change("lembas", 2)
    assert adventure.PLAYER["inventory"]["lembas"] == 101

def test_inventory_change_missing_key():
    adventure.PLAYER["inventory"] = {}
    inventory_change("lembas")
    # breakpoint()
    assert "lembas" in adventure.PLAYER["inventory"], f"inventory_change() should add missing keys to the inventory."
    assert adventure.PLAYER["inventory"]["lembas"] == 1, f"inventory_change() with no quantity argument should add 1."
    
def test_inventory_change_remove():
    adventure.PLAYER["inventory"]["lembas"] = 5
    inventory_change("lembas", -6)
    assert "lembas" not in adventure.PLAYER["inventory"], f"inventory_change() subtracting quantity <= 0 will remove key or item."

def test_teardown():
    assert "lembas" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."
 

