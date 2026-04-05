seconds=int(input())
last=1
before=0
distance=1
for i in range(seconds-1):
    fib=last+before
    before=last 
    last=fib 
    distance+=fib**(1/2)
print(round(distance,3))