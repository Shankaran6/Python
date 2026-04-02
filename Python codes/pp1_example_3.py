nums=input().split()
target=int(input())
for num in nums:
    num=int(num)

for j in range(len(nums)):
    for i in range(len(nums)):
        if i==j:
            continue
        elif int(nums[i])+int(nums[j])==target:
            k=(nums[j],nums[i])
            print(k)
            run=False
            break
    if run==False:
        break
