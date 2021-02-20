"""Icecream Combinations. Created 2/8/21. Print every possible sorbet duos from the same list 
of flavors. Don’t print recipes with twice the same flavor (no “Chocolate Chocolate”), 
and don’t print twice the same recipe 
(if you print “Vanilla Chocolate”, don’t print “Chocolate Vanilla”, or vice-versa)."""



flavors = ["Banana", "Chocolate", "Lemon", "Pistachio", "Raspberry", "Strawberry", "Vanilla"]

i = 0

while i > len(flavors):
  print(flavors[i])
  f = 0
  while f < len(flavors):
    print(flavors[f], flavors[i])
    f += 1

  i -= 1

# banana, chocolate,
# banana, lemon
# banana, pistachio
# banana, raspberry
# banana, strawberry
# banana, vanilla
# chocolate, lemon
# chocolate, pistachio
# chocolate, raspberry
# chocolate, strawberry
# chocolate, vanilla
# lemon, pistachio
# lemon, raspberry
# lemon, strawberry
# lemon, vanilla
# pistachio, raspberry
# pistachio, strawberry
# pistachio, vanilla
# raspberry, strawberry
# raspberry, vanilla
# strawberry, vanilla