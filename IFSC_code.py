code = input("Enter the IFSC code: ")
print("Valid IFSC code" if len(code)==11 and code[:4].isalpha() and code[4] == "0" and code[5:].isalnum() else "Invalid IFSC code")