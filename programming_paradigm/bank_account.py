class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        #Adds specified amount to the account balance
        if amount > 0:
            self.account_balance += amount
        else:
            print('Deposited amount must be positive')

    def withdraw(self, amount):
        #Deducts specified amount from the account balance if funds are sufficient.
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False

    def display_balance(self):
        #Prints the current balance in a user-friendly format
        print(f'Current Balance: ${self.account_balance:.2f}')
    
