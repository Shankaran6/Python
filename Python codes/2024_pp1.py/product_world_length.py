sentence=input().split()
product=1
for word in sentence:
    product*=len(word)
print(int(product%500))
