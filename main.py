# Need some more Work around I guess. 

class Account:
    def __init__(self, balance = 0):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount)
        if amount > 0:
            self.balance = self.balance + amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return True
        else: 
            return False

class Bank:
    no_customers = 0

    def __init__(self, bank_name, customers):
        self.bank_name = bank_name
        self.customers = customers

    def add_customer(self, f: str, l: str):
        self.customers.append(Customer(f, l))
        self.no_customers += 1

    def get_number_of_customers(self):
        return self.no_customers

    def get_customer(self, index: int):
        return self.customers[index]

class Customer:
    def __init__(self, firstName, lastName):
        self.firstname = firstName
        self.lastname = lastName
        self.account = Account()

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_account(self):
        return self.account

    def set_account(self, acnt):
        self.account = acnt

def main():
    customers = []
    mandiri = Bank('BANK MANDIRI', customers)
    default = Account(0)

    def menu():
        print('What would you like to do?')
        user_input = input('1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Exit\n--> ')

        if u_Input == '1':
            firstname = input('\nFirst name: ')
            lastname = input('Last name: ')
            bca.add_customer(firstname, lastname)
            bca.get_customer(len(customers)-1).set_account(Account(50000))
            print('\nAccount successfully created with a balance of 50000!\n')
            menu()

        elif u_Input == '2':

            if len(customers) == 0:
                print(f'\nYour current balance: {default.get_balance()}\n')
            else:
                print(f'\nYour current balance: {bca.get_customer(len(customers)-1).get_account().get_balance()}\n')
            menu()

        elif u_Input == '3':
            amt_to_deposit = int(input('\nEnter the amount to deposit: '))

            if len(customers) == 0:
                result = default.deposit(amt_to_deposit)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')

            else:
                result = bca.get_customer(len(customers)-1).get_account().deposit(amt_to_deposit)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')
            menu()

        elif u_Input == '4':
            amt_to_withdraw = int(input('\nAmount to withdraw: '))

            if len(customers) == 0:
                result = default.withdraw(amt_to_withdraw)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')

            else:
                result = bca.get_customer(len(customers)-1).get_account().withdraw(amt_to_withdraw)
                if result is True:
                    print('\nTransaction Successful!\n')
                else:
                    print('\nTransaction Unsuccessful!\n')
            menu()

        elif u_Input == '5':
            print('\nThanks for using Bank Mandiri')

    menu()


if __name__ == "__main__":
    main()





