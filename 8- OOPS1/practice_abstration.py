#Questions
#Create a account class with 2 attributes - balance and account number 
#Create methods for debit , credit and printing the balance

class Account():
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"Credited amount")
        print("Total Balance = ",self.get_balance())

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"debited amount")
        print("Total Balance =",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(10000,9087564312)
# print("Account no",acc1.account_no)
# print("Total balance",acc1.balance)
acc1.debit(1000)

acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
