k=int(input("Enter the number: "))
while k>=0:
    if k ==1 or k ==0:
        print("non_prime")
        k=int(input("Enter the number: "))
    else:
        for i in range(2,round((k**(1/2)))+1):
            if k%i==0:
                print("non_prime")
                break
            else: 
                continue
        else:
            print("Prime") 
        k=int(input("Enter the number: "))