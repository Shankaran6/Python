# print("line 1")
# if True:
#     print("line 2") # 4 spaces or a tab 
# print("line 3")

# print("line 1")
# if False:
#     print("line 2") # 4 spaces or a tab 
# print("line 3")

# if True:
#     print("Need at least one line inside if condition")


# x = input("please enter True or False")
# if x=="False":
#     print("Hi")
# elif x=="True":
#     print("Hello")

# is_bool= bool(input("Enter True or False"))
# print(is_bool)
# if is_bool:
#     print("Hi")
# else:
#     print("Hello")



# if marks_< 45:
#     print("fail")
# elif marks_ <55:
#     print("S")
# elif marks_ <65:
#     print("C")
# elif marks_ <75:
#     print("B")
# else:
#     print("A")
marks_=int(input("please enter your marks:"))
if marks_<0 or marks_>100:
    print("Invalid marks")
else:
    if 0<=marks_<45:
        print("Fail")
    else:
        if marks_<55:
            print("S")
        else:
            if marks_<65:
                print("C")
            else:
                if marks_<75:
                    print("B")
                else:
                    if 75<= marks_ <=100:
                        print("A")


