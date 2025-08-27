heading=["Name", "Total", "Average", "Results"]
sub_num=int(input("Please enter the number of subjects:"))
stu_num=int(input("Please enter the number of students:"))
student_data=[]
student_marks=[[]for _ in range (stu_num)]
student_results=[[]for _ in range (stu_num)]
Student_average=[]
Student_total=[]
ranking=[]
def marking():
    if marks>75:
        results="A"
    elif marks>65:
        results="B"
    elif marks>55:
        results="C"
    elif marks>45:
        results="S"
    else:
        results="F"
    student_results[i].append(results)
for i in range(0,sub_num):
    subject=str(input("Please enter the subject name:"))
    heading.insert(-3,subject)

for i in range(0,stu_num):
    name=str(input("Please enter student's name:"))
    student_data.append(name)
    total=0
    for k in range(0,sub_num):
        marks=int(input(f"Please enter the student's {heading[k+1]} marks:"))
        total+=marks
        student_marks[i].append(marks)
        marking()
    Student_total.append(total)
    average=total/sub_num
    Student_average.append(average)

ranked=Student_average.copy()
ranked.sort(reverse=True)
Student_total.sort(reverse=True)

for i in range(0,stu_num):
    ranking.append(Student_average.index(ranked[i]))

student_data_sorted=[]
student_marks_sorted=[]
student_results_sorted=[]

for i in range(0,stu_num):
    student_data_sorted.append(student_data[ranking[i]])
    student_marks_sorted.append(student_marks[ranking[i]])
    student_results_sorted.append(student_results[ranking[i]])


n=0
print("-"*15*(sub_num+3))

while n<len(heading):
    print(f"{heading[n]:>12}", end='')
    n+=1

print("-"*15*(sub_num+3))
    
n=0
while n<len(student_data_sorted):
    print(f"{student_data_sorted[n]:<12}",end='')
    m=0
    while m < sub_num:
        print(f"{student_marks_sorted[n][m]:>12}",end='')
        m+=1

    print(f"{Student_total[n]:>12}",end='')
    print(f"{ranked[n]:>12}",end='')
    m=0
    while m < sub_num:
        print(f"{student_results_sorted[n][m]:>12}",end='')
        m+=1
    
    n+=1
    print("")
    









    
        



