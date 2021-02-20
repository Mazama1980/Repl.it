"""Icecream Flavors. Created 2/8/21"""

#flavors is a list of 7 string values.
flavors = ["Banana", "Chocolate", "Lemon", "Pistachio", "Raspberry", "Strawberry", "Vanilla"]

#i is an integer for increments set to zero
i = 0

#while is a loop. "i" is set to 0. len is tracking the length of the list called
#flavors which is 7 items. So while i is less than 7 then the while loop will keep looping.
while i < len(flavors):
  
  #print statement is to print the values. 
  #1st loop:
  #i + 1 rewritten as 0 + 1 which would = 1  
  #flavors[i] is Banana
  #output would be 1 banana
  #2nd loop:
  #Each loop will increment by 1. Flavors will be called and then incremently with the i in the brackets. 
  print(i + 1, flavors[i])

  #this is where i gets incremented and the value is changed so that when it repeats the loop 
  #there is a finite set of values according to the len function of the list.
  i += 1

