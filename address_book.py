"""address book exersize."""

# Goal
# ----
# [x] Ask the user if they want to list or add contacts. 
#     Examples:
#     [p]rint, [a]dd: 
#     Would you like to PRINT or ADD?
# [x] If the users wants to add contacts, do the above.
# [x] If the user wants to list the contacts
#     [x] open the data/contacts.txt file and print every line.
# [ ] search contacts
#     [x] Now ask the user if they want to list, add, or search contacts.
#     [x] If the user chooses search, then ask them what they want to search for.
#     [x] Open the file 
#         [x] loop through each line. 
#         [x] If the line contains the text that they entered, print the line.
#         Hint: use the in operator.
#     Bonus:
#     [ ] Make the search cases insensitive by changing both the user input and the line to lower case
#     [ ] If nothing was found, print a message that no matching contacts were found.


FILENAME = "data/contacts.txt"

def add_contact(name, phone):
    fh = open(FILENAME, "a")
    fh.write(f"{name} {phone}\n")
    fh.close()

def main():
    print("Would you like a printed list of the contacts, or to add to the contacts?", "[p]rint, [a]dd, [s]earch")
    choice = input()
    if choice == "a":
       name = input("What is your name?")
       phone = input("What is your phone number?") 
       add_contact(name, phone)
    elif choice == "p":
        fh = open(FILENAME)
        for line in fh.readlines():
            print(line, end="")
        fh.close()
    elif choice == "s":
        question = input("What would you like to search for?")
        fh = open(FILENAME)
        for line in fh.readlines():
            if question in line:
                print(line)
        fh.close()


main()


