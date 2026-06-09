msg=list(map(str,input("Enter the message: ").split()))
print([int(word) for word in msg if word.isdigit() and len(word)==6])