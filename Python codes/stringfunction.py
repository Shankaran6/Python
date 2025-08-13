S= "Welcome to python"
# print(len(S))
# print(S[0])
# print(S[0:7], end=' ')
# print(S[-9:-6],end='')
# print(S[11:17])
# i=0
# while i<len(S):
#     print(S[i],end='')
#     i+=1
# print("")
# for i in range (0,len(S)):
#     print(S[i], end='')
# print("")


# i=1
# k= int(len(S)) 
# while i<len(S):
#     print(S[k-i])
#     i+=1

# i=1

# while i<=len(S):
#     print(S[-i])
#     i+=1

# i=-len(S)
# while i<0:
#     print(S[i])
#     i+=1
# print(S[-len(S):-1])

# for i in range (0,len(S)):
#     print(S[-len(S)+i],end='')

# for i in S:
#     print(i)

# for i in range(len(S)-1,-1,-1):
#     print(S[i])

# for i in reversed(S):
#     print(i)

# S[0] ="w"
# print(S)

# letters = []

# for i in range(0,len(S)):
#     k=str(S[i])
#     letters.append(k)

# letters[0]="w"

# print(letters)

# a=S[0:5]
# print(a)

# print(S[-17:-10])




dob = input("Please enter your dob in format YYYY/MM/DD")


k=0
for i in range(0,len(dob)):
    if i!= 4 and i!=7:
        k+=int(dob[i])
    else:
        continue
while k>9:
    l=str(k)
    k=int(l[0]) +int(l[1])

d=int(dob[8])+int(dob[9])
while d>9:
    e=str(d)
    d=int(e[0])+int(e[1])
print("sum of all numbers",k)
print("sum of numbers in date",d)
    