numbers=list(map(int,input().split()))
lengths=[]
for i in range(len(numbers)):
    for k in range(i,len(numbers)):
        num=numbers[i]
        for number in numbers[i+1:k+1]:
            if num<number:
                num=number
            else:
                break
        else:
            lengths.append(len(numbers[i:k+1]))
print(max(lengths))
        





