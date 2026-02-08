num_of_stu=int(input("Please enter the numeber of students"))
num_of_subjects=int(input("Please enter the numeber of subjects"))

students=[[] for _ in range (num_of_stu)]
subjects=[]

k=0
while k< num_of_subjects:
    subject=str(input("Please enter the name of subjects:"))
    subjects.append(subject)
    k+=1
i=0
j=0
while i< num_of_stu:
    name=str(input("Please enter your name"))
    students[i].append(name)
    j=0
    while j< num_of_subjects:
        marks=int(input("Please enter marks:" ))
        students[i].append(marks)
        j+=1
    i+=1
total=[]
for i in range (0,num_of_stu):
    l=sum([i],students[1:num_of_subjects])
    total.append(l)
print(total)
    
    

