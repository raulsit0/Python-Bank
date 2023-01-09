class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Customer(Person):

    def __init__(self, firstname, lastname, account_number, balance=0):
        super().__init__(firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):

         return   f"{self.firstname}, {self.lastname} my account number is {self.account_number} and my balance is {self.balance}"

    def deposit(self, add_money):
        self.balance += add_money

    def withdraw(self, take_money):
        if self.balance >= take_money:
            self.balance -= take_money


def create_client():
    first_name_ct = input("enter your name: ")
    last_name_ct = input("enter your last name: ")
    account_number = input("enter your account number: ")
    customer1 = Customer(first_name_ct, last_name_ct, account_number)

    return customer1

def start():
    my_customer = create_client()
    print(my_customer)
    option = "G"

    while option != "E":
        print("Choose: deposit (D), Withdraw (W), or exit (E)")
        option = input()

        if option == "D":
            dep_amount =int(input("Deposit amount:  "))
            my_customer.deposit(dep_amount)
        elif option == "W":
            with_amount = int(input("Withdraw amount: "))
            my_customer.withdraw(with_amount)
        print(my_customer)

    print("thank you for using my bank")

start()