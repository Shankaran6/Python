numbers=list(map(int,input().split()))
Result=[]
for number in numbers:
    k=int((2*number)**(1/2))
    if number%15==0 and k*(k+1)==number*2:
        Result.append(True)
    else:
        Result.append(False)
print(Result)
