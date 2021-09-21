"""Exercise 34 (String Formatting)

Use the format() function to:

Format the number 48.7052 to two decimal points.

Format the number 2.5 to two decimal points.

Format .25 to 25%

Truncate the string "September" to a width of 3 characters

Center the string "Game Over" to a width of 80

Right align the text "8 of 10" to a width of 80

Left align the string "Question" with a fill character of "=" to a width of 30 characters.."""

format(48.7052, ".2f")
format(2.5, ".2f")
format(.25, ".0%")
format("September", ".3s")
format("Game Over", "^80")
format("8 of 10", ">80")
format("8 of 10", "<80")
format("Question ", "=<30")

# left align uses "<", which looks like an arrow pointing to the left:    "<--------"
# right align uses ">", which looks like an arrow pointing to the right:   "-------->"
# center uses "^", where the smallest part of the arrow is in the middle