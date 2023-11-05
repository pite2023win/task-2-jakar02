import logging
import multiprocessing
import threading
import queue
from queue import Empty

logging.basicConfig(filename='account_info.log', level=logging.INFO)

class Account:
    def __init__(self, account_id, name_surname):
        self.account_id = account_id
        self.name_surname = name_surname
        self.money = 0

    def deposit(self, money_to_deposit):
        self.money = self.money + money_to_deposit

    def withdraw(self, money_to_withdraw):
        if self.money - money_to_withdraw >= 0:
            self.money = self.money - money_to_withdraw
        else:  
            logging.error("Not enough money. You need %s more.", money_to_withdraw - self.money)

    def transfer_money(self, account_to_transfer, money_to_transfer):
        if self.money - money_to_transfer >= 0:
            self.money = self.money - money_to_transfer
            account_to_transfer.money = account_to_transfer.money + money_to_transfer
        else:  
            logging.error("Not enough money. You need %s more.", money_to_transfer - self.money)

    def get_account_info(self):
        return f'Account_id: {self.account_id}\nName Surname: {self.name_surname}\nMoney: {self.money}\n'


class AccountInfo:
    number_of_accounts = 0

    def __init__(self):
        self.list_of_all_accounts = []

    @staticmethod
    def sum_of_money_in_bank(list_of_everyone):
        sum = 0
        for account in list_of_everyone:
            sum = sum + account.money
        return sum
    
    def new_account(self, acc_id, name_surname):
        if acc_id not in self.list_of_all_accounts:
            new_account = Account(acc_id, name_surname)
            self.list_of_all_accounts.append(new_account)
            AccountInfo.number_of_accounts = AccountInfo.number_of_accounts + 1
        else:
            logging.error("Account with this ID already exsist.")

    def get_account(self, id):
        for account in self.list_of_all_accounts:
            if id == account.account_id:
                return account
        else:
            return None

    def deposit(self, id, money_to_deposit):
        account = self.get_account(id)
        if account is not None:
            account.deposit(money_to_deposit)
        else:
            logging.error("Account with ID %s not found.", id)
            
    def withdraw(self, id, money_to_withdraw):
        account = self.get_account(id)
        if account is not None:
            account.withdraw(money_to_withdraw)
        else:
            logging.error("Account with ID %s not found.", id)

    def transfer_money(self, id, id_to_send, money_to_transfer):
        account = self.get_account(id)
        account_to_send = self.get_account(id_to_send)
        account.transfer_money(account_to_send, money_to_transfer)

    def get_accounts_info(self):
        for account in self.list_of_all_accounts:
            logging.info("%s\n-------------------------", account.get_account_info())

    def find_the_most_rich_person(func):
        def inner(*args, **kwargs):
            logging.info("Searching for the richest person...")
            richest_person = func(*args, **kwargs)
            return richest_person
        return inner

    @find_the_most_rich_person
    def find(self):
        richest_person = self.list_of_all_accounts[0]
        for account in self.list_of_all_accounts:
            if account.money > richest_person.money:
                richest_person = account
        return richest_person.name_surname, richest_person.money


if __name__ == "__main__":
    obj = AccountInfo()
    obj.new_account(1, "Adam Paleczny")
    obj.new_account(2, "Witek Dabrawski")
    obj.new_account(3, "Bartek Sekalski")
    obj.get_accounts_info()
    obj.deposit(2, 100)
    obj.deposit(1, 50)
    obj.deposit(3, 200)
    obj.withdraw(1, 10)
    obj.withdraw(1, 10)
    obj.withdraw(2, 20)
    obj.transfer_money(2,1,40)
    obj.transfer_money(1,2,30)
    obj.transfer_money(1,2,15)
    obj.get_accounts_info()
    logging.info(obj.sum_of_money_in_bank(obj.list_of_all_accounts))
    name1, money1 = obj.find()
    logging.info(f'Name: {name1}, money: {money1}')
    logging.info(AccountInfo.number_of_accounts)
    obj.withdraw(1, 1000)

    data = "4, Ambrozy Gajda\n5, Jackie Chan\n6, James Bond"
    file_path = "data.txt"
    with open(file_path, "w") as file:
        file.write(data)
    parsed_data = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            obj.new_account(int(parts[0]), parts[1])
    obj.get_accounts_info()
    
    deposit_thread = threading.Thread(target=obj.deposit, args=(4, 1000))
    withdraw_thread = threading.Thread(target=obj.withdraw, args=(3, 20))
    deposit_thread.start()
    withdraw_thread.start()
    deposit_thread.join()
    withdraw_thread.join()
    obj.get_accounts_info()

    


