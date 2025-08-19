# Subjects=["Math","Tamil","English","Science","IT"]


# for i in range(0,5):   # using for loop
#     print(Subjects[i],end=', ')

# print(Subjects[-5])

# print(len(Subjects))


# n=0

# while n<5:              # using while loop
#     print(f"{n+1}.",Subjects[n])
#     n+=1

# print(type(Subjects))



# n=0

# while n<5:     
#     answer= str(input(f"Do you want to change the subject {Subjects[n]}?").lower())   
#     if answer == "yes":
#         newsubject=str(input("Please enter the name of the new subject"))
#         Subjects[n]=newsubject
#         n+=1
#     else:
#         n+=1
        
        
    

# n=0
# while n<5:              # using while loop
#     print(f"{n+1}.",Subjects[n])
#     n+=1
# print(Subjects[1:3])
 
# print(Subjects[1:5])

# print(Subjects[:3])
# # print(type(Subjects))

# print(Subjects[2:])

# print(Subjects[::3])

#Non fixed salary, tax calculation - 
# 50000 -3 %
#50000 - 100000 -5 %
#100000 - 300000 - 8 %
#300000 + - 10 %
#Calculate tax for the monthly salary

Salary=[]
i=0
while i <12:
    salary = int(input(f"Please enter your salary for month {i+1}:"))
    Salary.append(salary)
    i+=1
taxes=0
for i in range (0,12):
    k=Salary[i]
    if k <50000:
        tax=k*3/100
    elif k <100000:
        tax = 50000*0.03 + (k-50000)*0.05
    elif k <300000:
        tax = 50000*0.03 + 50000*0.05 + (k-100000)*0.08
    elif k>300000:
        tax = 50000*0.03 + 50000*0.05 + 200000*0.08 + (k-300000)*0.1
    taxes+=tax
    print(f"Tax for the month {i+1} is {tax}")
print(f"Your total tax is {taxes}")
    

        
