class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        # Ensure the deposit amount is positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.format_balance()}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        # Ensure the withdrawal amount is positive and does not exceed the current balance
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        elif amount > self.balance:
            print(f"Insufficient balance! Current balance is {self.format_balance()}.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.format_balance()}")

    def check_balance(self):
        # Display account information and formatted balance
        print(f"Account holder: {self.account_holder}, Account number: {self.account_number}, Current balance: {self.format_balance()}")

    def format_balance(self):
        # Format balance with commas as per usual bank format
        return "{:,.2f}".format(self.balance)

# Function to validate account number (12 digits)
def validate_account_number(account_number):
    if len(account_number) != 12 or not account_number.isdigit():
        raise ValueError("Account number must be exactly 12 digits.")

# Function to validate account holder's name (alphabet only)
def validate_account_holder(name):
    if not name.replace(" ", "").isalpha():
        raise ValueError("Account holder's name must contain only letters.")

# Function to create new bank accounts with validation
def create_account():
    while True:
        try:
            name = input("Enter the account holder's name: ")
            validate_account_holder(name)
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            account_number = input("Enter the account number (12 digits): ")
            validate_account_number(account_number)
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            initial_balance = float(input("Enter the initial balance: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    
    account = BankAccount(name, account_number, initial_balance)
    print(f"Account created successfully for {name} with Account number {account_number}")
    return account

# Function to show menu and perform operations
def bank_operations(account):
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    
    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        try:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid input! Please enter a valid amount.")
    
    elif option == "2":
        try:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid input! Please enter a valid amount.")
    
    else:
        # If wrong option selected, thank the customer and show the balance
        print(f"\nInvalid option selected. Here is your account information:")
        account.check_balance()
        print(f"Thank you for banking with us, {account.account_holder}!")

# Example usage
if __name__ == "__main__":
    account = create_account()
    bank_operations(account)
