numbers=list(map(int,input().split(",")))
maximum=max(numbers)
LeastCM=maximum
run=True
while run:
    for number in numbers:
        if LeastCM%number==0:
            continue
        else:
            LeastCM+=maximum
            break
    else:
        print(LeastCM)
        run=False
        