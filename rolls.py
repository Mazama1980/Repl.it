import random

rolls = []
number = 0
while True:
  number = random.randint(1,6)
  print("You rolled", number)
  reply = input("Keep your roll? ")
  if reply == "n":
    continue
  if reply == "q":
    break
  rolls.append(number)
print(rolls)