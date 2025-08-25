# 5 students take 3 subjects
# marks stored (total 15 marks)
#Out put - 
# Student name - Maths , physics , chemistry , total , average , results

heading=["Name", [], "Total", "Average", "Results"]
sub_num=int(input("Please enter the number of subjects:"))
stu_num=int(input("Please enter the number of students:"))

Student_name=[]
Students_marks=[[] for _ in range(stu_num)]
Student_calc=[[],[],[[]for _ in range(stu_num)]]
n=0
while n<sub_num:
    name_subject=str(input("Please enter the name of the subject:"))
    heading[1].append(name_subject)
    n+=1

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
    Student_calc[2][n].append(results)
total=0
n=0
while n <stu_num:
    name=str(input("Please enter the name of student:"))
    Student_name.append(name)
    m=0
    while m< sub_num:
        marks=int(input(f"Please enter the student's {heading[1][m]} marks:"))
        total+=marks
        Students_marks[n].append(marks)
        marking()
        m+=1
    n+=1
    average=total/sub_num
    Student_calc[1].append(round(average,2))
    Student_calc[0].append(round(total,2))
    total=0
    average=0
n=0
print("-"*15*(sub_num+3))
print(f"{heading[0]:<12}", end='')
while n<sub_num:
    print(f"{heading[1][n]:>12}", end='')
    n+=1
print(f"{heading[2]:>12}{heading[3]:>12}{heading[4]:>14}")
print("-"*15*(sub_num+3))
    
n=0
while n<len(Student_name):
    print(f"{Student_name[n]:<12}",end='')
    m=0
    while m < sub_num:
        print(f"{Students_marks[n][m]:>12}",end='')
        m+=1
    k=0
    while k<3:
        if k<2:
            print(f"{Student_calc[k][n]:>12}",end='')
        else:
            print(end="        ")
            s=0
            while s<3:
                print(f"{Student_calc[2][n][s]}",end='')
                s+=1

        k+=1
    
    n+=1
    print("")
    

    






    
