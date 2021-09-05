import re


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = str(pin)
        self.password = password

    def change_name(self, new_name):
        # new_name = input("New name: ")
        if not re.search(r"^[a-z]\w{1,10}$", new_name, flags=re.IGNORECASE):
            print(
                "User names must be between 2-10 characters long, begin with a letter and contain no spaces or special characers.")
            return
        self.name = new_name

    def change_pin(self, new_pin):
        # new_pin = input("New PIN: ")
        new_pin = str(new_pin)
        if not re.search(r"^\d{4}$", new_pin):
            print("PIN must be axactly 4 digits.")
            return
        if new_pin == self.pin:
            print("Your new pin is the same as the old one!!!")
        self.pin = new_pin

    def change_password(self, new_password):
        # new_password = input("New password: ")
        new_password = str(new_password)
        if not re.search(r"(?=.{5,})(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=_\-!?])", new_password):
            print(
                "Passwords must be at least 5 characers long and contain at least: one uppercase, one lowercase one digit and one special character .")
        if (new_password == self.password):
            print("The new passwords different from your previous")
            return
        self.password = new_password


class Bank_User(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def show_balance(self):
        print(f"{self.name} has a current balace of: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.check_holds(False, ''):
            return False
        amount = self.check_amount(amount, "to withdraw ")
        if (type(amount) == float):
            if (self.balance >= amount):
                self.balance -= amount
                return True
            else:
                return self.cancel_transaction("Insuficent funds")
        return self.cancel_transaction(amount)

    def deposit(self, amount):
        if self.check_holds(False, ''):
            return False
        amount = self.check_amount(amount, "to deposit ")
        if (type(amount) == float):
            self.balance += amount
            return True
        return self.cancel_transaction(amount)

    def transfer_money(self, amount, user):
        amount = self.check_amount(amount, "to transfer ")
        if (type(amount) == float):
            print(f"You are transfering ${amount:.2f} to {user.name}")
            if self.check_holds(user.on_hold, user.name):
                return False
            print("Authentication required")
            PIN_check = self.check_PIN(input("Enter your PIN: "))
            if PIN_check == True:
                print("Transfer Authorized")
                if user.deposit(amount):
                    self.withdraw(amount)
                    print(f"Transfering ${amount:.2f} to {user.name}")
                    return True
                else:
                    return False
            return self.cancel_transaction(PIN_check)
        return self.cancel_transaction(amount)

    def request_money(self, amount, user):
        amount = self.check_amount(amount, "requested ")
        if (type(amount) == float):
            print(f"You are requesting ${amount:.2f} from {user.name}")
            if self.check_holds(user.on_hold, user.name):
                return False
            print("User uthentication required...")
            PIN_check = user.check_PIN(input(f"Enter {user.name}'s PIN: "))
            if PIN_check != True:
                return self.cancel_transaction(PIN_check)
            pass_check = self.check_password(input(f"Enter your password: "))
            if pass_check != True:
                return self.cancel_transaction(pass_check)
            print("Request Authorized")
            if user.withdraw(amount):
                self.deposit(amount)
                print(f"{user.name} sent ${amount:.2f}")
                return True
            return False
        return self.cancel_transaction(amount)

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

    def check_amount(self, amount, action):
        try:
            amount = float(amount)
            if amount < 0:
                return(f"Amount {action}must be a positive number.")
            return amount
        except:
            return(f"Amount {action}must be numeric.")

    def toggle_hold(self):
        self.on_hold = not self.on_hold

    def check_holds(self, users_hold, user_name):
        if self.on_hold:
            return not self.cancel_transaction("This account is on hold.")
        if users_hold:
            return not self.cancel_transaction(f"{user_name}'s account is on hold.")
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
user2.change_password('invl')
user2.change_password('P4ss!')
user2.change_pin('1111')

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
