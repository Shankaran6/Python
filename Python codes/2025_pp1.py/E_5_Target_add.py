numbers=list(map(int,input().split()))
target=int(input())

# Faster

# k=0
# sum=0
# pair=[]
# while k<len(numbers):
#     for i in range(k,len(numbers)):
#         if sum!=target:
#             sum+=numbers[i]
#             pair.append(numbers[i])
#         elif sum==target:
#             print(tuple(pair),end=' ')
#             sum=0
#             k+=1
#             pair=[].copy()
#             break
#         else:
#             sum=0
#             k+=1
#             pair=[].copy()
#             break
#     if k==len(numbers)-1:
#         break
#Slower

for i in range(len(numbers)):
    for k in range(i,len(numbers)):
        if target==sum(numbers[i:k]):
            print(tuple(numbers[i:k]))
        else:
            continue
            

    

