firstName = input("Please enter a your first name:")

while not (firstName.isalpha()):
    print("invalid name")
    firstName=input("Please enter a valid name:")

lastName = input("Please enter a your last name:")

while not (lastName.isalpha()):
    print("invalid name")
    lastName=input("Please enter a valid name:")

ID = input("Please enter your IC number:")

while not ( ID.isdigit()) and len(ID)==12:
    print("Invalid ID")
    ID = input("Please enter your ID")
    





