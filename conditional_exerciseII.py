import random
num = random.randint(1,100)

if num % 2 == 0 and num % 10:
	print("you guessed wisely", num)
else:
  print("Guess again")