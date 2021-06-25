class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.balance -= 5
        return self
	
    def display_account_info(self):
        print(f"Saldo: ${self.balance}")
	
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

cuenta1 = BankAccount(0.05, 1000)
cuenta2 = BankAccount()

print("cuenta1")
cuenta1.deposit(1000).deposit(2000).deposit(3000).withdraw(2000).yield_interest().display_account_info()
print(("-")*30)
print("cuenta2")
cuenta2.deposit(1000).deposit(1000).withdraw(1000).withdraw(1500).yield_interest().display_account_info()


