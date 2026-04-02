Equations=[]
def getEquation(filepath):
    file=open(filepath,"r")
    for line in file:
        equation=line.strip()
        Equations.append(equation)
    file.close()
getEquation("chemical_balance.txt")
for equation in Equations:    
    elements=[{},{}]
    sides=equation.split("->")
    for side in sides:
        
        components=side.split("+")
        for component in components:
            char=""
            count="1"
            coeff=1
            if "*" in component:
                coeff,elem=component.split("*")
                coeff=int(coeff)
            else:
                elem=component
            i=0
            for i in range(len(elem)):
                if elem[i].isupper():
                    if char!="":
                        elements[sides.index(side)][char]=elements[sides.index(side)].get(char,0) +int(count)*coeff
                        char=""
                        
                    char+=elem[i]
                    if i<len(elem)-1:
                        if elem[i+1].islower():
                            char+=elem[i+1]
                    count="1"
                elif elem[i].isdigit():
                    if count=="1":
                        count=elem[i]
                    else:
                        count+=elem[i]
            if char !="":
                elements[sides.index(side)][char]=elements[sides.index(side)].get(char,0) +int(count)*coeff     
    if elements[0]==elements[1]:
        print("Correct")
    else:
        print("Incorrect")
print(elements)









