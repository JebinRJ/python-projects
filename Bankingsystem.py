#import sys
class Customer:
    '''WELCOME TO '''
    bankname = "INDIAN OVERSEAS BANK "
    
    def __init__(self,name , accNo , balance=0):
        self.name = name
        self.accNo = accNo
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(" Amount Deposited. ")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print(" Insufficient Balance ! ")
        else:
            self.balance = self.balance - amount
            print(" Amount withdraw successfully. ")

    def balance1(self):
        print("Your Account Balance is : ",self.balance)

print("")    
print(Customer.__doc__+Customer.bankname)
print("")
while True:
    name=input("Enter your Name : ")
    print("")
    name1="user"

    accNo=int(input("Enter Account No : "))
    print("")
    accNo1=12345
    customer1=Customer(name,accNo)

    if name1==name and accNo==accNo1:
        while True:
            print(" Choices : ""D-Deposit","W-Withdraw","E-Exit","B-Balance")
            choice=input("Enter your choice : ")
    
            if choice== "D":
                amount=float(input("Enter your amount : "))
                customer1.deposit(amount)
        
            elif choice == "W":
                amount = float(input("Enter your amount : "))
                customer1.withdraw(amount)

            elif choice == "B":
                customer1.balance1()

            elif choice=="E":
                quit()
        
        
            
    else:
        print("")
        print(" Enter correct Username and Account_Number ")
        print("")
    
    

