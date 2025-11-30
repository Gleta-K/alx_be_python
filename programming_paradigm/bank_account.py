class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance   # encapsulated attribute

    def deposit(self, amount):
        """Add money to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Deduct amount only if sufficient funds exist."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
    print(f"Current Balance: ${self.account_balance:.2f}")

