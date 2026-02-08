# # # S={"Maths", "Tamil", "English"}
# # # print(S)
# # # print(type(S))

# # S={"Maths", "Tamil", "English","Maths"} #unordered and not indexed

# # print(S)
# # print(type(S))

# # S.add("IT") #for single values
# # print(S)

# # S.update(["History","Sinhala","Literature"]) #multiple values
# # print(S)

# # S.remove("Maths")
# # print(S)

# # S.discard("Math")
# # print(S)

# # S.pop()
# # print(S)

# # S.clear()
# # print(S)


# #add, update, remove, discard

# # numbers=[70, 90, 26, 70, 55, 90, 76, 55, 38]
# # s=set(numbers)
# # print(s)

# a={1,2,3,4,5}
# b={3,5,7,8,9}

# # c=a|b 
# # c=a.union(b)
# # Q=a&b
# # Q=a.intersection(b)
# # print(Q)

# # e=a-b    #AnB'
# # e=b-a     
# # print(e)

# f=a^b      #(AUB)n(AnB)'
# print(f)

a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}

d=a|b|c
e=a&b&c
print(d)
print(e)
print(a<=b) #a is a sub set of b
print(b>=a)
print(a.issubset(b))
print(b<=a)
print(a.issuperset(b))





