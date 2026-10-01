# string="Hello, META_06_, sIGNING oUT"
# for i in range(len(string)):
#     if not string[i].isdigit(): 
#         print(string[i],end="")
#     else:
#         print(end=' ')
# string="Hello, META_06_, sIGNING oUT"

# strings=string.rsplit('e')
# print(strings)


# numbers=list(map(int,input().split()))
# count=0
# for i in range(len(numbers)-2):
#     for j in range(i+1,len(numbers)-1):
#         for k in range(j+1,len(numbers)):
#             if (numbers[i]+numbers[j]+numbers[k])%3==0:
#                 count+=1
# print(count)


# string=str(input())
# k=int(input())%26
# for char in string:
#     if char.isalpha():
#         order=ord(char)
#         order+=k
#         if order>122:
#             order=order-122+96
#         print(chr(order),end='')
#     else:
#         print(char,end='')

    
# tuple_=("hi", "hello" )

# line=" ".join(tuple_)
# print(line)

# with open("random.txt") as file:
#     for line in file:
#         print(line)

Lise=[1,2,3,4,5,6]
print(Lise[:3])
print(Lise[3:])