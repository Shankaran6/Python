# Final_Data=[]

# with open("Lab_07_data.txt") as file:
#     for line in file:
#         Length,E,I,Load=map(float,line.strip().split())
        
#         #Calculating D Max

#         L_3=Length**3
#         P=Load*1000
#         E=E*(10**9)

#         D_Max=round(P*L_3/(48*E*I),6)

#         #Calculating S Max
#         S_Max= round(P*Length/(4*I),3)

#         Final_Data.append([Length,D_Max,S_Max])

# for bar in Final_Data:
#     print("Length: "+str(bar[0])+" m, "+"Max Deflection: "+str(bar[1])+" m, "+"Max Bending Stress: "+str(bar[2])+" Pa")
#     print(f"Length: {bar[0]} m, Max Deflection: {bar[1]} m, Max Bending Stress: {bar[2]} Pa")


 

# Output=[]
# data=[]
# with open("Lab_07_data.txt") as file:
#     for line in file:
#         Length,E,I,Load=map(float,line.strip().split())
#         E=E*(10**9)
#         Load=Load*1000
#         data.append([Length,E,I,Load])

# for beam in data:
#     Def_Max=round((beam[3]*(beam[0]**3))/(48*beam[1]*beam[2]),6)
#     S_Max=round((beam[3]*beam[0])/(4*beam[2]),2)
#     Output.append([beam[0],Def_Max,S_Max])

# for data in Output:
#     print(f"Beam {Output.index(data)+1}: Length: {data[0]} m, Max Deflection: {data[1]} m, Max Bending Stress: {data[2]:.2f} Pa")

    
Output=[]

Input=[]

with open("Lab_07_data.txt") as file:
    for line in file:
        Length,E,I,Load=map(float,line.strip().split())
        E=E*(10**9)
        Load=Load*1000
        Input.append([Length,E,I,Load])

for beam in Input:
    Def_max=(beam[3]*(beam[0]**3))/(48*beam[1]*beam[2])
    S_max=(beam[3]*beam[0])/(4*beam[2])
    Output.append([beam[0],Def_max,S_max])

for i in range(len(Output)):
    print(f"Beam {i+1}: Length {Output[i][0]:.1f} m, Max Deflection: {Output[i][1]:.6f}, Max Bending Stress: {Output[i][2]:.2f} Pa")




