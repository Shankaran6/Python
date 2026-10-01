# numbers=list(map(int,input().split()))
# Factors=[[1] for _ in range(len(numbers))]

# for k in range(2,min(numbers)+1):
#     if all(number%k==0 for number in numbers):
#         print("Not coprime")
#         exit()
#     else:
#         continue    
# else:
#     print("coprime")     



numbers=list(map(int,input().split()))
for i in range(2,min(numbers)+1):
    if any(numbers[j]%i!=0 for j in range(len(numbers))):
        continue
    else:
        print("Not coprime")
        break
else:
    print("Co prime")

