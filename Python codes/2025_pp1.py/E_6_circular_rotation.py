string_1,string_2=input().split()
for i in range(len(string_1)):
    string_1=string_1[-1]+string_1[:len(string_1)-1]
    if string_1==string_2:
        print("True")
        break
else:
    print("False")