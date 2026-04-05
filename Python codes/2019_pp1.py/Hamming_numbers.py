#writable in the format 2^i * 3^j * 5^k
initial,final=input().split()
initial=int(initial)
final=int(final)
summation=0
def divisor(number):
    if number%2==0:
        number=number/2
    if number%3==0:
        number=number/3
    if number%5==0:
        number=number/5
    return number
for number in range(initial,final+1):
    num=number
    while number!=1: 
        if number%2!=0 and number%3!=0 and number%5!=0:
            break
        else:
            number=divisor(number)
    else:
        summation+=num
print(summation)

