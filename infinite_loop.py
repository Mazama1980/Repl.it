import random

while True:
  num = random.randint(1,10)
  print("The number is", num)
  reply = input("Would you like to end? ")
  if reply == "y":
    break