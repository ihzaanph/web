class train:
    def __init__(self,name,seat_no):
        self.name=name
        self.seat_no=seat_no
        print(self.name,self.seat_no)
    def book(self):
        if self.seat_no==0 :
            print("seats are not available")
        else:
            seatno=int(input("enter the no of seats needed : ",))
            self.seat_no=self.seat_no-seatno
        print(self.name,self.seat_no)
    def cancel(self):
            seatno=int(input("enter no of seat need to cancel"))
            self.seat_no=self.seat_no+seatno
            print(self.name,self.seat_no)

t1=train('netravathi',50)

t2=train('venad',40)
while(True):
    print("ENTER CHOICE\n 1.booking\n 2.cancel\n 3.exit\n")
    n=int(input("enter your choice"))
    if(n==1):
        print("enter the train \n 1.netravathi \n 2.venad")
        m=int(input("enter your choice"))
        if m==1:
                t1.book()
        elif m==2:
                t2.book()
        else:
                print("wrong choice")
    elif(n==2):
        print("enter the train \n 1.netravathi \n 2.venad")
        o=int(input("enter your choice"))
        if o==1:
                t1.cancel()
        elif o==2:
                t2.cancel()
        else:
                print("wrong choice")
    else:
                print("wrong choice")
            

                       
