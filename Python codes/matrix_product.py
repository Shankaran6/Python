order_of_matrix=input("Enter the order of matrix: ")
order=order_of_matrix.split(' ')
print("Enter matrix A: ")
matrix=[[]for _ in range(int(order[0]))]
for i in range(0,int(order[0])):
    row=input("")
    matrix[i]=row.split(' ')
print("Enter matrix B: ")
matrix_=[[] for _ in range(int(order[0]))]
for i in range(0,int(order[0])):
    row=input("")
    matrix_[i]=row.split(' ')
for k in range(0,int(order[0])):
    print("\n")
    for i in range(0,int(order[1])):
        sum=0
        for j in range(0,int(order[1])):
            sum+=int(matrix[k][j])*int(matrix_[j][i])
        print(sum, end=' ')

        