# for x in "Shankaran":
#     print(x)

# for x in range(10):
#     if x==5:
#         continue
#     print(x)

for i in range(10):
    if i%2==0:
        print(i, end='')

print("\n")

for i in range(10):
    if i%2!=0:
        print(i, end='')

print("\n")

for i in range(5):
    print(i*(i+1)/2, end='')

print("\n")

for i in range(5):
    print(i*i, end='')

print("\n")

for i in range(10):
    if i%2==1:
        print(i, end = '')
    else:
        print("*", end = '')

print("\n")

for i in range (1,5):
    print(i, end = '')
    print("*"*i)

print("\n")

for i in range (3):
    for k in range (1,6):
        print(k, end='')
    print("")

print("\n")

for i in range (3):
    for k in range (5,0,-1):
        print(k, end='')
    print("")

print("\n")

for i in range (5):
    print(f"{i}"*4)
    print("")

print("\n")

for i in range (5):
    print("*"*i)
    print("")

print("\n")

for i in range (5):
    print(f"{i}"*i)
    print("")

print("\n")
