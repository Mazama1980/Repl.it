"""address book exersize."""

# Goal
# ----
# [x] Ask the user if they want to list or add contacts. 
#     Examples:
#     [p]rint, [a]dd: 
#     Would you like to PRINT or ADD?
# [x] If the users wants to add contacts, do the above.
# [x] If the user wants to list the contacts
#     [x] open the contacts.txt file and print every line.


def add_contact(name, phone):
    fh = open("contacts.txt", "a")
    fh.write(f"{name} {phone}\n")
    fh.close()

def main():
    print("Would you like a printed list of the contacts, or to add to the contacts?", "[p]rint, [a]dd")
    choice = input()
    if choice == "a":
       name = input("What is your name?")
       phone = input("What is your phone number?") 
       add_contact(name, phone)
    elif choice == "p":
        fh = open("contacts.txt")
        for line in fh.readlines():
            print(line, end="")
        fh.close

main()


