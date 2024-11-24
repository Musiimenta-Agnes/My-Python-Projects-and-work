# reating a class;
class BankAccount:

    # Adding a constructor or init function.
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance


        # Adding a method to the class
        def deposit(self,amount): # amount is the parameter and deposite is the methid name
            self.balance += amount
            print(f"The deposit is {deposit} and the new balance is {self.balance}")


            # Creating ana instance/object and calling the new method to verify its function.
account = BankAccount('1234567','10000')
print(f"Account number: {account.account_number}")
print(f"Balance: {account.balance}")
