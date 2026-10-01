# import matplotlib.pyplot as plt

# with open("Lab_09_01.txt") as file:
#     Data=[line.strip() for line in file.readlines()]
        
# Vin,Vout,Tolerance=map(float,Data[0].strip().split(","))
# Resistors=list(map(float,Data[1].strip().split(",")))

# def check_tol(Vout,V_out):
#     range=abs((Vout-V_out)/Vout)
#     if range<Tolerance:
#         return True
#     else:
#         return False

# Possible_combinations=[]
# Power_dissipation=[]
# for i in range(len(Resistors)):
#     Choose_J=Resistors[:i]+Resistors[i+1:]
#     for j in range(len(Resistors)-1):
#         R1=Resistors[i]
#         R2=Choose_J[j]
#         V_out=Vin*(R2/(R1+R2))
#         P=Vin**2/(R1+R2)
#         if check_tol(Vout,V_out):
#             Possible_combinations.append([int(R1),int(R2)])
#             Power_dissipation.append(P)
#         else:
#             continue
# min_dis=min(Power_dissipation)
# index=Power_dissipation.index(min_dis)
# Combo=Possible_combinations[index]
# R1=Combo[0]
# R2=Combo[1]
# print(str(R1)+", "+str(R2))

# Rl=[10*i for i in range(1,101)]
# Voltage=[]
# for i in range(len(Rl)):
#     R_=R2*Rl[i]/(R2+Rl[i])
#     Vnew=Vin*(R_/(R1+R_))
#     Voltage.append(Vnew)

# plt.plot(Rl,Voltage)
# plt.show()



import matplotlib.pyplot as plt

with open(input()) as file:
    Data=[line.strip() for line in file.readlines()]

Vin,Vout,Tolerance=map(float,Data[0].strip().split(","))
Resistors=list(map(float,Data[1].strip().split(",")))
Possible_combinations=[]
Power_dissipations=[]

for i in range(len(Resistors)):
    R1=Resistors[i]
    Select_R2=Resistors[i+1:]
    for j in range(len(Resistors)-1):
        R2=Resistors[j]
        V_out=Vin*(R2/(R1+R2))
        P=(Vin**2)/(R1+R2)
        ran=abs((Vout-V_out)/Vout)
        if ran<Tolerance:
            Possible_combinations.append([R1,R2])
            Power_dissipations.append(P)

min_dissipation=min(Power_dissipations)
index=Power_dissipations.index(min_dissipation)

Combo=Possible_combinations[index]
print(*Combo)
R1=Combo[0]
R2=Combo[1]
Ri=[10*i for i in range(1,101)]
Voltage=[]
for i in range(len(Ri)):
    R_=R2*Ri[i]/(R2+Ri[i])
    Vnew=Vin*(R_/(R1+R_))
    Voltage.append(Vnew)

plt.plot(Ri,Voltage)
plt.show()










    












