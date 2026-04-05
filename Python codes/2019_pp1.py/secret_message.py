alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string=str(input())
letters=list(set((char) for char in string))
letters_ordered=[[],[]]
for i in range(26):
    if alphabets[i] in letters:
        if len(letters_ordered[0])<(len(letters)//2):
            letters_ordered[0].append(alphabets[i])
        else:
            letters_ordered[1].append(alphabets[i])
secret_message=""
letters_ordered[1]=letters_ordered[1][::-1]
for char in string:
    if char in letters_ordered[0]:
        secret_message+=letters_ordered[1][letters_ordered[0].index(char)]
    elif char in letters_ordered[1]:
        secret_message+=letters_ordered[0][letters_ordered[1].index(char)]
    else:
        secret_message+=char
print(secret_message)
