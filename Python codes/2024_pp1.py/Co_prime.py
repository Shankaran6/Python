numbers=list(map(int,input().split()))
Factors=[[1] for _ in range(len(numbers))]

for k in range(2,min(numbers)+1):
    if all(number%k==0 for number in numbers):
        print("Not coprime")
        exit()
    else:
        continue    
else:
    print("coprime")     
