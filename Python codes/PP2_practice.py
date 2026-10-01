# with open("PP2_practice_1.txt") as file:
#     Data=[line.strip() for line in file.readlines()]
# with open("PP2_practice_2.txt") as file:
#     Match=[line.strip() for line in file.readlines()]

# Match_with=[]
# for line in Data:
#     words=line.split()
#     for word in words:
#         word_string=""
#         for i in range(len(word)):
#             if word[i].isalpha():
#                 word_string.append(word[i])
#             Match_with.append(word)
# Matched=[]
# for word in Match_with:
#     if word in Match:
#         Matched.append(word)
# final_string="\n".join(word for word in Matched)
# with open("PP2_output.txt","w") as file:
#     file.write(final_string)


#12 6 \6
#18 12 \6

# x=17
# y=16
# z=min(x,y)
# m=max(x,y)
# def function(x,z):
#     k=x%z
#     if k==0:
#         return z
#     else:
#         return function(x,k)
# GCD = function(m,z)
# print(GCD)

# Dictionary={"hello":3,"hi":2}

# Keys=list(Dictionary.keys())
# for i in range(len(Dictionary)):
#     print(f"{Keys[i]:<5}",Dictionary[Keys[i]])






