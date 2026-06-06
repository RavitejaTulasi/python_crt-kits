Godown_A=list(map(int,input("Enter the product codes: ").split()))
Godown_B=list(map(int,input("Enter the product codes: ").split()))
print('Unified Inventory: ',set(Godown_A+Godown_B), "length: ", len(set(Godown_A+Godown_B)))