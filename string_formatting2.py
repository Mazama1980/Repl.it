"""Exercise 36 (Format email address)

Given the following values:

user = "joe"
domain = "gmail"
extension = "com"
Use .format() to print the string:

"joe@gmail.com"

Bonus: Write a format_email() function that takes three arguments, name, domain, and extension and returns a formatted email address string.
"""

user = "joe"
domain = "gmail"
extension = "com"
print("{user}@{domain}.{extension}".format(user="joe", domain="gmail", extension="com"))
print(f'{user}@{domain}.{extension}')

def format_email(user, domain, extension):
    address = f"{user}@{domain}.{extension}"
    return address

print(format_email("joe", "gmail", "com"))
print(format_email("bilbo", "dwarf", "net"))