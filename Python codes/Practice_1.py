fraction=input("Enter the fraction: ")
n_d=fraction.split('/')

neu=int(n_d[0])
den=int(n_d[1])

if neu> den:
    whole_part=neu//den
    neu=neu%den
    
    if neu==0:
        print(whole_part)
    else:

        for i in range(1,neu+1):
            if neu%i==0 and den%i==0:
                neu=neu/i
                den=den/i
            else:
                continue
        print(whole_part," ",str(int(neu)),"/",str(int(den)))

else:
    for i in range(1,neu+1):
        if neu%i==0 and den%i==0:
            neu=neu/i
            den=den/i
        else:
            continue
    print(str(int(neu)),"/",str(int(den)))
    

