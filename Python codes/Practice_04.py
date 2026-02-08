string=str(input("Enter the string: "))

separated=list(string.casefold())

if "b".casefold() in separated and "o".casefold() in separated and "y".casefold() in separated:
    print("He is a boy!")
elif "g".casefold() in separated and "i".casefold() in separated and "r".casefold() in separated and "l".casefold() in separated:
    print("She is a girl")
else:
    print("None found")