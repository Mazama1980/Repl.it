"""Loop Patterns practice exercise 3 'The Twelve Days of Christmas' 
Created 1/12 - 1/18/21."""

days = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 
"Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]

gifts = ["Partridge in a pear tree", "Turtle doves", "French hens", 
"Calling birds", "Golden rings", "Geese a laying", 
"Swans a swimming", "Maids a milking", "Ladies dancing", 
"Lords a leaping", "Pipers piping", "Drummers drumming"]
#for word in days:
  #print( "On the", len(days), "of Christmas, my true love sent to me....")

#add the appropriate day into the lyric line

d = 0

while d < len[days]:
  g = 0
  while g < len[gifts]:
    print("On the", days[d], "of Christmas, my true love sent to me....", gifts[g], "\n")
    g += 1
    #l = 0
    #while l < len(lyric):
      #print(days[d], gifts[g], lyric)
      #l += 1
  print()
  d += 1