import re
for i in range(5):
    open(f"Level_{i}.txt", "w").close()
with open("Lab_09_02.txt") as file:
    Datas=[line.split() for line in file.readlines()]

def classify(Molecules):
    Compatible=""
    if Molecules.get("S",0)>=1 and Molecules.get("O",0)>=4 and Molecules.get("Na",0)>=1:
        Compatible+="1"
        Molecules["S"]=Molecules["S"]-1
        Molecules["O"]=Molecules["O"]-4
        Molecules["Na"]=Molecules["Na"]-1

    if Molecules.get("S",0)>=1 and Molecules.get("O",0)>=3 and Molecules.get("Mg",0)>=1:
        Compatible+="2"
        Molecules["S"]=Molecules["S"]-1
        Molecules["O"]=Molecules["O"]-3
        Molecules["Mg"]=Molecules["Mg"]-1

    if Molecules.get("O",0)>=2 and Molecules.get("Cl",0)>=3:
        Compatible+="3"
        Molecules["O"]=Molecules["O"]-2
        Molecules["Cl"]=Molecules["Cl"]-3
    if len(Compatible)>1:
        return "Level_4"
    if len(Compatible)==0:
        return "Level_0"
    else:
        return f"Level_{Compatible}"
    
for data in Datas:
    Molecules={}
    structure=data[1].split("-")
    for compound in structure:
        match=re.fullmatch(r"([A-Za-z]+)(\d*)",compound)
        name=match.group(1)
        number=match.group(2)
        if number=="":
            number=1
        Molecules[name]=Molecules.get(name,0)+int(number)
    Level=classify(Molecules)
    with open(Level+".txt","a") as file:
        file.write(data[0].strip() + "\n")












                



    

    
    
