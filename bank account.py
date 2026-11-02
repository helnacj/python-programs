class BankAccount:

    # Constructor
    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Current balance:", self.balance)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance!")

    # Method to display account details
    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Type:", self.account_type)
        print("Current Balance:", self.balance)


# Creating objects
account1 = BankAccount("1001", "Helna", "Savings", 10000)
account2 = BankAccount("1002", "Anu", "Current", 15000)

# Demonstrating account1
account1.display()
account1.deposit(5000)
account1.withdraw(3000)
account1.display()

# Demonstrating account2
account2.display()
account2.deposit(2000)
account2.withdraw(4000)
account2.display()