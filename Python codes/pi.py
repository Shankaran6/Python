# num=int(input())
# sum=0
# for n in range(1,num):
#     sum+=n**(-2)
# print((sum*6)**(1/2))



# memo={0:0,1:1}

# def f(x):
#     if x in memo:
#         return memo[x]
#     else:
#         memo[x] = f(x-1) + f(x-2)
#         return memo[x]
# n=int(input())
# f(n)
# print(memo[n])

# first_term=0
# second_term=1
# fib=0
# n=int(input())
# for n in range(0,n):
#     first_term=fib
#     fib+= second_term
#     second_term=first_term
# print(fib)

feb=[0,1]
n=int(input())
for i in range(2,n+1):
    feb.append(feb[i-1]+feb[i-2])
print(feb)