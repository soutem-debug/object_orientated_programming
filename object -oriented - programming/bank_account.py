class Account:

    def __init__(self, name, date_birth, address, contact):
        self.name = name
        self.date_birth = date_birth
        self.address = address
        self.contact = contact

    def profile(self):
        print(f"---------------------------------------")
        print(f"Customer Profile")
        print(f"---------------------------------------")
        print(f"Name:" + " ", self.name)
        print(f"D.O.B:" + " ", self.date_birth)
        print(f"Address:" + " ", self.address)
        print(f"Contact details:" + " ", self.contact)

# child class to run methods


class Banking(Account):
    def __init__(self, name, date_birth, address, contact):
        super().__init__(name, date_birth, address, contact)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Balance total after deposit: £", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to withdraw" "/ Balance available: £", self.balance)
        else:
            self.balance = self.balance - amount
            print("Balance has been updated", "£",self.balance)

    def get_balance(self):
        self.profile()
        self.balance = 0
        print("Account balance is: £")


oslo = Banking("Oslo", "09/05/1982", "The Millennium Dome", "07895 303 1985")
milo = Banking("Milo", "08/11/1975", "The Blackpool Tower", "07851 623 3010")
oslo.get_balance()

oslo.deposit(1000)
oslo.deposit(100)
oslo.withdraw(300)
print(oslo.get_balance)

milo.get_balance()
milo.deposit(50)
milo.deposit(100)
milo.withdraw(300)
print(milo.get_balance)










