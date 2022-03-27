from random import randrange

class Person():
    def __init__(self,id,first_name,last_name):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name


class Account ():
    def __init__(self,number,type,owner):
        self.acc_num=number
        self.type=type
        self.owner=owner
        self.balance=0.0

class Bank():
    def __init__(self):
        self.customer_list={}
        self.accounts_list={}


        def add_customer(self, first_name, last_name):
            cust_id=randrange(1000)
            while cust_id in self.customer_list:  # if id exist  go inside while loop and generate new id
                cust_id =randrange(1000)  # assigning random no to cust_list
            self.customer_list[cust_id]=Person(cust_id,first_name,last_name)

       def add_account(self,type,owner):
           acc_id=randrange(1000)
           if owner not in  self.accounts_list:
               print("Invalid cust  id")
           while acc_id  in self.accounts_list:
               id=randrange(1000)
           self.accounts_list[acc_id]=Account(acc_id,type,owner)


       def remove_account(self,acc_id):
           del self.accounts_list[acc_id]

       def deposit(self,acc_id,amount):
           self.accounts_list[acc_id].balance+=amount

       def withdraw(self,acc_id,amount):
           self.accounts_list[acc_id].balance-=amount

       def balance(self,acc_id):
           print(self.accounts_list[acc_id].balance)