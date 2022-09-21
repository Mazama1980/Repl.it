
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
[ ] 10.4 do the string formatting for the do_shop function list that prints out