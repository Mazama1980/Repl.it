pick = 34

import random

guess = random.randint(1,100)

print("The computer guessed ", guess)

if guess == pick:
  print("The computer got it right!")

elif guess > pick - 30 and guess < pick + 30:
  print("The computer got close.")

else:
  print("Try again.")


  