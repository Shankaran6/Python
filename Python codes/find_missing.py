n=str(input()).split()
m=str(input()).split()
def missingNumbers(n,m):
    i=0
    while i <len(m):
        if m[i] in n:
            n.remove(m[i])
            m.remove(m[i])           
        else:
            i+=1
    m.sort()
    print(*m)
missingNumbers(n,m)
