integers=list(map(int,input().split()))
count=0
while True:
    for k in range(len(integers)):
        if integers[k]==0:
            print(count)
            exit()
    k=integers[0]
    for i in range(len(integers)):
        if i == len(integers)-1:
            integers[i]=abs(k-integers[i])    
        else:
            integers[i]=abs(integers[i]-integers[i+1])
    print(integers)
    count+=1
            
        
            

    

    