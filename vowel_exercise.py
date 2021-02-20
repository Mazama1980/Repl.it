word = input("Enter a word: ")

i = 0
while i < len(word):
  if word[i] in ["a","e","i","o","u"]:
    print("letter", i, "is", word[i])
  i += 1