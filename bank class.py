class bank:
    def __init__(self,acc_no="empty",name="empty",type="empty",balance=0):
        self.acc_no=acc_no
        self.name=name
        self.type=type
        self.balance=balance
    def deposit(self,balance=0):
        self.balance=self.balance+balance
    def withdraw(self):
        balance=int(input("enter the amount to be withdraw"))
        if((self.balance-balance)<0):
            print("\n insufficent balance")
        else:
            self.balance=self.balance-balance
    def details(self):
        print("\n -----your account details-----")
        print("\n account no",self.acc_no)
        print("\n account holder name",self.name)
        print("\n account type",self.type)
        print("\n account balance",self.balance)
m1=int(input("enter account number"))
m2=input("enter account holder name")
m3=input("enter account type")
c1=bank(m1,m2,m3)
while(True):
    print("\n 1.deposit \n 2.withdraw \n3.details")
    ch=int(input("\n enter your choice"))
    if ch==1:
        n=int(input("enter amount needed to deposit"))
        c1.deposit(n)
    elif ch==2:
        c1.withdraw()
    elif ch==3:
        c1.details()
    else:
        break
    
    
    
    
