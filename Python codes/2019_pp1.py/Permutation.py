n=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
Permutation=[]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if i!=j and i!=k and j!=k:
                Permutation.append(str(numbers[i])+str(numbers[j])+str(numbers[k]))
# Permutation=Permutation.sort  
# print(Permutation)
print(Permutation[0],Permutation[n-1],Permutation[-1])

