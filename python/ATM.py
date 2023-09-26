class SimpleATM:
    def __init__(self):
        self.accounts = {
            "user1": 1000.0,
            "user2": 1500.0,
            "user3": 2000.0
        }
        self.current_user = None

    def run(self):
        while True:
            print("Welcome to the Simple ATM!")
            user_id = input("Enter your User ID: ")

            if self.authenticate(user_id):
                self.current_user = user_id
                self.display_main_menu()
            else:
                print("Authentication failed. Try again.")

    def authenticate(self, user_id):
        return user_id in self.accounts

    def display_main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Logout")

            choice = input("Select an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                self.current_user = None
                return
            else:
                print("Invalid option. Try again.")

    def check_balance(self):
        balance = self.accounts[self.current_user]
        print(f"Your balance: ${balance:.2f}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        balance = self.accounts[self.current_user]

        if 0 < amount <= balance:
            self.accounts[self.current_user] = balance - amount
            print(f"Withdrawal successful. New balance: ${balance - amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        balance = self.accounts[self.current_user]

        if amount > 0:
            self.accounts[self.current_user] = balance + amount
            print(f"Deposit successful. New balance: ${balance + amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def transfer(self):
        recipient = input("Enter the recipient's User ID: ")

        if recipient in self.accounts and recipient != self.current_user:
            amount = float(input("Enter the amount to transfer: $"))
            sender_balance = self.accounts[self.current_user]
            recipient_balance = self.accounts[recipient]

            if 0 < amount <= sender_balance:
                self.accounts[self.current_user] = sender_balance - amount
                self.accounts[recipient] = recipient_balance + amount
                print("Transfer successful.")
            else:
                print("Invalid transfer amount or insufficient funds.")
        else:
            print("Invalid recipient or self-transfer.")


if __name__ == "__main__":
    atm = SimpleATM()
    atm.run()
