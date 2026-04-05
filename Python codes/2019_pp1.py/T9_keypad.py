Data=[[" "],["a","b","c"],["d","e","f"],
      ["g","h","i"],["j","k","l"],["m","n","o"],
      ["p","q","r","s"],["t","u","v"],["w","x","y","z"],["."]]

move=0.4
press=0.2
persist=0.7
k=0 
string=str(input()).casefold()
time=-0.4 # to not consider the first digit moving time
for char in string:
    for i in range(len(Data)):
        if char in Data[i]:
            if k==i:
                time+=persist+press*(Data[i].index(char)+1)
            else:
                time+=move+press*(Data[i].index(char)+1)
            k=i
            break
print(f"{time:.2f}")