#phone reload system:
#For first 30 min 2/= per minute 
#for 31 - 60 min 1.50/=
# 60 to 120 - 1/=
# above 120  0.5/=

# time = int(input("please enter the minutes talked"))

# while time<0:
#     time=int(input("Please enter a valid time"))
# if time<=30:
#     cost= time*2
# elif 30<time <=60:
#     cost= 60 + 1.5* (time-30)
# elif 60<time <=120:
#     cost= 105 + 1* (time-60)
# elif 120<time:
#     cost= 165 + 0.5* (time-120)
    
# print(cost)

#________________________________________________________________

#1-90 7/=
#91-150  10/=
# 151-300. 15/=
#300 + 15/= + 3%

# units = int(input("Please enter the number of units used"))

# while units<0:
#     units = int(input("Please enter a valid number"))

# if units<91:
#     cost=units*7
# elif units<151:
#     cost=630 + (units-90)*10
# elif units<301:
#     cost=1230 + (units-150)*15
# elif units>300:
#     cost=(3480 +(units-300)*15)*103/100

# print(cost, "/=")


#_______________________________________________________________


# 0 -1000 l  500/=
#1001 - 3000l  per l -3/=
#3001 - 10000l per l -5/=
# 10001 l - per l 10/=
#0777861677


water = int(input("Please enter litres used"))

while water<0:
    water =int(input("Please enter valid number"))
if water <1001:
    cost = 500
elif water < 3001:
    cost = 500 + (water-1000)*3
elif water < 10001:
    cost = 500 +2000*3 + (water-3000)*5
elif water >10000:
    cost = 500 + 2000*3 + 7000*5 + (water-10000)*10

print(water,"litres")
print(cost,"/=")