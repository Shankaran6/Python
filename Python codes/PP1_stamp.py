Cases=[]
Requirement=[]
Stamps=[]

def getText(filepath):
    with open(filepath) as file:
        for line in file:
            Cases.append(line.split())

def addMax(Stamp,Requirement):
    run=True
    Donors=0
    sum_of_stamps=0
    while run:
        if len(Stamp)>0:
            sum_of_stamps+=max(Stamp)
     
            Donors+=1
            Stamp.remove(max(Stamp))
        else:
            print("IMPOSSIBLE")
            run=False
        if sum_of_stamps>=Requirement:
            run=False
            print("Yes",Donors)
    
getText("PP1_stamp.txt")  

number_of_cases=int(Cases[0][0])
Stamps_int=[[] for _ in range(number_of_cases)]
Requirement_int=[[] for _ in range(number_of_cases)]
for i in range(number_of_cases):
    Requirement.append(Cases[i*2+1])
    Stamps.append(Cases[i*2+2])

for i in range(number_of_cases):
    Stamps_int[i]=list(map(int,Stamps[i]))
    Requirement_int[i]=list(map(int,Requirement[i]))

for i in range(number_of_cases):
    addMax(Stamps_int[i],Requirement_int[i][0])


            

        

        

            
        

            