# n=int(input("Enter the numeber: "))

# def check(n):
#     n=str(n)
#     return n ==n[::-1]  #Checks whether it is palindrome or not, returns True/ False

# def reverse(n):
#     return int(str(n)[::-1])

# while not check(n):
#     rev=reverse(n)
#     n = n + rev


# print(n)


n=int(input(("Enter the number: ")))
steps=0
def check(n):
    n=str(n)
    return n ==n[::-1]  #Checks whether it is palindrome or not, returns True/ False

def reverse(n):
    return int(str(n)[::-1])

while not check(n):
    rev=reverse(n)
    n = n + rev
    steps+=1
    if steps>25:
        print("too long")
        break

print(n)
steps=0





            