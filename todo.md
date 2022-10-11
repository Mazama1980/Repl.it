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
[ ] add tests for do_examine:
    [x] when item is in the current place
    [ ] when item is in inventory
    [ ] when item not in inventory or the current place
[ ] Look at the way items are printed in the following commands, and check that
    you are using the item["name"], item["key"], item["summary"], and
    item["description"] correctly
    [ ] do_examine()
    [ ] do_take()
    [ ] do_buy()
    [ ] do_drop
[ ] Do 10.4 C
[ ] Do 10.4 D
