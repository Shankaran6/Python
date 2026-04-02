dealer=input().split(" ")
player=input().split(" ")
Play=[dealer, player]
k=False
for i in range(len(Play)):
    sum=0
    for j in range(len(Play[i])):
        if "J" in Play[i][j] or "Q" in Play[i][j] or "K" in Play[i][j] or "10" in Play[i][j]: #
            sum+=10
        elif "A" in Play[i][j]:
            Play[i].append("True")
            if i==0:
                sum+=11
            else:
                k=True
        else:
            sum+=int(Play[i][j][1])
    Play[i]=[sum]
if k:
    if Play[1][0]>10:
        Play[1][0]=Play[1][0]+1
    else:
        Play[1][0]=Play[1][0]+11
d=Play[0][0]-Play[1][0]

if d>10 or Play[0][0]>20:
    print("Lost")
elif d<0:
    print("Win")
else:
    print("Hit")
