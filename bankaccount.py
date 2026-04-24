class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = 1234567891
        self.balance = 10000000000000
        def deposit(self, amount):
            if amount > 0:
                self.balance += amount  
                print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
            else:
                print("Invalid deposit amount. Amount must be greater than 0.")
def withdraw(self, amount):
    if 0 < amount <= self.balance:
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
def get_balance(self):
    return self.balance
def check_balance(self):
    print(f"Account Number: {self.account_number}")
    print(f"Current Balance: {self.balance:.2f}")
    return self.balance
if __name__ == "__main__":
    account = BankAccount("123456789", 1000)
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
         account.check_balance()
        elif choice == "2":
           amount = float(input("Enter amount to deposit: "))
           account.deposit(amount)
        elif choice == "3":
          amount = float(input("Enter amount to withdraw: "))
          account.withdraw(amount)
        elif choice == "4":
          print("Exiting. Have a nice day!")
        break         
    else:
        print("Invalid choice. Please select a valid option.")
