# print("Enter the matrix : \n")
# matrix_=[]
# matrix=[]
# run=True
# k=0
# while -1 not in matrix:
#     try:
#         matrix=(list(map(int,input("").strip().split())))
#         while k==0:
#             length=len(matrix)
#             k+=1
#     except Exception:   #Exception works even when not written
#         print("Error")
#         run=False
#         break
#     if -1 in matrix:
#         if len(matrix_)==0:
#             run=False
#         continue
#     else:
#         if length==len(matrix):
#             matrix_.append(matrix)
#         else:
#             print("Invalid matrix")
#             run=False
#             break
# while run:
#     matrix_transpose=[[] for _ in range(len(matrix_[0]))]
#     for i in range(len(matrix_[0])):
#         for j in range(len(matrix_)):
#             matrix_transpose[i].append(matrix_[j][i])
#     print("\n")
#     for i in range(len(matrix_[0])):
#         print(*matrix_transpose[i])
#     break



matrix_=[]
matrix=[]
run=True
k=0
while -1 not in matrix:
    matrix=(list(map(str,input("").strip().split())))
    while k==0:
        length=len(matrix)
        k+=1
    if "-1" in matrix:
        if len(matrix_)==0:
            print("Error")
            run=False
        break
    else:
        matrix_.append(matrix)
for row in matrix_:
    try:
        for n in row:
            int(n)/1
    except Exception:
        print("Error")
        run=False
        break
    if length==len(row):
        continue
    else:
        print("Invalid matrix")
        run=False
        break
while run:
    matrix_transpose=[[] for _ in range(len(matrix_[0]))]
    for i in range(len(matrix_[0])):
        for j in range(len(matrix_)):
            matrix_transpose[i].append(matrix_[j][i])
    for i in range(len(matrix_[0])):
        print(*matrix_transpose[i])
    break
        



