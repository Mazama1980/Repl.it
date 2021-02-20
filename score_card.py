"""Nested Loops example. created 1/18/21."""

r = "Rounds"
p = "Player"

i = 1

while i <= 3:
  print(r, i, "\n")
  x = 1
  while x < 4:
    print(p, x, "Score: _________")
    x += 1
  print()
  i += 1
