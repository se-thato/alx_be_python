class BankAccount:
    def __init__(self, account_balance =250 ):
        #initialize the bank account
        self._account_balance = account_balance

    def deposit(self, amount):
        #deposit the amount into the account
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                return True
            else:
                return "Insufficient funds."
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
        
    def display_balance(self):
        return f"Current Balance: ${self._account_balance}"
