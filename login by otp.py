import random
user_name="Prerna"
password=1101
def details():
    user=input("Enter username:")
    pass_w=int(input("Enter password:"))
    if user==user_name and pass_w==password:
        print("Login successfully")
    else:
        print("something is wrong")
        a=int(input("1:Press 1 relogin 2:Press 2 forget password/username"))
        if a==1:
            details()
        if a==2:
            def otp():
                ot_p=random.randrange(1000,100000)
                print("Your otp is:",ot_p)
                user_otp=int(input("Enter the given otp"))
                if user_otp==ot_p:
                    print("user_name=Prerna")
                    print("password=1101")
                    details()
                else:
                    print("Entered Otp is wrong")
                    print("Resent otp")
                    if True:
                        otp()
                    else:    
                        details()
            otp()
            
                        
                    

details()

