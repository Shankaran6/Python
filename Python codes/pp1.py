# numbers=input("n,c").split(' ')
# n=int(numbers[0])
# c=int(numbers[1])
# while n == 0:
#     numbers=input("Please enter valid values for n,c").split(' ')
#     n=int(numbers[0])
#     c=int(numbers[1])



# total=0
# if c==0:
#     print("0")
# else:
#     for i in range(1,c+1):
#         total+=n**i
#     print(total)



n=int(input("Please enter the integer n"))

while n<=0:
    n=int(input("Please enter proper value for the integer n"))
sum_of_square=0
for i in range (1,n+1):
    sum_of_square+=i**2

total=0
for i in range (1,n+1):
    total+=i

square_of_sum=total**2

difference=(square_of_sum-sum_of_square)

print(difference)


