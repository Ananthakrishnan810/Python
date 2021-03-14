class bank:
    def __init__(self,anumber,name,taccount):
        self.anumber=anumber
        self.name=name
        self.taccount=taccount
        self.balance=0
    def dep(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("The balance is:",self.balance)

    def withdraw(self):
      amount=int(input("Enter the amount to withdraw:"))
      self.balance-=amount
      print("The balance remainings:",self.balance)

a=input("Enter your account number:")
b=input("Enter your name:")
c=input("Enter your type of account:")
bank1=bank(a,b,c)
bank1.dep()
bank1.withdraw()