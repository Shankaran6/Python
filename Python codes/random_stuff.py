# for n in range(2): # stop argument, number not included
#     for m in range(3): print(n+1,m) # on the same line => same as intendation
#     print(n) #print belongs to the outer for loop, as no intendation is present

# list1=["why","hi","hello","hi","how"]
# print(list1)
# list1.remove("hi")
# print(list1)

# list1.insert(1,"hiya") #use to insert at a certain index position in a list
# print(list1)

# from collections import deque
# my_deque = deque()

# list1.pop(2)
# print(list1)


#Python expressions

# print(len([1,2,3]))        # 3
# print([1,2,3]+[4,5,6])     # [1, 2, 3, 3, 4, 5, 6]
# print(["hi"]*4)            # ['hi', 'hi', 'hi', 'hi']
# print(3 in [1,2,3])        # True
# for x in [1,2,3]:          # 1
#     print(x)               # 2
#                            # 3
# #Indexing and slicing

# L=['spam', 'Spam', 'SPAM']
# print(L[2])
# print(L[-2])
# print(L[1::])


# numList=[2,3,4,2,3,4,5,6,7,8,9,10,11,4,3,2,1]
# even=[]

# for i in numList:
#     if i not in even and i%2==0:
#         even.append(i)
# print(even)

# Message=input("Enter message: ")[::-1]
# Base= int(input("Enter base: "))
# encrypt_message=[]
# for char in Message:
#     encrypt=ord(char)
#     while encrypt>0:
#         encrypt_message.append(str(encrypt%Base))
#         encrypt=encrypt//Base
# print(''.join((encrypt_message[::-1])))

# text="Hello"  

# print(text[::-1])
# print(text[::-2])
# print(text[-3::-1])

# a = [[1,2],[3,4]]
# b = [[5,6],[7,8]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[1])):
#         s += a[i][j] * b[j][i]
# print (s)


# numbers=str(input())
# n=len(numbers)
# k=0

# for total in range(int((n*(n-1))/2)+1):
#     i=0
#     k+=1
#     n=len(numbers)
#     while n-k>=0:
#         print(numbers[:i]+numbers[i+k:])
#         i+=1
#         n-=1

# number=input()
# length=len(number)
# run=False
# for i in range(1,length+1):  #size of removed portion 
#     for j in range(length-i+1): #first reference begining
#         if j+i<length-3:
#             continue
#         else:
#             final=str(number[:j]+number[j+i:])
#             if not final:
#                 continue
#             else:
#                 if int(final)%8==0:
#                     print("The final number is : ",final)
#                     run=True
#                     break
           
#     if run==True:
#         break
# if run==False:
#     print("None")



# def f(x,l):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(3,[3,2])
        
# person= dict(name="Hi")
# print(type(person))

# a=5
# b=3

# print(a&b)
# print(a <<3)

# len="h"

# print(len[0:])

Model=[[1,2],[2,3],[3,4]]

for a,b in Model:
    print(a,b)