import random

def character_info(character_name, character_level, character_title):
  if character_level < 3:
    character_rank = "novice"
    
  elif character_level <= 6:
    character_rank = "apprentice"
    
  elif character_level >= 7:
    character_rank = "master"
  print(character_name, "is a level", character_level, character_rank, character_title)
 

def character_level(character_name, character_level):
  print(character_name, "is now level", character_level)


name = "Ash"
level = random.randint(1,5)
title = "mage"

character_info(name, level, title)

level = level + 2

character_level(name, level)

level = level + random.randint(1,5)

print(name, "is now level", level)


character_info("Ansel", random.randint(1,8), "dragon slayer")

character_info("Bill", random.randint(1,8), "warrior")

character_info( "Max", random.randint(1,8), "mage")

# Inside of character_info make a new variable `rank`
# Use an if-statement to decide if the rank is:
# - novice      : less than level 3
# - apprentice  : between level 3 - 6
# - master      : level 7 or over
# Then change your print statement on line 4 so it 
#   prints something like:
# Ash is now a level 8 master mage

