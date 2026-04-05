Guesses=list(map(str,input().split()))
Guesses_copy=Guesses.copy()
Solution=str(input())
Output=[[0,0] for _ in range(len(Guesses))]
for i in range(len(Guesses)):
        for j in range(4):
            if Guesses[i][j]==Solution[j]:
                Guesses_copy[i]=Guesses_copy[i][:j]+" "+Guesses_copy[i][j+1:]
                Output[i][0]+=1

            else:
                if (Guesses_copy[i][j] in Solution):
                    Output[i][1]+=1
for item in Output:
     print(tuple(item),end=' ')
                