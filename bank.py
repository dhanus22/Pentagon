bal = 10000
p = 3206
print("welcome to Canara")
print("Insert your card")
a = int(input("Enter your pin:"))
if (a == p):
    print("1.English")
    print("2.Kannada")
    print("3.Hindi")
    b = int(input("Choose your language:"))
    if(b == 1):
        print("1.Savings")
        print("2.Current")
        c = int(input("Select your account type:"))
        if(c == 1):
            print("1.Withdraw")
            print("2.Check balance")
            print("3.deposit")
            d = int(input("Enter your choice:"))
            if(d == 1):
                e = int(input("enter amount to withdraw:"))
                if(e <= bal):
                    bal = bal - e
                    print("Collect your cash")
                    print("Transaction successful")
                    print("Amount debited",e)
                else:
                    print("Low balance")
            elif(d == 2):
                print("Available balance:",bal)
            elif(d == 3):
                f = int(input("Enter amount to deposit:"))
                bal = f + bal
                print("Amount deposited",f)
else:
    print("Wrong pin")     

                
