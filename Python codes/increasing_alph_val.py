string=str(input())
sum=0
for i in range(len(string)):
    for j in range(i,len(string)):
        if ord(string[j])>ord(string[i]):
            sum+=1
print(sum)
    