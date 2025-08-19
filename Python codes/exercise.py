months=["Months","January","February","March","April","May","June","July","August","September","October","November","December"]
Salary=["Salary",100000,150000,45000,80000,120000,400000,180000,250000,70000,60000,50000,300000]
Taxes=["Taxes"]
netsalary=["Net salary"]
i=0
totalsalary=0
# while i <12:
#     salary = int(input(f"Please enter your salary for {months[i]}:"))
#     Salary.append(salary)
#     totalsalary+=salary
#     i+=1


taxes=0
for i in range (1,13):
    totalsalary+=Salary[i]



for i in range (1,13):
    k=Salary[i]
    if k <50000:
        tax=k*3/100
    elif k <100000:
        tax = 50000*0.03 + (k-50000)*0.05
    elif k <300000:
        tax = 50000*0.03 + 50000*0.05 + (k-100000)*0.08
    elif k>300000:
        tax = 50000*0.03 + 50000*0.05 + 200000*0.08 + (k-300000)*0.1
    Taxes.append(tax)
    netsal=Salary[i]-tax
    netsalary.append(netsal)
    taxes+=tax
    # print(f"Tax for {months[i]} is {Taxes[i]}")
    if i ==12:
        months.append("Total")
        Salary.append(totalsalary)
        Taxes.append(taxes)
        net=totalsalary-taxes
        netsalary.append(net)


    # print(f"{months[i]:<10}{Salary[i]:>12}{Taxes[i]:>12}{netsalary[i]:>12}")
for i in range (0,14):
    print(f"{months[i]:<10}{Salary[i]:>12}{Taxes[i]:>12}{netsalary[i]:>12}")
print(f"Your total salary is {totalsalary} and your total tax is {taxes}")
print(f"Your net salary is {totalsalary - taxes}")

