
print("Welcome to coding club")

#-------------------------------------------------
# Function
#-------------------------------------------------

def show(pet):
  print('----------------------------------------')
  print('Name:  ', pet['name'])
  print('Age:  ', pet['age'])
  print('Weight: ', pet['weight'])
  print('Happy: ', pet['happy'])
  print('Photo: ', pet['photo'])

  if pet['hungry']:
    print('Hungry: ', 'Yes!')
  else:
    print('Hungry: ', 'No!')

  print('-----------------------------------------')
#----------------------------------------------------
def hr():
    print('-------------------------------------')
#----------------------------------------------------
def feed(pet):
  if pet['hungry']== True:
     pet['hungry']= False
     pet['weight']= pet['weight'] + 1
  else: 
     print('The Pypet is not hungry')
#---------------------------------------------------
def exercise(pet):
  pet['weight']= pet['weight'] - 1
#---------------------------------------------------
def treat(pet):
  pet['happy']= True

#-------------------------------------------------
# Variables
#-------------------------------------------------


cat= {
  'name': 'Fluffy',
  'happy': False,
  'age': 9,
  'weight': 9.5,
  'hungry':True,
  'photo': '(=^*.*^=)___'
}


dog= {
  'name': 'Taffy',
  'happy': False,
  'age': 5,
  'hungry': True,
  'weight': 15.5,
  'photo': '^{0g0}^,'
}


fish= {
  'name':'Kai',
  'happy': False,
  'age': 1,
  'weight': .2,
  'hungry': False,
  'photo': '<`)))><'
}


mouse= {
  'name': 'Squeak',
  'happy': False,
  'age': 2,
  'weight': 1.1,
  'hungry':True,
  'photo' :'<:3 )~~~'
}


puppy= {
  'name': 'Rocket',
  'happy': False,
  'age': 4,
  'weight': 12.5,
  'hungry': False,
  'photo': '(^0@0^)_,'
}

#-------------------------------------------------
# Main Body
#-------------------------------------------------
print('Hello ' + cat['name'])
print(cat)
feed(cat)
print(cat)

hr()
exercise(cat)
print(cat)

hr()
print('Hello ' + dog['name'])
print(dog)
feed(dog)
print(dog)

hr()
print('Hello ' + fish['name'])
print(fish)
feed(fish)
print(fish)

hr()
print('Hello ' + mouse['name'])
print(mouse)
feed(mouse)
print(mouse)

hr()
print('Hello ' + puppy['name'])
print(puppy)
feed(puppy)
print(puppy)

hr()

print(cat)
treat(cat)
print(cat)

hr()

print(dog)
treat(dog)
print(dog)

hr()

print(fish)
treat(fish)
print(fish)

hr()

print(mouse)
treat(mouse)
print(mouse)

hr()

print(puppy)
treat(puppy)
print(puppy)


show(cat)
show(dog)
show(fish)
show(mouse)
show(puppy)

pets=[
  cat,
  dog,
  fish,
  mouse,
  puppy,
]

pets=[
  cat,
  dog,
  fish,
  mouse,
  puppy
]

hr()

for pet in pets:
  feed(pet)
  show(pet)

hr()

groceries=[
  "milk",
  "corn tortillas",
  "diet Dr. Pepper",
  "beets",
  "squash",
]

print("My grocery list")

for stuff in groceries:
  print("[ ] "+stuff)

hr()

for pet in pets:
  print('Name: ' +pet['name'])
  print("Photo: " +pet['photo'])
 

    