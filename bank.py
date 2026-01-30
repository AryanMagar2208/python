class bank:
    def __init__(self, accno, balance):
        self.accno = accno
        self.balance = balance
    
    def deposit(self):
        n = int(input("Enter money to be deposited :"))
        if n>0:
            self.balance += n
            print("Money Deposited")
            
    def withdraw(self):
        n = int(input("Enter money to be withdrawn :"))
        if n>0 and n<=self.balance:
            self.balance -= n
            print("Money Withdrawn")
            
    def checkbal(self):
        print(f"Account Number : {self.accno}")
        print(f"Current Balance : {self.balance}")
    
num=int(input("Enter Account Number: "))
bal=int(input("Enter Your Balance: "))
B1 = bank(num,bal)

m=1
while(m!=0):
    print(f"What Do You Want To DO ? \n 1.) Deposit \n 2.) Withdraw \n 3.) Check Balance \n 4.) Exit")
    x = int(input("Enter Your Choice : "))
    if(x==1):
        B1.deposit()
    elif(x==2):
        B1.withdraw()
    elif(x==3):
        B1.checkbal()
    elif(x==4):
        m=0
        print("Thank You")
    else:
        print("Invalid Input")
