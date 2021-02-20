
#Make a list of five songs
#Print the second song on the list
#Print the last song on the list
#Use concatenation to add two more songs to the list
#Use a slice to remove the last song on the list

songs = [ "Hello", "Goodbye", "Forever", "River", "Rain"]
print(songs[1])
print(songs[-1])

songs += ["Ocean", "Arizona"]

print(songs)

songs = songs[:-1]
print(songs)



