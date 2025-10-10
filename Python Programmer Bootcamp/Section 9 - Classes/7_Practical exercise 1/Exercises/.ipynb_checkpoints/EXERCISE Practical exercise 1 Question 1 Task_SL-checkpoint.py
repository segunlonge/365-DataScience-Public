# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

class BankAccount(object):
    '''
    According to the question it is required that a bank account class be created
    for displaying account balance and handling depositis and withdrawals
    
    see course solution for comprehensive answer
    '''
    def __init__(self, balance = 0.0, account_name = 'Unnamed', account_number = '00000000', deposit = 0.0, withdrawal = 0.0):
        self.balance = balance
        self.account_name = account_name
        self.account_number = account_number
        self.deposit = deposit
        self.withdrawal = withdrawal
        
    def deposit_method(self, deposit = 0.0):
        self.deposit = deposit
        
    def withdrawal_method(self, withdrawal = 0.0):
            self.withdrawal = withdrawal
        
    def calculate_balance(self):
        self.balance = self.balance - self.withdrawal + self.deposit
        if self.withdrawal > self.balance:
            print('Insufficient funds')
        else: 
            #self.balance = self.balance - self.withdrawal + self.deposit
            print(f'''Account Balance: {self.balance}, Account Holder Name: {self.account_name}''')
        
BankAccount_1 = BankAccount(
    balance = 1000000,
    account_name = "Segun Longe",
    account_number = "123456")

#BankAccount_1.deposit_method(1000000)

#BankAccount_1.withdrawal_method(1000)

BankAccount_1.calculate_balance() 

'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
