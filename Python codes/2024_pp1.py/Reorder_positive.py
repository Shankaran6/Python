numbers=list(map(int,input().split()))
First=[]
Last=[]
for number in numbers:
    if number>=0:
        First.append(number)
    else:
        Last.append(number)
print(*(First+Last))