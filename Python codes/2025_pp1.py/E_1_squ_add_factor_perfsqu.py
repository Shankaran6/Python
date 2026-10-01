number=int(input())
square_sum=sum(i**2 for i in range(1,number+1))
sum=0
for i in range(1,square_sum):
    if square_sum%i==0:
        if int(i**(1/2))==i**(1/2):
            sum+=i
print(sum)


