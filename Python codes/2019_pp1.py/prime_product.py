number=int(input())
Prime={}
i=2
number_mod=number
while i <= int((number+1)/2):
    if all(i%k!=0 for k in range(i+1,int((i**(1/2)+1)))):
            if number_mod%i==0:
                if str(i) in Prime:
                    Prime[str(i)]+=1
                else:
                     Prime[str(i)]=1
                number_mod=number_mod//i
            elif number_mod == 1:
                 break
            else:
                 i+=1
num=1
for key, value in Prime.items():  
    if value>1:
        print(f"{key}"+"^"+f"{value}",end="")
        num+=1
    else:
        print(f"{key}",end="")
        num+=1
    if num<=len(Prime):
         print("X",end='')
    
print("")