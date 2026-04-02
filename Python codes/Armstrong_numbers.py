k=int(input("Give the number to check up to: "))
Armstrong_numbers=[]
for number in range(0,k):
    k=str(number)
    digits=[]
    sum=0
    for i in range(0,len(k)):
        digits.append(int((k[i])))
        sum+=(int(k[i])**len(k))

    if number==sum:
        # print(number, "is an Armstrong Number")
        Armstrong_numbers.append(k)
    else:
        # print(number, "is Not an armstrong number")
        continue
print(Armstrong_numbers)

