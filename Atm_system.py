pin = int(input("Enter your 4 digit pin: "))
acc_bal = 0
if pin == 1234:
    print("Welcome to the SBI Bank")
    while True:
        print("1.Deposit")
        print("2.Withdrawl")
        print("3.Balance Inquiry")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        print("\n")
        if(choice==1):
            amount=int(input("Enter the amount to deposit: "))
            acc_bal=acc_bal+amount
            print(f"Dear customer your account xxxxxxxxxxxx1234 is credited with {amount}")
        elif(choice==2):
            amount=int(input("Enter the amount to withdraw: "))
            if (amount<acc_bal):
                print(f"Dear customer your account xxxxxxxxxxx1234 is debited with {amount}")
                acc_bal=acc_bal-amount
            else:
                print("Insufficient Balance.....!")
        elif(choice==3):
            print(f"Your SBI account xxxxxxxxxx1234 balance is {acc_bal}")
        else:
            print("Thank You.........!")
            break
else:
    print("you entered wrong pin.")