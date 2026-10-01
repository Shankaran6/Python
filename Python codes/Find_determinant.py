order=int(input())
Matrix=[]
det=1
for i in range(order):
    Matrix.append(list(map(int,input().split())))
for k in range(order):
    if Matrix[k][k]==0:
        for check in range(k+1,order):
            if Matrix[check][k]!=0:
                for t in range(k,order):
                    Matrix[k][t]=Matrix[k][t]+Matrix[check][t]
                break
        else:
            print("Determinant is 0")
            exit()
    for i in range(k+1,order):
        factor=Matrix[i][k]/Matrix[k][k]
        for j in range(order):
            Matrix[i][j]=Matrix[i][j]-Matrix[k][j]*factor
for i in range(order):
    det=det*Matrix[i][i]
print(round(det,3))
# 2,3,4
# 3,5,1
# 2,5,7

