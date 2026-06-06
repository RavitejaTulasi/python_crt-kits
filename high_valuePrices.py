prices=list(map(int,input("Enter the prices: ").split()))
print([i for i in prices if i>1000])

#using loop
Prices = list(map(int,input("Enter the prices: ").split()))
newList=[]
for i in Prices:
    if i >1000:
        newList.append(i)
print(newList)