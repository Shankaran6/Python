Characters=list(map(str,input().split()))
Zeros=[]
Non_zeros=[]
for char in Characters:
    if char !="0":
        Non_zeros.append(char)
    else:
        Zeros.insert(0, char)
Final=Zeros+Non_zeros
print(' '.join(Final))