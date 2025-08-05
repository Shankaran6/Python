print("Customer registration system")
n = int(input("Please enter the total number of members in team"))
names =[]
passwords=[]
c=0
attempt=0
while c < n:
    func= str(input("Please enter R for registering and L for login"))
    if func == "R":
        name = str(input("Please enter the name of member"))
        names.append(name)
        c+=1
        print(len(names),"is your number")
        password= str(input("Please enter password"))
        passwords.append(password)
    elif func =="L":
        num=int(input("please enter your number"))
        print(f"Good morning {names[num-1]}.")
        pas = str(input("please enter your password:"))
        while attempt<5:
            if pas == passwords[num-1]:
                print("logged in")
                attempt=0
            else:
                print("Incorrect password")
                attempt+=1









    
    