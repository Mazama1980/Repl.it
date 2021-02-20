print("Fantasy Game 1")
hero = "Manly"
import random

# the goal is to modify this value every time 
# pick_up() is called
coins = random.randint(1,100)

# this function should:
#  - assign a new random number of coins to add
#  - add the new number to coins from line 7
#  - print out the number of coins that you have when it's
#    done adding them

def pick_up():
  global coins
  coins_to_add = random.randint(1,100)
  new_total = coins + coins_to_add
  print("You picked up",coins_to_add, "new coins.")
  coins = new_total
  if coins_to_add < 50:
    print("You added to your cash.")
  elif coins_to_add > 51:
    print("Wow! You found a big cache.")
  print("You now have",coins, "coins.")

pick_up()
pick_up()
pick_up()
