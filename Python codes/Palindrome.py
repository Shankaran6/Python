# #effective method for any
number=str(input())
if len(number)>2:
    if len(number)%2==1:
        front=number[:int(len(number)/2)-1]
        mid=int(number[int((len(number)-1)/2)-1:int((len(number)-1)/2)+2])
    else:
        front=number[:int(len(number)/2)-1]
        mid=int(number[int(len(number)/2)-1:int(len(number)/2)+1])
else:
    mid=number
red_mid=mid
while str(mid)!=str(mid)[::-1] and str(red_mid)!=str(red_mid)[::-1]:
    mid+=1
    red_mid-=1
if str(mid)==str(mid)[::-1]:
    print(front+str(mid)+front[::-1])
else:
    print(front+str(red_mid)+front[::-1])

# slower code but effective for smaller numbers
# number=int(input())
# red_number=number
# while str(number)!=str(number)[::-1] and str(red_number)!=str(red_number)[::-1]:
#     number+=1
#     red_number-=1
# if str(number)==str(number)[::-1]:
#     print(number)
# else:
#     print(red_number)