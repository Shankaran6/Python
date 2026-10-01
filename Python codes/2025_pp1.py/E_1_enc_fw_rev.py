encoded_as=str(input())
message=str(input()).upper()
if encoded_as=="E":
    for i in range(len(message)):
        if ord(message[i])==ord("A"):
            order=ord("Y")
        elif ord(message[i])==ord("B"):
            order=ord("Z")
        else:
            order=ord(message[i])-2
        message=message.replace(message[i],chr(order))
if encoded_as=="D":
    for i in range(len(message)):
        if ord(message[i])==ord("Y"):
            order=ord("A")
        elif ord(message[i])==ord("Z"):
            order=ord("B")
        else:
            order=ord(message[i])+2
        message=message.replace(message[i],chr(order))
print(message)

