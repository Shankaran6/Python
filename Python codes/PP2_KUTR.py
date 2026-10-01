with open("PP2_Kutr.txt") as file:
    Data=[line.strip() for line in file.readlines()]

n=int(Data[0])

Deliveries=Data[1:]
Driver_distance={}
Driver_deliveries={}
Driver_delivery_success={}
Drivers=[]

for i in range(n):
    Driver,ID,distance,Result=Deliveries[i].split()
    if Driver not in Drivers:
        Drivers.append(Driver)
    
    Driver_distance[Driver]=Driver_distance.get(Driver,0)+int(distance)
    Driver_deliveries[Driver]=Driver_deliveries.get(Driver,0)+1
    if Result=="D":
        Driver_delivery_success[Driver]=Driver_delivery_success.get(Driver,0)+1

def Success_rate(Driver):
    dis=Driver_distance[Driver]
    k=Driver_deliveries[Driver]
    j=Driver_delivery_success[Driver]
    Success_per=(j/k)*100
    if Success_per>=80 and dis>=50:
        return "Excellent",Success_per
    elif Success_per>=60:
        return "Good",Success_per
    else:
        "Needs review",Success_per
        
for Driver in Drivers:
    Success,rate=Success_rate(Driver)
    print(Driver,Driver_delivery_success[Driver],Driver_distance[Driver],Success,round(rate,2))
    
