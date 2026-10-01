# triangle_size=int(input())
# start=int(input())
# series=[[0,start,0]]+[[] for _ in range(triangle_size)]
# for i in range(1,triangle_size+1):
#     series[i].append(0)
#     for j in range(1,i+2):
#         series[i].append(series[i-1][j-1]+series[i-1][j])
#     series[i].append(0)
# for line in series:
#     line=line.remove(0)
# for line in series:
#     line=line.remove(0)
# for line in series: 
#     print(*line)


# triangle_rows=int(input())
# start=int(input())
# last_line=[]
# line=[]
# print(start)
# for r in range(1,triangle_rows):
#     line.append(start)
#     for p in range(1,r):
#         line.append(last_line[p-1]+last_line[p])
#     line.append(start)
#     print(*line)
#     last_line=line.copy()
#     line=[]

triangle_rows=int(input())
start=int(input())
list=[[start]]
for r in range(1,triangle_rows):
    list.append([start])
    for i in range(1,r):
        list[r].append(list[r-1][i-1]+list[r-1][i])
    list[r].append(start)
for line in list:
    print(*line)





