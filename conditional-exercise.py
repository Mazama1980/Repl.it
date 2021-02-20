import random
num = random.randint(1,100)

if num > 50:
  print("Number greater than 50")
elif num % 2 == 0:
  print("Number is an even number")
elif num % 2 != 0:
  print("Number is odd")

print(num)


  