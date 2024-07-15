class BankAccount:
    def __init__(self, account_balance =0 ):
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
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${account_balance}")
