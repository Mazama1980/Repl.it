****
# To Do

## future to learn / do

[ ] add annotations and docstrings to 1-2 functions until they are all done
[ ] add tests for
    [ ] place_has()

### Part 10.2 (tests)

[x] write a test_place_can_true() test
[x] in it, make a fake place that has a "can" key that contains a fake command string
[x] call it with that string
[x] assert that it is true

[x] write a test_place_can_false() test
[x] figure out how to write this test

[x] do 10.2 A
[x] do 10.2 C
[x] write test for do_buy() command
[-] do 10.3
[x] finish do_buy() (to add the message about how many gems the player has and
    the price of the item)
[x] Fix inventory_change() as per failing test: test_inventory_change_with_negative_quantity
[x] write a test_do_buy_actually_buy() for when the user really buys it
[x] finish do_buy() to actually buy the item
[x] 10.4 do the string formatting for the do_shop function list that prints out
[ ] add tests for any do_*() functions that deal with items to include quotes in
    the key name, for example do_examine()
[x] change tests to reflect changes made to 'key' and 'name' in the game functions
[x] change your all your "name" keys in your ITEMS dictionary to be "summary"
[x] go through all your do_*() functions to see where item["name"] is used, and see if you meant to use "name" or "summary"
[x] change formatting on inventory
[x] add tests for do_examine:
    [x] when item is in the current place
    [x] when item is in inventory
    [x] when item not in inventory or the current place
[x] Look at the way items are printed in the following commands, and check that
    you are using the item["name"], item["key"], item["summary"], and
    item["description"] correctly
    [x] do_examine()
    [x] do_take()
    [x] do_buy()
    [x] do_drop
[ ] Do 10.4 C
[ ] Do 10.4 D

### Aliases function

[ ] write a test_setup_aliases() test
    [ ] ...
[ ] write a function setup_aliases() 
    [ ] write a for loop iterating over ITEMS.items() getting two variables `key` (str) and `item` (dict)
        [ ] nest a for loop iterating over item['aliases'] (list) getting the variable `alias` (str)
            [ ] add to ITEMS_ALIASES (dict) with the key `alias`(str) and the value `item` (dict) 
    [ ] add to ITEMS_ALIASES with the key `key` (str) and the value `item` (dict)
[ ] add ITEMS_ALIASES to tests and call setup_aliases() in tests (Alissa to figure this part out)
[ ] add 'aliases' key to each item where needed in the ITEMS dicionary
    [ ] add a list of possible words for each item as a dictionary in the 'aliases' key   
[ ] make a new global dicitionary ITEMS_ALIASES that's empty    
[ ] write or modify a test_get_item() test to reflect pulling from ITEM_ALIASES
    [ ] make sure it works with the original item key, any alias in the aliases list, and for items with no "aliases" key
[ ] change the get_item() function to get items from ITEMS_ALIASES instead of ITEMS
[ ] call the function setup_aliases() in main()
[ ] might need to change some tests if any of them broke

```python
# imaginary ITEMS dict
ITEMS = {
    "crystal ball": {
        "key": "crystal ball",
        "aliases": ["ball", "globe"],
        "name": "Crystal ball",
        "summary": "a faintly glowing ball",
        "description": "all it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "book": {
        "key": "book",
        "name": "Book",
        "summary": "Diary of a wimpy dragon",
        "description": "A soft leather bound book laying on the desk at home. There may be useful information in it.",
        "can_take": True,
    },
}

# before
ITEMS_ALIASES = {}

def setup_aliases():
    ...

crystal_ball = ITEMS.get("crystal ball")
book = ITEMS.get("book")

# AFTER (but modified by setup_aliases(), not hard-coded)
ITEMS_ALIASES = {
    "crystal ball": crystal_ball,
    "ball": crystal_ball,
    "globe": crystal_ball,
    "book": book,
}

# if the user types any of these, it should work
# buy "crystal ball"
# buy globe
```
