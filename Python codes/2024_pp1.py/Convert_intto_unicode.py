numbers="0123456789"
string=str(input())
final=""
number=""
for char in string:
    if char not in numbers:
        if len(number)>1:
            final+=chr(int(number))
            number=""
        final+=char
    else:
        number+=char
if len(number)>1:
            final+=chr(int(number))
print(final)
    



