num1=int(input("Enter the initial number: "))
num2=int(input("Enter the final number: "))
sum=0
for i in range(num1+1,num2):
    sum+=i
print(sum)