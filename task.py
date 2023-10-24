#
#AccountInfoing simulator. Write a code in python that simulates the AccountInfoing system. 
#The program should:
# - be able to create new AccountInfos
# - store client information in AccountInfos
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Bank:
    def __init__(self, bankname):
        self.bankname = bankname

class AccountInfo:
    def __init__(self, name, cash_on_account, bankname):
        self.name = name
        self.cash_on_account = cash_on_account
        Bank.bankname = bankname

    def __str__(self):
        return 'Name: ' + str(self.name) + ', money: ' + str(self.cash_on_account)

    def cash_input(self, add_money):
        self.cash_on_account = self.cash_on_account + add_money

    def send_money(self, how_much_money, clientX):
        self.cash_on_account = self.cash_on_account-how_much_money
        clientX.cash_on_account = clientX.cash_on_account + how_much_money


if __name__ == "__main__":
    bank1 = Bank("BestBankEver")

    client1 = AccountInfo("Jakub", 123, bank1)
    print(client1)
    client1.cash_input(12)
    print(client1)

    client2 = AccountInfo("Witek", 100, bank1)
    print(client2)

    client1.send_money(20, client2)
    print(client1)
    print(client2)







