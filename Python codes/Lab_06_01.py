# N_Rows,N_Columns=map(int,input("Enter the Dimension: ").split(","))
# Matrix_A=[]
# Matrix_B=[]
# Transpose=[[] for _ in range(N_Columns)]
# Product=[]

# def Get_Matrix(Matrix):
#     Row_data=[]
#     for i in range(N_Rows):
#         try:
#             Row_data=list(map(int,input().split()))
#         except Exception:
#             print("Error")
#             exit()
#         if len(Row_data)!=N_Columns:
#             print("Invalid Matrix")
#             exit()
#         Matrix.append(Row_data)

# def Get_Transpose(Matrix):
#         for i in range(N_Columns):
#             for j in range(N_Rows):
#                 Transpose[i].append(Matrix[j][i])

# def Get_Product(Matrix):
#     for i in range(N_Rows):
#         Product_Row=[]
#         for j in range(N_Rows):
#             summation=0
#             for k in range(N_Columns):
#                 summation+=Matrix[i][k]*Transpose[k][j]
#             Product_Row.append(summation)
#         Product.append(Product_Row)

# def Display_Matrix():
#     print("A x B Transpose :")
#     for row in Product:
#         print(*row)
    
# print("Enter Matrix_A:")
# Get_Matrix(Matrix_A)
# print("Enter Matrix_B:")
# Get_Matrix(Matrix_B)
# Get_Transpose(Matrix_B)
# Get_Product(Matrix_A)

# print(Transpose)
# Display_Matrix()


# print("Enter matrix A: ")
# for i in range(N_Rows):
#     row=list(map(int,input().split()))
#     Matrix_A.append(row)
# print("Enter matrix B: ")
# for i in range(N_Rows):
#     row=list(map(int,input().split()))
#     Matrix_B.append(row)
# for k in range(N_Rows):
#     print("")
#     for i in range(N_Rows):
#         summation=0
#         for j in range(N_Columns):
#             summation+=Matrix_A[k][j]*Matrix_B[i][j]
#         print(summation,end=' ')
N_Rows,N_Columns=map(int,input("Enter number of rows and columns :").split(","))
Matrix_A=[]
Matrix_B=[]
Transpose=[[] for _ in range(N_Columns)]
Product=[]
def Get_Matrix(Matrix):
    for i in range(N_Rows):
        try:
            row_input=list(map(int,input().split()))
        except Exception:
            print("Error")
            exit()
        if len(row_input)!=N_Columns:
            print("Invalid Matrix")
            exit()
        Matrix.append(row_input)

def Get_Transpose(Matrix):
    for i in range(N_Columns):
        for j in range(N_Rows):
            Transpose[i].append(Matrix[j][i])

def product_of_matrix(Matrix):
    for k in range(N_Rows):
        Row_Data=[]
        for j in range(N_Rows):
            Summation=0
            for i in range(N_Columns):
                Summation+=Matrix[k][i]*Transpose[i][j]
            Row_Data.append(Summation)
        Product.append(Row_Data)

def Display_Matrix():
    for row in Product:
        print(*row)

print("Enter Matrix A :")
Get_Matrix(Matrix_A)
print("Enter Matrix B :")
Get_Matrix(Matrix_B)
Get_Transpose(Matrix_B)
product_of_matrix(Matrix_A)
print("A x B Transpose :")
Display_Matrix()






