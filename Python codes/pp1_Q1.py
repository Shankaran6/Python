# name,list=input().split("=")
# name_,target=input().split("=")
# target=target.strip()
# target_int=int(target)
# run=True
# nums=eval(list)
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i==j:
#             continue
#         else:
#             if nums[i]+nums[j]==target_int:
#                 final=(nums[i],nums[j])
#                 print(final)
#                 run=False
#                 break
#         if run==False:
#             break
#     if run==False:
#         break
# if run==True:
#     print("none")








# sentence=input().split(" ")
# max=0
# for word in sentence:
#     if len(word)>max:
#         max=len(word)
# sentence_set=set(sentence)
# print("Number of unique words is:", len(sentence))
# print("Longest word is",max,"characters long")








# sentence_t=str(input())
# sentence_p=str(input())
# indices=[]
# indexed=0
# while sentence_p in sentence_t:
#     indexe=(sentence_t.index(sentence_p))
#     indices.append(indexed+indexe)
#     indexed+=len(sentence_p)+indexe
#     sentence_t=sentence_t[:indexe]+sentence_t[indexe+len(sentence_p):]
# print(indices)











# sentence=str(input()).casefold()
# vowels=["a","e","i","o","u"]
# index_of_vowels=[]
# for i in range(len(sentence)):
#     if sentence[i] in vowels:
#         index_of_vowels.append(i)
# if len(index_of_vowels)>=1:
#     result=[[index_of_vowels[0]]]
#     for i in range(1,len(index_of_vowels)):
#         if index_of_vowels[i]-index_of_vowels[i-1]>1:
#             result.append([index_of_vowels[i]])
#         else:
#             result[-1].append(index_of_vowels[i])
# final=[]
# for res in result:
#     if len(res)==len(result[0]):
#         continue
#     else:
#         exit()
# else:
#     run=True
# if len(result)>=1:
#     for section in result:
#         if len(section)>len(final):
#             final=section
# if run:
#     for i in range(len(result)):
#         print(sentence[result[i-1][0]+1:result[i][0]]+"["+sentence[result[i][0]:result[i][0]+1]+"]",end='')
#     print(sentence[result[-1][-1]+1:])
# else:         
#     print(sentence[:final[0]-1]+"["+sentence[final[0]-1:final[len(final)-1]]+"]"+sentence[final[len(final)-1]:])







# sentence=str(input()).casefold()
# vowels=["a","e","i","o","u"]
# index_of_vowels=[]
# run=False
# for i in range(len(sentence)):
#     if sentence[i] in vowels:
#         index_of_vowels.append(i)
# if len(index_of_vowels)>=1:
#     result=[[index_of_vowels[0]]]
#     for i in range(1,len(index_of_vowels)):
#         if index_of_vowels[i]-index_of_vowels[i-1]>1:
#             result.append([index_of_vowels[i]])
#         else:
#             result[-1].append(index_of_vowels[i])
# for res in result:
#     if len(res)>len(result[0]):
#         maxlen=res
#         run=True
#     else:
#         continue 
# if run==True:
#     print(sentence[:res[0]]+"["+sentence[res[0]:res[-1]+1]+"]"+sentence[res[-1]:])
# else:
#     k=0
#     for char in sentence:
#         if char in vowels:
#             while k==0:
#                 print("[",end='')
#                 k=1
#             print(char,end='')
#             if char==sentence[-1]:
#                 print("]")
#         elif char not in vowels and k==1:
#             print("]",end='')
#             print(char,end='')
#             k=0
#         else:
#             print(char,end='')

    
    
    
    




# string=str(input())
# characters=[]
# for char in string:
#     characters.append(char)
# i=0
# while i < len(characters)-1:
#     n=1
#     if characters[i].isalpha():
#         for j in range(i,len(characters)):
#             if characters[i]==characters[j]:
#                 characters[i]=f"{n+1}"
#                 # print(characters)
#                 i=i+1
#     i=i+1
# print(characters)








# string=str(input())
# characters=[[string[0]]]
# for i in range(1,len(string)):
#     if string[i]==string[i-1]:
#         characters[-1].append(string[i])
#     else:
#         characters.append([string[i]])
# for sets in characters:
#     if len(sets)>1:
#         run=True
#         continue
#     else:
#         run=False
#         break
# if run==True:
#     for sets in characters:
#         print(sets[0]+f"{len(sets)}",end="")
#     print("")
# else:
#     print(string)








# n=int(input())
# k=int(input())
# special=[]
# for i in range(1111,10000):
#     string=str(i)
#     if "0" in string:
#         continue
#     else:
#         for char in string:
#             if int(char)%n==0:
#                 continue
#             else:
#                 break
#         else:
#             special.append(string)
# if len(special)>=k:
#     print(special[k-1])
# else:
#     print("-1")









# # import copy
# r,c=input().split(" ")
# r=int(r)
# c=int(c)
# Matrix=[[]for _ in range(r)]
# Matrix_copy=[[]for _ in range(r)]
# for i in range(r):
#     row=input().split()
#     Matrix[i]+=row
#     Matrix_copy[i]+=row
# # Matrix_copy = copy.deepcopy(Matrix) 
# # can also use this when copying 2D lists
# for i in range(r):
#     for j in range(c):
#         if int(Matrix[i][j])==0:
#             for z in range(c):
#                 Matrix_copy[i][z]="0"
#             for k in range(r):
#                 Matrix_copy[k][j]="0"
# print()
# for row in Matrix_copy:
#     print(' '.join(row))






# num,position=input().split()
# special_num=[]
# int_position=int(position)
# for i in range(1111,9999):
#     characters=list((str(i)))
#     if len(set(characters))==4 and ("0" not in characters):
#         for char in characters:
#             if int(num)%int(char)==0:
#                 continue
#             else:
#                 break
#         else:
#             if int(int_position)>0:
#                 special_num.append(i)
#                 int_position-=1
# if len(special_num)>0:
#     print(special_num)
# else:
#     print("-1")

    










    
    








            


                
        





