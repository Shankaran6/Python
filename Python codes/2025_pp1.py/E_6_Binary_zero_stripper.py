string=str(input())
for i in range(len(string)):
    if string[i]=="0":
        if i==len(string)-1:
            print("0")
            break
        continue
    else:
        print(string[i:])
        break