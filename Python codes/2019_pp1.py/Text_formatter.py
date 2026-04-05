string=input()
func=string[:2]
stri=string[3:]

k=1
def h1(stri):
    stri=stri.upper()
    print(rf"//{"="*(len(stri)+2)}\\")
    print("||",stri,"||")
    print(rf"\\{"="*(len(stri)+2)}//")
def h2(stri):
    print(" "+stri+" ")
    print("-"*(len(stri)+2))
def ol(stri):
    print(k+".",stri)
    k+=1
def ul(stri):
    print(">",stri)
def pp(stri):
    print(stri) 
 
if func=="h1":
    h1(stri)
if func=="h2":
    h2(stri)
if func=="ol":
    ol(stri)
if func=="ul":
    ul(stri)
if func=="pp":
    pp(stri)


 