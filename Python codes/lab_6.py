dimensions=input("Enter the dimensions:")
dimensions_rc=dimensions.split(',')

row=int(dimensions_rc[0])
column=int(dimensions_rc[1])

Matrix_A=[[] for _ in range(row)]
Matrix_B=[[] for _ in range(row)]
Transpose_B=[[] for _ in range(column)]
print("Enter the matrix A:")

for i in range (0,row):
    Matrix_A[i]=input("").split(' ')

print("Enter the matrix B?")

for i in range (0,row):
    Matrix_B[i]=input("").split(' ')
    
for i in range(row):
    for j in range(column):
        Transpose_B[j].append(Matrix_B[i][j])

AB_T=[]


for i in range(0,row):
    for j in range(0,column):
        for z in range(0,row):
            AB_T.append(int(Matrix_A[i][j])*int(Transpose_B[j][z]))

print(AB_T)
AB_TT=[[]for _ in range(row)]
z=0
for i in range(0,row):
    for j in range(0,row):
        z+=AB_T[i*row+j]
    AB_TT.append(z)
    z=0

print(AB_TT)
    


    
