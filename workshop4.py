class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        #new_name = input("New name: ")
        self.name = new_name

    def change_pin(self, new_pin):
        #new_pin = input("New PIN: ")
        self.pin = new_pin

    def change_password(self, new_password):
        #new_password = input("New password: ")
        self.password = new_password


class Bank_User(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has a current balace of: ${self.balance}")

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            return True
        else:
            print("Insuficentfunds. Transaction cancelled.")
            return False

    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            return True
        else:
            print("Deposits must be a positive amount. Transaction cancelled.")
            return False

    def transfer_money(self, amt, user):
        print(f"You are transfering ${amt} to {user.name}")
        print("Authentication required")
        PIN_check = self.check_PIN(input("Enter your PIN: "))
        if PIN_check == True:
            print("Transfer Authorized")
            if user.deposit(amt):
                self.withdraw(amt)
                print(f"Transfering ${amt} to {user.name}")
                return True
            else:
                return False
        return self.cancel_transaction(PIN_check)

    def request_money(self, amt, user):
        print(f"You are requesting ${amt}  from {user.name}")
        print("User uthentication required...")
        PIN_check = user.check_PIN(input(f"Enter {user.name}'s PIN: "))
        if PIN_check != True:
            return self.cancel_transaction(PIN_check)
        pass_check = self.check_password(input(f"Enter your password: "))
        if pass_check != True:
            return self.cancel_transaction(pass_check)
        print("Request Authorized")
        if user.withdraw(amt):
            self.deposit(amt)
            print(f"{user.name} sent ${amt}")
            return True
        return False

    def check_PIN(self, PIN):
        if PIN == str(self.pin):
            return True
        return ("Inavlid pin.")

    def check_password(self, password):
        if self.password == password:
            return True
        return ("Inavlid password.")

    def cancel_transaction(self, err):
        print(err, " Transaction cancelled")
        return False


        # Driver Code for Task 1
"""
test_user = User("Bob", 1234, "password")
print(test_user.name, test_user.pin, test_user.password)

"""
# Driver Code for Task 2
"""
test_user = User("Bob", 1234, "password")
print(test_user.name, test_user.pin, test_user.password)
test_user.change_name("Bobby")
test_user.change_pin(4321)
test_user.change_password("newpassword")
print(test_user.name, test_user.pin, test_user.password)
 """

# Driver Code for Task 3
"""
test_user = Bank_User("Bob", 1234, "password")
print(test_user.name, test_user.pin, test_user.password, test_user.balance)
 """

# Driver Code for Task 4
"""
test_user = Bank_User("Bob", 1234, "password")
test_user.show_balance()
test_user.deposit(1000)
test_user.show_balance()
test_user.withdraw(500)
test_user.show_balance()
 """

# Driver Code for Task 5
user1 = Bank_User("Ray", 9090, "havoc")
user2 = Bank_User("Veronica", 9044, "bushy")

user2.deposit(5000)
user2.show_balance()
user1.show_balance()
did_transfer = user2.transfer_money(500, user1)
user2.show_balance()
user1.show_balance()
if (did_transfer == True):
    user2.request_money(250, user1)
    user2.show_balance()
    user1.show_balance()
