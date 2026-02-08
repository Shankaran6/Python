def simplification():
    k=1
    while n_d[0]%1==0:
        n_d[0]==n_d[0]/k
        n_d[1]==n_d[1]/k
        k+=1

fraction=input("Enter the fraction:")

n_d=fraction.split('/')
n_d[0]=int(n_d[0])
n_d[1]=int(n_d[1])

while n_d[0] < n_d[1]:
    rem, quo = divmod(n_d[0],n_d[1])
    n_d[0]=rem
    n_d[1]=quo
    simplification()
    
else:
    simplification()

print(n_d[0]+"/"+n_d[1])
    