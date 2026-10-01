# from datetime import datetime
# Final_data=[]
# def days_to_birthday(date):
#     datetime_object=datetime.strptime(date,"%Y-%m-%d")
#     date=datetime_object.date()
#     num_days=date.timetuple().tm_yday
#     return num_days

# outfile=open("Lab_06_write.txt","a")
# outfile.truncate(0)

# NIC=[]
# Data_line=[]
# Admission_num={}
# with open(input()) as file:
#     for line in file:
#         Data_line.append(line.strip())
# for line in Data_line:
#     final_line=""
#     name,DoB,Gender=line.split(" ")
#     DAYS=days_to_birthday(DoB)
#     if Gender=="F":
#         DAYS+=500
#     if DoB[0:4] in Admission_num:
#         Admission_num[DoB[0:4]]+=1
#     else:
#         Admission_num[DoB[0:4]]=1
#     nic=str(DoB[0:4])+str(DAYS).zfill(3)+str(Admission_num.get(DoB[0:4])).zfill(3)
#     final_line=str(name)+" "+str(nic)
#     outfile.write(f"{final_line}\n")
# outfile.close() 

# from datetime import datetime
# def days_to_birthday(date):
#     datetime_object=datetime.strptime(date,"%Y-%m-%d")
#     date=datetime_object.date()
#     num_days=date.timetuple().tm_yday
#     return num_days
# Final_Data=[]
# Admission_num={}
# Data=[]
# with open("Lab_06_read.txt","r") as file:
#     for line in file:
#         Data.append(line.split(" "))
# file.close()
# for person in Data:
#     if person[1][0:4] in Admission_num:
#         Admission_num[person[1][0:4]]+=1
#     else:
#         Admission_num[person[1][0:4]]=1
#     DAYS=days_to_birthday(person[1])
#     if person[2]=="F":
#         DAYS+=500
#     Output=str(person[0])+" "+str(person[1][0:4]+str(DAYS).zfill(3)+str(Admission_num[person[1][0:4]]).zfill(3))
#     Final_Data.append(Output)
# Final_output="\n".join(Final_Data)

# with open("Lab_06_write.txt","w") as file:
#     file.write(Final_output)
# file.close()

from datetime import datetime

def days_to_birthday(date):
    datetime_object=datetime.strptime(date,"%Y-%m-%d")
    date=datetime_object.date()
    num_days=date.timetuple().tm_yday
    return num_days
Data_of_people=[]
Admission_num={}
Final_Data=[]
with open (input()) as file:
    for line in file:
        Data_of_people.append(line.strip().split())

for person in Data_of_people:
    DAYS=days_to_birthday(person[1])
    if person[1][0:4] in Admission_num:
        Admission_num[person[1][0:4]]+=1
    else:
        Admission_num[person[1][0:4]]=1
    if person[2].strip()=="F":
        DAYS+=500
    name=str(person[0])
    Year=str(person[1][0:4])
    day_string=str(DAYS).zfill(3)
    admission_num_str=str(Admission_num[person[1][0:4]]).zfill(3)
    final_line=name+" "+Year+day_string+admission_num_str
    Final_Data.append(final_line)

Output_data="\n".join(Final_Data)

with open("Lab_06_write.txt","w") as file:
    file.write(Output_data)






        


  




        
    