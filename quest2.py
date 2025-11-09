# create  Account class with 2 atrributes -balancr and account no.create methods for debit ,credit and printiing the balance 

class Account:
  def __init__(self,balance,account_no):
    self.balance=balance
    self.account_no=account_no
  
  def debit(self,amount):  #debit method
    self.balance-=amount
    print("RS",amount,'was debited ')

  def credit(self,amount):  #debit method
    self.balance+=amount
    print("RS",amount,'was credited ')

  def total_balance(self):
    return self.balance  #debit method
    


acc1=Account(500,123456)
acc1.debit(100)
acc1.credit(200)
print(acc1.balance,acc1.account_no)