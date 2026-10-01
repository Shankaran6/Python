integers=list(map(int,input().split()))
harmonies=0
for i in range(len(integers)-1):
    if integers[i]==integers[i+1]:
        harmonies+=1
print(harmonies)