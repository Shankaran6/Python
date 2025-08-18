names=[]
lastnames=[]
IDS=[]
numbers=[]

n = int(input("Please enter the total number of members in team"))
c=0
while c < n:
    func= str(input("Please enter R for registering and L for login"))   
    if func == "R":
        print("Your number is {}".format(len(names)+1))
        firstName = input("Please enter a your first name:")

        while not (firstName.isalpha()):
            print("invalid name")
            firstName=str(input("Please enter a valid name:"))
            
        names.append(firstName)
        lastName = input("Please enter a your last name:")

        while not (lastName.isalpha()):
            print("invalid name")
            lastName=str(input("Please enter a valid name:"))
        lastnames.append(lastName)    

        ID = input("Please enter your IC number:")

        while not ( ID.isdigit()) and len(ID)==12:
            print("Invalid ID")
            ID =str(input("Please enter your ID"))
            IDS.append(ID)

        import math

        
        year =int(ID[0:4])
        day = int(ID[4:7])
        date = int(0)

        mo= day/30
        month = math.ceil(mo)

        if day > 500:
            day = day - 500

        if day <32:
            month =1
            date = day
        elif day <61:
            date = day - 31
            month =2
        elif day <92:
            date = day - 60
            month = 3
        elif day <122:
            date = day - 91
            month = 4
        elif day <153:
            date = day - 121
            month = 5
        elif day <183:
            date = day - 152
            month = 6
        elif day <214:
            date = day - 182
            month = 7
        elif day <245:
            date = day - 213
            month = 8
        elif day <275:
            date = day - 244
            month = 9
        elif day <306:
            date = day - 274
            month = 10
        elif day <336:
            date = day - 305
            month = 11
        else:
            date = day - 335
            month = 12

        number =("{0}/ {1}/ {2}".format(year,month,date))
        numbers.append(number)

        c+=1

        
    if func =="L":
        num=int(input("Please enter the valid number"))
        
        print(names[num-1])
        print(lastnames[num-1])
        print(numbers[num-1])
        
    








