with open("PP2_Kuna.txt") as file:
    Data=[line.strip() for line in file.readlines()]

Rows,Col,K=map(int,Data[0].split())
CELLS=[]
number_of_hotspots=0
Hotspots=[]
for line in Data[1:]:
    CELLS.append([int(element) for element in line.split()])

def neighbor_count(cell,i,j):
    Rows_consider=CELLS[i-1:i+2]
    box_consider=[]
    for row in Rows_consider:
        box_consider.append(row[j-1:j+2])
    summation=0
    for part in box_consider:
        summation+=sum(part)
    summation-=cell
    return summation
    
Consider_cells=CELLS[1:len(CELLS)-1]
for i in range(len(Consider_cells)):
    Consider_rows=Consider_cells[i][1:len(Consider_cells[i])-1]
    for j in range(len(Consider_rows)):
        # print(i,j,Consider_rows[j])
        p=i+1
        q=j+1
        cell=Consider_rows[j]
        count=Consider_rows[j]*8-neighbor_count(cell,p,q)
        
        if K<count:
            Hotspots.append([p+1,q+1,count])
            number_of_hotspots+=1
print(f"Hotspots: {number_of_hotspots}")
for i in range(len(Hotspots)):
    print(*Hotspots[i])




