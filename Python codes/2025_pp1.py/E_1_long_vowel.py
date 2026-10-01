# vowels=("aeiouAEIOU")
# string=str(input())
# maxim=0
# string_final=string
# for i in range(len(string)):
#     for j in range(i,len(string)):
#         for char in string[i:j]:
#             if char not in vowels:
#                 break
#         else:
#             if maxim>=len(string[i:j]):
#                 continue
#             else:
#                 maxim=len(string[i:j])
#                 string_final=string[:i]+"["+string[i:j]+"]"+string[j:]
# print(string_final)

vowels="aeiouAEIOU"
string=str(input())
vowel_parts=[]
vowel_part=""
for i in range(len(string)):
    if string[i] in vowels:
        vowel_part+=string[i]
    else:
        if len(vowel_part)!=0:
            vowel_parts.append(vowel_part)
        vowel_part=""
print(max(vowel_parts,key=len))
first,last=string.rsplit(max(vowel_parts,key=len))
print(first+"["+max(vowel_parts,key=len)+"]"+last)

