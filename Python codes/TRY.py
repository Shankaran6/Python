# number_list=input()
# numbers=list(map(float,number_list.split()))

# maximum=numbers[0]
# minimum=numbers[0]
# for number in numbers:
#     if number > maximum:
#         maximum=number
#     if number < minimum:
#         minimum=number
#if maximum%1==0:
#   maximum=int(maximum)
#if minimum%1==0:
#   minimumm=int(minimumm)
# print(maximum,minimum)


# game_inputs=input()

# games=game_inputs.split()

# Subjects=["I", "We"]
# Verbs=["play", "watch"]

# for subject in Subjects:
#     for Verb in Verbs:
#         for game in games:
#             print(subject, Verb, game)


# student_marks=[]
# Total=[]
# Average=[]
# for i in range(4):
#     student_marks.append(list(map(int,input().split())))

# for student in student_marks:
#     total=0
#     for mark in student:
#         total+=mark
#     Total.append(total)
#     average=total/3
#     Average.append(average)

# for i in range(4):
#         print("Total: ",Total[i],"Average: ",Average[i])

# matrix_row=[] 
# matrix=[] 
# run=True
# while -1 not in matrix_row:
#     matrix_row=list(map(str,input().split()))
#     if "-1" not in matrix_row:
#         matrix.append(matrix_row)
#     else:
#         break
#     if len(matrix[0])==len(matrix_row):
#         continue
#     else:
#         run=False
#         error="Invalid matrix"
# for row in matrix:
#     for element in row:
#         try:
#             int(element)/1
#         except Exception:
#             run=False
#             error="Error"
# while run:
#     for i in range(len(matrix[0])):
#         print("")
#         for j in range(len(matrix)):
#             print(matrix[j][i],end=' ')
#     break
# while not run:
#     print(error)
#     break




# numbers=list(map(float,input().split()))
# maximum=numbers[0]
# minimum=numbers[0]

# for number in numbers:
#     if number>maximum:
#         maximum=number
#     if number<minimum:
#         minimum=number

# if maximum%1==0:
#     maximum=int(maximum)
# if minimum%1==0:
#     minimum=int(minimum)
# print("Minimum =",minimum)
# print("Maximum =",maximum)


# matrix_row=[]
# matrix=[]
# run=True
# while True:
#     matrix_row=list(map(str,input().split()))

#     if "-1" in matrix_row:
#         break
#     else:
#         matrix.append(matrix_row)
#     if len(matrix_row)==len(matrix[0]):
#         continue
#     else:
#         run=False
#         error="Invalid matrix"
#     try:
#         for element in matrix_row:
#             int(element)/1
#     except Exception:
#         run=False
#         error="Error"

# while run:
#     for i in range(len(matrix[0])):
#         print("")
#         for j in range(len(matrix)):
#             print(matrix[j][i],end=' ')
#     break
# while not run:
#     print(error)


