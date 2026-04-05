number_of_cities=int(input())
distances=list(map(int,input().split()))
dis=0
Distance=[[] for _ in range(number_of_cities)]
distance_ordered=[0]

for distance in distances:
    dis+=distance
    distance_ordered.append(dis)

for i in range(number_of_cities):
    print("")
    for j in range(number_of_cities):
        print(abs(distance_ordered[j]-distance_ordered[i]),end=" ")
    






