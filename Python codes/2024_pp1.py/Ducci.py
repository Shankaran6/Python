numbers_considered=list(map(int,input().split()))
numbers=numbers_considered.copy()
first=numbers_considered[0]
count=0
while not all(numbers[i]==0 for i in range(len(numbers))):
    for i in range(len(numbers)):
        if i<len(numbers)-1:
            numbers[i]=abs(numbers_considered[i]-numbers_considered[i+1])
        else:
            numbers[i]=abs(numbers_considered[i]-first)
    numbers_considered=numbers.copy()
    first=numbers_considered[0]
    count+=1
print(count)

