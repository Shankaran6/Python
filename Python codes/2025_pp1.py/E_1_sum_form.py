numbers=list(map(int,input().split()))
add_upto=int(input())
final=[]
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i]+numbers[j]==add_upto:
            final.append((min(numbers[i],numbers[j]),max(numbers[i],numbers[j])))
final=set(final)
for item in final:
    print(*item)
# for item in final:
#     item=item.sort()
# unique=[]
# for item in final:
#     if item not in unique:
#         unique.append(item)
# for item in unique:
#     print(*item)
