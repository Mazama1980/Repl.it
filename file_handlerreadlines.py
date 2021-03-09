print("Groceries")
print("=========")

fh = open("groceries.txt")
for line in fh.readlines():
    print(line, end="")

fh.close()