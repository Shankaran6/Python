#for loop
#while loop
# x=1
# isbool = True
# while isbool:
#     print(x)
#     x+=1
#     if x==5:
#         isbool = False

# x=0

# while x < 10:
#     print("Shankaran")
#     x+=1
# x=1
# while x < 5:
#     y=1
#     while y <6:
#         print(y,end='')
#         y+=1
#     print("\n")
#     x+=1

number= int(input("Please enter a numeber:"))
x=1
y=1

while x<=number:
    while y<=number:
        print(x*y,",",end='')
        y+=1
    y=1
    print("\n_"+"_"*30)
    x+=1

    


