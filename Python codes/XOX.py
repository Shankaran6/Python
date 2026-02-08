def selector():
    if ask<5:
        enter= ask+4
    else:
        enter= ask-4
    if enter in table[1]:
        table[1][table[1].index(enter)]="O"
    elif enter in table[2]:
        table[2][table[2].index(enter)]="O"


import random
table=[[0],[1,3,5,7],[2,4,6,8]]
number1=[0,1,2,3]
number2=[0,1,2,3]
x=0

ask=int(input("Please enter the position of X:"))
if ask==0:
    table[0][0]="X"
    enter=random.choice(number1)
    number1.remove(enter)
    table[1][enter]="O"
print(table)

ask=int(input("Please enter the position of X:"))
if ask in table[1]:  
    enter=table[1].index(ask)  
    table[1][enter]="X"
    number1.remove(enter)
    selector()

print(table)

ask=int(input("Please enter the position of X:"))
if ask in table[1]:  
    enter=table[1].index(ask)  
    table[1][enter]="X"
    number1.remove(enter)

    for k in range (0,3):
        if table[1][k]=="X" and table[1][k+1]=="X":
            table[2][k+1]=="O"
        else:
            n=random.choice(number2)
            table[2][n]=="O"

print(table)

ask=int(input("Please enter the position of X:"))
if ask in table[2]:  
    enter=table[2].index(ask)  
    table[2][enter]="X"
    number2.remove(enter)

print(table)
    
    










        

