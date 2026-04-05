String_1=str(input())
String_2=str(input())
number_of_ones=0
i=0
while i <len(String_2):
    if String_1[i]==String_2[i]:
        i+=1
        continue
    
    elif String_1[i]=="0" and String_1[i+1]=="0":
            String_1=String_1[:i]+"1"+String_1[i+2:]
            i+=2
    else:
         print("No")
         exit()
print("Yes")


            