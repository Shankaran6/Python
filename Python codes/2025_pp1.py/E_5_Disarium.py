number=str(input())
summation=0
for i in range(len(number)):
    summation+= int(number[i])**(i+1)
if int(number)==summation:
    print("Disarium number")
else:
    print("Non Disarium")

