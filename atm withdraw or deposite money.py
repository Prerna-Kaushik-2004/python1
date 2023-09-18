class atm:
    def __init__(self):
        print("WELCOME TO OUR ATM")
        
    def check_balance(self):
        print("Your total account balance is : 50000.06")
        
    def withdrawal(self):
        amount_w=int(input("Enter the amount to withdraw : "))
        amount=50000.06
        if amount_w>amount:
            print ("Your account balance is insufficient...\n Please try again")
            
        else:
            print("Now you can collect your money...")
            print("Now your remaining balance is : ",amount-amount_w)
    
    def deposit(self):
        amount=50000.06
        amount_d=int(input("Enter the amount to deposit : "))
        print("Your amount is deposited successfully")
        print("Now your new balance is : ",amount+amount_d)
            
    

s=atm()
c=int(input("Enter your Pin to proceed"))
pin=2234
if c==pin:
    s.check_balance()
    a=int(input("Press 1 for withdrawal and 2 to deposit money..."))       
    if a==1:
        s.withdrawal()
    elif a==2:
        s.deposit()
    else:
        print("Choose either 1 or 2 ")
else:
    print("Your pin is incorrect..\n Please try again")