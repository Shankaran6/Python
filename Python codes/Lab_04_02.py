final_number=int(input("Enter the final number: "))
abundant_numbers=0
for i in range(1,final_number+1):
    S=0
    for j in range(1,i):
        if i%j==0:
            S+=j
        else:
            continue
    if S>i:
        abundant_numbers+=1
print("Input:\n","  Input number: ",str(final_number))
print("Output:\n","  Number of abundant numbers from 1 to ",str(final_number),"is : ",str(abundant_numbers))
