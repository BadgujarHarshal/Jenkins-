class Bank_Account:
    def __init__(self,name,account_number,account_type,balance=0.0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    def deposit(self,amount):
        if amount> 0:
            self.balance += amount
            print(f" Deposited{amount}.new balance: {self.balance}")
        else:
            print("Error")
    def withdrew(self,amount):
        if amount> 0 and self.balance>= amount:
            self.balance -= amount
            print(f" Withdrew{amount}.new balance: {self.balance}")
        else:
            print("Insufficient Balance.")
    def display(self):
        print(f"Account Holder:",self.name)
        print(f"Account Number:",self.account_number)
        print(f"Account Type:",self.account_type)
        print(f"Balance:",self.balance)
def main():
    bank_account = None
    while True:
        print("\nBank Account Menu:")
        print("1. New Customer")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Display")
        print("5. Exit")
        choice= int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter Depositor's name:")
            account_number = int(input("Enter account number:"))
            account_type = input("Enter account type: Saving Or Current")
            balance = float(input("Enter initial balance:"))
            bank_account = Bank_Account(name, account_number, account_type, balance)
            print(f"Account created successfully for {name}")
        elif choice == 2:
            amount = float(input("Enter the deposit amount:"))
            bank_account.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter the withdrawal amount:"))
            bank_account.withdrew(amount)
        elif choice == 4:
            bank_account.display()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
