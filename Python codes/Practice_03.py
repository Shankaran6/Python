input_number=int(input("Please enter the number: "))

k=2*input_number-1

for i in range(1,input_number+1):
    print("."*(input_number-i),"*"*(2*i-1),"."*(input_number-i))

