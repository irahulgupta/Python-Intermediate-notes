#---------------------------------------------
#OOP
#----------------------------------------------
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount, bonus=0):
        self.__balance += amount + bonus
        print(f"{self.account_holder} deposited {amount} with bonus {bonus}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.account_holder} withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print(f"Insufficient balance for {self.account_holder}")

    def get_balance(self):
        return self.__balance

    def display_account_type(self):
        raise NotImplementedError("Subclass must implement this method")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, minimum_balance):
        super().__init__(account_number, account_holder, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.minimum_balance:
            current_balance = self.get_balance() - amount
            print(f"{self.account_holder} withdrew {amount} from Savings Account. Remaining balance: {current_balance}")
            self._BankAccount__balance = current_balance
        else:
            print(f"Withdrawal denied for {self.account_holder}. Minimum balance must be maintained.")

    def display_account_type(self):
        print(f"{self.account_holder} has a Savings Account")


class CurrentAccount(BankAccount):
    def display_account_type(self):
        print(f"{self.account_holder} has a Current Account")


print("MODULE 2 HANDS-ON: BANKING SYSTEM APPLICATION")
print("-" * 55)

account1 = SavingsAccount("SA101", "Rahul", 10000, 2000)
account2 = CurrentAccount("CA201", "Anita", 15000)

print("\n1. CLASSES AND OBJECTS")
print("Created two account objects successfully")

print("\n2. INHERITANCE AND POLYMORPHISM")
accounts = [account1, account2]

for account in accounts:
    account.display_account_type()

print("\n3. ENCAPSULATION")
print(f"Rahul's balance: {account1.get_balance()}")
print(f"Anita's balance: {account2.get_balance()}")

print("\n4. METHOD OVERRIDING")
account1.withdraw(3000)
account2.withdraw(5000)

print("\n5. METHOD OVERLOADING STYLE USING DEFAULT ARGUMENT")
account2.deposit(2000)
account2.deposit(2000, 500)

print("\n6. FINAL BALANCES")
print(f"Rahul's final balance: {account1.get_balance()}")
print(f"Anita's final balance: {account2.get_balance()}")
