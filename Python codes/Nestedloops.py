# x=1

# while x <= 5:
#     y=1
#     while y <=3:
#         print(y,end='')
#         y+=1
#     print(f"{x}\n")
#     x+=1


# number= int(input("Please enter a numeber:"))
# x=1
# y=1

# while x<=number:
#     while y<=number:
#         print(x*y,",",end='')
#         y+=1
#     y=1
#     print("\n_"+"_"*30)
#     x+=1


#_____________________
# 1,3,5,7,9
x=1
while x<10:
    if x%2!=0:
        print(x,end='')
    x+=1
print("\n_"+"_"*20)

#______________________
#2,4,6,8,10

x=1
while x<11:
    if x%2==0:
        print(x,end='')
    x+=1
print("\n_"+"_"*20)

#______________________
#1,3,6,10,15
x=1
while x<5:
    print(x*(x+1)/2,end='')
    x+=1
print("\n_"+"_"*20)


#_______________________
#1,4,9,16
x=1
while x<5:
    print(x*x,end='')
    x+=1
print("\n_"+"_"*20)

#______________________
#1,*,3,*,5,*,7
# x=0
x=1
while x<10:
    
    if x%2!=0:
        print(x,end='')
    else:
        print("*",end='')
    x+=1
print("\n_"+"_"*20)
    
#______________________

#1*
#2**
#3***
#4****

x=1
while x<5:
    print(x,"*"*x,"\n",end='')
    x+=1
print("\n_"+"_"*20)

#__________________________


#12345
#12345
#12345

x=1
while x < 5:
    y=1
    while y <6:
        print(y,end='')
        y+=1
    print("")
    x+=1

print("\n_"+"_"*20)
#________________
#54321
#54321
#54321
x=1
while x < 5:
    y=5
    while y >0:
        print(y,end='')
        y-=1
    print("")
    x+=1
    
print("\n_"+"_"*20)
#________________

#11111
#22222
#33333
#44444

x=1
while x<5:
    print(f"{x}"*5)
    x+=1
print("\n_"+"_"*20)

#_________________
#*
#**
#***
#****
#*****
x=1
while x <6:
    print("*"*x)
    x+=1
print("\n_"+"_"*20)
#__________________
#1
#22
#333
#4444
#55555
x=1
while x <6:
    print(f"{x}"*x)
    x+=1
print("\n_"+"_"*20)


#__________________

