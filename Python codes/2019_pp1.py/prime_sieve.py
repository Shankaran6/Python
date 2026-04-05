n=int(input())
Numbers=[num for num in range(1,n+1)]
Numbers.remove(1)
numb=2
while numb<n+1:
    if numb in Numbers:
        for k in range(2,(n//numb)+1):
            if (numb*k in Numbers):
                Numbers.remove(numb*k)
             
    numb+=1
print(Numbers)

