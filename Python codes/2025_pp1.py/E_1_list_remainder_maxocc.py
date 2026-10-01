# numbers=list(map(int,input().split()))
# divisor=int(input())
# numbers_remainder=[]
# copy=numbers_remainder.copy()
# count=0
# for number in numbers:
#     for i in range(len(numbers_remainder)):
#         if number%divisor == numbers_remainder[i][0]:
#             print("he")
#             numbers_remainder[i][1]+=1
#             break
#     else:
#         print("hi")
#         numbers_remainder.append([number%divisor,1])
# print(numbers_remainder)
# min_val=max(numbers)
# maximum=(max(numbers_remainder[i][1] for i in range(len(numbers_remainder))))
# for i in range(len(numbers_remainder)):
#     if maximum==numbers_remainder[i][1]:
#         if min_val>numbers_remainder[i][0]:
#             min_val=numbers_remainder[i][0]
# print(min_val,maximum)


numbers=list(map(int,input().split()))
divisor=int(input())
Remainder=[(number%divisor) for number in numbers]
remainders={}
for rem in Remainder:
    if rem in remainders:
        remainders[rem]+=1
    else:
        remainders[rem]=1
print(max(remainders),remainders[max(remainders)])




    
        


