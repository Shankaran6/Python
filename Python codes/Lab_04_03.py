# message=str(input("Enter message: "))
# base=int(input("Enter base: "))
# for character in message:
#     encryption_ini=[]
#     k=ord(character)
#     while k>0:
#         encryption_ini+=str((k%base))
#         k=k//base
#     print(*encryption_ini[::-1],end=" ")

message=input("Enter message: ")[::-1]
base=int(input("Enter base: "))
encryption=[]
for character in message:
    k=ord(character)
    while k>0:
        encryption+=str(k%base)
        k=k//base
print(*encryption[::-1])


    



