numbers=list(map(int,input().split()))
numbers.sort()
Factors=[]
maximum=1
for j in range(1,int(numbers[0]**(1/2)+1)):
    if int(numbers[0])%j ==0:
        Factors.append(j)
        Factors.append(numbers[0]/j)
for factor in Factors:
    for number in numbers:
        if number%factor!=0:
            break
    else:
        if factor>maximum:
            maximum=factor
print(maximum)

