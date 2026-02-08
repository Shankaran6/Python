Alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number=int(input("Please enter the number: "))

for i in range(1,number+1):
    print("."*(number-i)+Alphabets[0:i-1]*((i-1) and 1)+Alphabets[i-1:0:-1]*((i-1) and 1)+Alphabets[0]+"."*(number-i))

for i in range(number-1,0,-1):
    print("."*(number-i)+Alphabets[0:i-1]*((i-1) and 1)+Alphabets[i-1:0:-1]*((i-1) and 1)+Alphabets[0]+"."*(number-i))