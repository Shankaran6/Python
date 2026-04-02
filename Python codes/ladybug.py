import random
number=int(input())
reps=int(input())
clock=[-5,-4,-3,-2,-1,1,2,3,4,5,6]
k=0
prob=0
choose=[-1,1]
repititions=reps
while reps>0:
    reps-=1
    k=0
    clock_=clock.copy()
    while len(clock_)>1:
        c=random.choice(choose)
        k+=c
        if k>6:
            k=-5
        elif k<-5:
            k=6
        try:
            clock_.remove(k)
        except Exception:
            continue
    if int(clock_[0])==number:
        prob+=1
    else:
        continue
    

print((prob/repititions)*100)
    
    


        


