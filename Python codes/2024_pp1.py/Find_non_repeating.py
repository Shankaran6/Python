string=str(input())
repeat=""
i=0
while i < len(string):
    if string[i] not in string[i+1:]:
        print(string[i])
        break
    else:
        string=string.replace(string[i],"")
else:
    print("-1")

