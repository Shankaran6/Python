numbers=list(map(int,input().split()))
summation=0
for number in numbers:
    if number%2==1:
        summation+=number
    else:
        continue
print(summation)