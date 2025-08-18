# def PrintMyName():
#     print("My name is Shankaran")
# PrintMyName()


# firstName = str(input("Please enter your first name"))
# lastName = str(input("Please enter your last name"))
# def getfullname(lastName="lastname",firstName="firstname"):
#     print(f"Your full name is {lastName} {firstName}")
#     return lastName + " " +firstName
# # getfullname("Shankaran","Guruparan")
# # getfullname("Shankaran")

# fullname= getfullname("Shankaran","Guruparan")

# print(fullname)
ammount= int(input("Please enter the deposit ammount"))

term=float(input("Please enter the term in years"))
intere=0

def calcinterest(ammount,term):
    if term == 0.25:
        intere = ammount*(12/100)*term
    elif term ==0.5:
        intere = ammount*(12.5/100)*term
    elif term == 1:
        intere = ammount*(13/100)*term
    elif term == 3:
        intere = ammount*(14/100)*term
    elif term == 5:
        intere = ammount*(15/100)*term
    elif term >5:
        intere = ammount*(15.5/100)*term
    print(int(intere))

calcinterest(ammount,term)

