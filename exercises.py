def exercise(number,name):
  print()
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print(number +")",name)
  print()

exercise("1","Groceries")
groceries=[
    "butter", 
    "cheese", 
    "bread", 
    "deli turkey",
]
for food in groceries:
  print(food)

exercise("2","Favorites")

colors={
    'primary':"Blue",
    'hue':"Ultramarine",
    'favorite':"Purple",
  }
colors['primary']

favorites={
  'color':"Purple",
  'food':"Soup",
  'season':"Fall",
}
for key, value in favorites.items():
  print("My favorite", key, "is", value)
  
exercise("3","Bottles of beer")
for i in range(99, 88, -1):
  print(i, "Bottles of beer on the wall")


 
