with open("Lab_08_02.txt") as file:
    Data=[line.strip() for line in file.readlines()]
n_matrix=Data[0]
k=1
Matrices=[]
for n in range(int(n_matrix)):
    Matrix=[]
    size=int(Data[k])
    for i in range(k+1,k+size+1):
        Matrix.append(Data[i].split(","))
    Matrices.append(Matrix)
    k+=size+1

def Minor(Matrix,i,j):
    Minor=[]
    Matri_rows=Matrix[:i]+Matrix[i+1:]
    for k in range(len(Matri_rows)):
        Minor.append(Matri_rows[k][:j]+Matri_rows[k][j+1:])
    return Minor

def determinant(Matrix):
    det=0
    if len(Matrix)==2:
        det_2=int(Matrix[0][0])*int(Matrix[1][1])-int(Matrix[0][1])*int(Matrix[1][0])
        return det_2
    for j in range(len(Matrix)):
        det+=int(Matrix[0][j])*(-1)**(j)*determinant(Minor(Matrix,0,j))
    return det
            
def adjoint(Matrix):
    Find_adj=[]
    if len(Matrix)==2:
        Adjoint=[[int(Matrix[1][1]),-int(Matrix[0][1])],[-int(Matrix[1][0]),int(Matrix[0][0])]]
    else:
        for i in range(len(Matrix)):
            Row=[]
            for j in range(len(Matrix)):
                Row.append((-1)**(i+j)*determinant(Minor(Matrix,i,j)))
            Find_adj.append(Row)
        Adjoint=transpose(Find_adj)
    return Adjoint

def transpose(Matrix):
    Transpose=[]
    for i in range(len(Matrix[0])):
        Row=[]
        for j in range(len(Matrix)):
            Row.append(Matrix[j][i])
        Transpose.append(Row)
    return Transpose

def Display(Matrix):
    for row in Matrix:
        print(*row)

for i in range(int(n_matrix)):
    Det_=determinant(Matrices[i])
    if Det_==0:
        print("Determinant is 0, thus inverse does not exist")
    else:
        Inverse_without_det=adjoint(Matrices[i])
        Inverse=[]
        for row in Inverse_without_det:
            Row=[]
            for element in row:
                value=element/Det_
                if value==0:
                    Row.append(f"{0:7.2f}")
                else:
                    Row.append(f"{value:7.2f}")
            Inverse.append(Row)
        Display(Inverse)


# def Minor(Matrix,i,j):
#     Rows=Matrix[:i]+Matrix[i+1:]
#     minor=[]
#     for row in Rows:
#         Columns=row[:j]+row[j+1:]
#         minor.append(Columns)
#     return minor

# def determinant(Matrix):
#     print(Matrix)
#     det=0
#     first_row=Matrix[0]
#     if len(first_row)!=2:
#         for i in range(len(Matrix)):
#             det+=int(((-1)**(i))*first_row[i]*determinant(Minor(Matrix,0,i)))
#     else:
#         det=Matrix[0][0]*Matrix[1][1]-Matrix[0][1]*Matrix[1][0]   
#     return det

# def Transpose(Matrix):
#     Transpose=[]
#     for i in range(len(Matrix[0])):
#         Row=[]
#         for j in range(len(Matrix)):
#             Row.append(Matrix[j][i])
#         Transpose.append(Row)
#     return Transpose
            
# def inverse(Matrix):
#     Inverse=[]
#     Inv=[]
#     det=determinant(Matrix)
#     for i in range(len(Matrix)):
#         Row=[]
#         for j in range(len(Matrix[0])):
#             element=(1/det)*((-1)**(i+j))*determinant(Minor(Matrix,i,j))
#             Row.append(f"{element:7.2f}")
#         Inv.append(Row)
#     Inverse=Transpose(Inv)
#     return Inverse





# with open("Lab_08_02.txt") as file:
#     Data=[line.strip() for line in file.readlines()]
# Matrices=[]
# Info=[]
# for line in Data:
#     if "," in line:
#         row=list(map(int,line.strip().split(",")))
#         Info.append(row)
    
#     else:
#         Info.append(line)
        
        

# n_matrix=int(Info[0])
# k=1
# for i in range(n_matrix):
#     size=int(Info[k])
#     Matrix=Info[k+1:k+size+1]
#     Matrices.append(Matrix)
#     k+=size+1
#     Inverse=inverse(Matrices[i])
#     for row in Inverse:
#         print(*row)




        

    
    
    
