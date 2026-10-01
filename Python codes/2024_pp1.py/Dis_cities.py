Cities=input().split()
distances=[0]+list(map(int,input().split()))
for i in range(len(Cities)):
    print("")
    for j in range(len(Cities)):
        print(abs(distances[i]-distances[j]),end=' ')
        
    
