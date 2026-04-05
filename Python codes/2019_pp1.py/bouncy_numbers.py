# p,q=input().split()
# bouncy_numbers=[]
# for i in range(int(p),int(q)+1):
#     k=2
#     compare=1
#     compare_less=9
#     str_i=str(i)
#     for char in str_i:
#         if int(char)>=compare:
#             compare=int(char)
#         else:
#             break
#     else:
#         k-=1
#     for char in str_i:
#         if int(char)<=compare_less:
#             compare_less=int(char)
#         else:
#             break
#     else:
#         k-=1    
#     if k==2:
#         bouncy_numbers.append(i)
# bouncy_numbers=set(bouncy_numbers)
# print(sum(bouncy_numbers))
            

p,q=input().split()
sum=0
for i in range(int(p),int(q)+1):
    s=str(i)
    increasing=False
    decreasing=False
    for j in range(len(s)-1):
        if s[j]<s[j+1]:
            increasing=True
        elif s[j]>s[j+1]:
            decreasing=True
        if increasing and decreasing:
            sum+=i
print(sum)
