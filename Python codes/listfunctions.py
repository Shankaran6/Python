Subject=["Maths", "Physics", "Chemistry"]
# # Subject[3]="IT"  Index out of range
# Subject.append("IT")


# Subject.insert(2,"Science")

# Subject.extend(["Tamil"])
# if "English" in Subject:
#     Subject.remove("English")


# Subject.pop()
# print(Subject)
# # Subject.clear()
# # Subject.append("Subjects empty")

# print(Subject.index("Maths")) #find does not work
Subject.sort(reverse=True)
# # Subject.reverse()
# print(Subject)


marks=[95,83,94,57,69,73]
print(max(marks))
print(min(marks))
print(sum(marks))
marksD=marks.copy() #use the copy function to create another array
marksD[2]=45        #If just equal is used, the array name may be different but the address is same.    
print(marks)
print(marksD)
