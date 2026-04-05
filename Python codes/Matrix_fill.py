S=str(input())
N=int(input())
i=0
Matrix=[[] for _ in range(N)]
def printing_in_matrix_form(Matrix):
    for row in Matrix:
        print(*row)
while i < N:
    for letter in S:
        Matrix[i].append(letter)
        i+=1
        if i == N:
            i=0
    else:
        for k in range(N-len(S)%N):
            Matrix[i].append("*")
            i+=1
            if i == N:
                break

for i in range(4):
    for k in range(len(Matrix[0])):
        print(Matrix[i][k],end='')



