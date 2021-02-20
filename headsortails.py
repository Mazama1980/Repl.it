"""Ask the user to choose heads or tails until they do.

Completed: 1/5/2021

An exercise for the loops lesson found here:
https://alissa-huskey.github.io/python-class/lessons/loops.html
"""


#user = input("Choose heads or tails")

#if input (""):
 #print("You must choose.")
#if user in [heads,tails]:
  #print("Thank you.")
#else:
  #print("Please choose heads or tails.")

user = ""
while user not in ["heads","tails"]:
  user = input ("You must choose.")