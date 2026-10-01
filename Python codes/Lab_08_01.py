# import math
# with open("Lab_08_01.txt") as file:
#     Data=file.readlines()
# def get_values(line):
#     Type,R,L,C,V,f=line.strip().split()
#     R=int(R)
#     L=int(L)*(10**-3)
#     C=int(C)*(10**-6)
#     V=int(V)
#     f=int(f)
#     ang_freq=2*math.pi*f
#     imp_ind=ang_freq*L
#     imp_cap=1/(ang_freq*C)

#     if Type=="series":
#         return analyseSeriesCircuit(R,imp_ind,imp_cap,V)
#     else:
#         return analyseParallelCircuit(R,imp_ind,imp_cap,V)
    

# def analyseSeriesCircuit(R,imp_ind,imp_cap,V):
#     imp_total=(R**2+(imp_ind-imp_cap)**2)**(1/2)
#     angle=math.atan((imp_ind-imp_cap)/R)
#     Current=V/imp_total
#     return [round(imp_ind,1),round(imp_cap,1),round(imp_total,1),round(Current,1),round(math.degrees(angle),1)]

# def analyseParallelCircuit(R,imp_ind,imp_cap,V):
#     imp_total=1/((1/R**2)+(((1/imp_ind)-(1/imp_cap))**2))**(1/2)
#     angle=math.atan(((1/imp_ind)-(1/imp_cap))*R)
#     Current=V/imp_total
#     return [round(imp_ind,1),round(imp_cap,1),round(imp_total,1),round(Current,1),round(math.degrees(angle),1)]
# write=""
# for i in range(len(Data)):
#     Final=get_values(Data[i])
#     write+=" ".join(str(item) for item in Final)+"\n"
# with open("Lab_08_01_w.txt","w") as file:
#     file.write(write)

    

import math
Data=[]
def get_values():
    with open(input()) as file:
        for line in file:
            Type,R,L,C,V,f=line.strip().split()
            R=int(R)
            L=int(L)*(10**-3)
            C=int(C)*(10**-6)
            V=int(V)
            f=int(f)
            
            
