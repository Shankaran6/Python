Marks=[[],[],[],[]]
run=True
for i in range(0,4):
    try:
        Marks[i]=list(map(int,input("Enter the marks of student "+str(i+1)+": ").split(' ')))
    except Exception:
        print("Error")
        run=False
while run:
    for j in range(0,4):
        sum=0
        for i in range(0,3):
            sum+=Marks[j][i]
        print("Total is :",sum,end=' ')
        average=round(sum/3, 1)
        if average%1==0:
            average=int(average)
        print("Average is :",average)
    break
