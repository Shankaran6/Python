A=[]
B=[]
ord_A=input().split()
for i in range(int(ord_A[0])):
    row=list(map(int,input().split()))
    A.append(row)
ord_B=input().split()
for i in range(int(ord_B[0])):
    row=list(map(int,input().split()))
    B.append(row)
for i in range(int(ord_A[0])):
    print("")
    for k in range(int(ord_B[1])):
        sum=0
        for j in range(int(ord_B[0])):
            sum+=A[i][j]*B[j][k]
        print(sum,end=' ')




