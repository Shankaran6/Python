#if divisible by 8, then give output yes
#if not remove minimum number of characters such that it becomes divisible by 8
#if new numeber found out put yes and output the new numeber, if not exist then output no
str_number=str(input())
number=[]
for char in str_number:
    number.append(char)
run=True
if int(str_number[-3:])%8==0:
    run=False
    m=str_number
while run:
    for i in range(len(str_number)-1):
        numbers=number.copy()
        for j in range(3):
            k=i
            numbers=number.copy()
            while k>-1:
                numbers.pop(len(numbers)-j-k-1)
                k-=1
            to_check=''.join(numbers)
            check=to_check[-3:]
            if int(check)%8==0:
                m=to_check
                run=False
                break
        if run==False:
            break
    if run==False:
        break
            
while run:        
    print("none")   
    run=False     
    break

if run==False:
    print("Yes", m)

