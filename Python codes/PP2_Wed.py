with open("PP2_Wed.txt") as file:
    Lines=[line.strip() for line in file.readlines()]
import re
n=int(Lines[0])
Data=Lines[1:]
for i in range(n):
    stacks=[]
    for k in range(1,len(Data[i])+1):
        string=""
        stacks.append(Data[i][-k])
    z=0
    string=""
    multiply=""
    while z <len(stacks):
        current=stacks.pop()
        if current.isdigit():
            multiply+=current
        else:
            if multiply=="":
                multiplier=1
            else:
                multiplier=int(multiply) 
        if current=="[":
            skip=0
            for j in range(1,len(stacks)+1):
                if stacks[-j]=="[":
                        skip+=1
                if stacks[-j]=="]":
                    if skip==0:
                        a=len(stacks)-j
                        stacks=stacks[:a]+stacks[a+1:]*multiplier
                        multiply=""
                        break
                    else:
                        skip-=1
        if current.isalpha():
            string+=current*multiplier
            multiply=""
    print(string)
        
            


        

            

        
        
    


        



