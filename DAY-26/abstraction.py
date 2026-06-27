from abc import ABC, abstractmethod

class BankAccount(ABC):
    def check_balance(self):
        print("You can check balance in your bank account")
        
    def view_history(self):
        print("You can view transaction history in your bank account")
        
    def userinfo(self):
        print("You can view user information in your bank account")
        
    def transaction(self):
        print("You can transfer money through net banking")
        
    
        
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
# we cant create object of abstract class because it has abstract methods. 
# so we can create object of child class which is inheriting the abstract class
# and implementing the abstract methods.  
#parent class doesnt have its definition
#but child class has its definition.
# so we can create object of child class and call the methods of parent class and child class.


class CurrentAccount(BankAccount):
    def deposit(self):
        print("You can deposit money in your current account")
    def withdraw(self):
        print("You can withdraw money from your current account")
    
    
class SavingsAccount(BankAccount):
    def deposit(self):
        print("You can deposit money in your savings account")
    def withdraw(self):
        print("You can withdraw money from your savings account")
        
class FixedDepositAccount(BankAccount):
    def deposit(self):
        print("You can deposit money in your fixed deposit account")
    def withdraw(self):
        print("You can withdraw money from your fixed deposit account")
        
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("You can deposit money in your salary account")
    def withdraw(self):
        print("You can withdraw money from your salary account")
        
class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("You can deposit money in your zero balance account")
    def withdraw(self):
        print("You can withdraw money from your zero balance account")
        
print( "---------------------Current Account-----------------")        
Akhil=CurrentAccount()
Akhil.check_balance()
Akhil.view_history()
Akhil.userinfo()
Akhil.transaction()
Akhil.deposit()
Akhil.withdraw()

print( "---------------------Savings Account-----------------")

Shiva=SavingsAccount()
Shiva.check_balance()
Shiva.view_history()
Shiva.userinfo()
Shiva.transaction()
Shiva.deposit()
Shiva.withdraw()




