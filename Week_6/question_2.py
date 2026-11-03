class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance              # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited: {amount}")
        else:
            print("Invalid deposit! Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal! Amount must be positive.")

        elif amount > self.__balance:
            print("Insufficient balance!")

        else:
            self.__balance -= amount
            print(f"Successfully withdrawn: {amount}")

    def get_balance(self):
        print(f"Current balance: {self.__balance}")



account = BankAccount("Abebe", 5000)

# Depositing money
account.deposit(1000)

# Withdrawing money
account.withdraw(2000)

# Displaying balance
account.get_balance()