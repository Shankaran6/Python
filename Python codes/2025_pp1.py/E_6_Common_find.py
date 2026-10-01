first=list(map(int,input().split()))
second=list(map(int,input().split()))
final=[]
for number in first:
    if number in second:
        if number in final:
            continue
        else:
            final.append(number)
print(*final)
