Data=[]

def getText(filepath):
    with open(filepath, "r") as file:
        for line in file:
            if not line.strip():
                continue
            else:
                Data.append(line.strip())

getText("/Users/shankaranguruparan/Documents/GitHub/Python/Python codes/Stacks.txt")

Stacks=[]

Stacks=Data[2].split(' ')
int_stacks=[int(x) for x in Stacks]
print(int_stacks)

total_bricks=sum(int_stacks)
print(total_bricks)
total_to_be_moved=0
height=total_bricks/int(Data[1])
for i in range(0,int(Data[1])):
    if int_stacks[i]-height>0:
        total_to_be_moved+=int_stacks[i]-height
    else:
        continue
print(int(total_to_be_moved))

with open('Result.txt','w') as file:
    file.write("Total bricks that need to be moved is "+str(total_to_be_moved))
print("File updated")



                