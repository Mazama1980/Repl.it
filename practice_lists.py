"""Make lists and dictionaries. Call them with for loops and while loops."""
#list:
breeds = ["Appaloosa", "Shetland", "Fresian", "Morgan"]


breeds.append("thoroughbred")
breeds[-1] = ("Thoroughbred")

for name in breeds:
    print(name)
print()

i = 0
while i < len(breeds):
    print(breeds[i])
    i += 1
print()

#string:
text = "pumpkin time"
i = 0
while i < len(text):
    letter = text[i]
    print(i, letter)
    i += 1
for letter in text:
    print(letter)


#dictionary
hobbits = {"Frodo": "Baggins", "Sam": "Gamgee", "Merry": "Took", "Pippin": "Brandybuck"} 
print(hobbits)  
hobbits["Fatty"] = "Bolger"
hobbits["Bilbo"] = "Baggins"
hobbits["Smeagol"] = "Gollum"
print(hobbits)

for f,l in hobbits.items():
    print(f,l)


