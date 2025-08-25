#listed lists
X=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
                ]
n=0
while n<3:
    for i in range (3):
        print(X[n][i],end=', ')
    n+=1
print("")
n=0
while n<3:
    i=0
    while i <3:
        print(X[n][i],end=', ')
        i+=1
    n+=1
print("")
for i in range(3):
    for j in range(3):
        print(X[i][j],end=', ')


# 5 students take 3 subjects
# marks stored (total 15 marks)
#Out put - 
# Student name - Maths , physics , chemistry , total , average , results