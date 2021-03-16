print("Groceries")
print("=========")

fh = open("data/groceries.txt")
for line in fh.readlines():
    print(line, end="")

fh.close()