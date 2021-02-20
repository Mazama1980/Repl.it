"""Loop patterns - nested loops exercise 1/11/12.
11/18: Great job! --Alissa
"""

rows, cols = 9, 9
r = 1
while r <= rows:
  #print("rows:", r) 
  c = 1
  while c <= cols:
    #print("cols:", c)
    output = r * c
    #print(r, "x", c, "=", output)
    print(output, "", end="")
    c += 1
  print()
  r += 1
