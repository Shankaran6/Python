product=[]
def read_text_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            if not line.strip():
                continue
            else:
                product.append(line.strip())

read_text_file("/Users/shankaranguruparan/Documents/GitHub/Python/Python codes/Apples.txt")

products=[]

for i in range(0,len(product)):
    products.append(product[i].split(' '))

for i in range(0,len(product)):
    products[i].append(int(products[i][1])-int(products[i][2]))
    if products[i][3]<=0:
        products[i][3]= "0 (Out of stock)"


for i in range(0,len(product)):
   print(f"{products[i][0]:<15}"+ f"{str(products[i][3]):<10}")





   



