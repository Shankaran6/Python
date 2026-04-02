numbers=list(map(float,input("Enter the numbers :").split(' ')))
max=numbers[0]
for i in numbers:
    if i >= max:
        max=i
    if i <= numbers[0]:
        numbers[0]=i
if max%1==0:
    max=int(max)
if numbers[0]%1==0:
    numbers[0]=int(numbers[0])
print(max,numbers[0])

    
    