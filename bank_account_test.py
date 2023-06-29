#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 3/15/2023
#Project: BankAccount Class Unit Test
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Using the attached Python class, write a unit test program to test it's complete 
#functionality, which means you test every method for correctness. There are errors, your job 
#is not to fix them, but to find them with unit testing."
#--------------------------------------------------------------------------------------------
#Algorithm
#-----------------
#Step 1) Test all edge casses for each method and constructor.
#Step 2) Display results.
#--------------------------------------------------------------------------------------------
import unittest
from bankaccount import BankAccount

#The purpose of this class is to test every case possible in the BankAccount class.
class Bank_Account_Test(unittest.TestCase):

    #First test: used to ensure contructor default values sets to 0 or specified value.
    def test_constructor(self):

        #Test defualt value scenario. (Edge Case)
        bank_object1 = BankAccount()
        self.assertEqual(0, bank_object1._balance)

        #Test the positive value scenario. (Edge Case)
        bank_object2 = BankAccount(5)
        self.assertEqual(5, bank_object2._balance)

        #Test the negative value scenario. (Edge Case)
        #Must banks will not let an individual start an account with a neg. balance.
        bank_object3 = BankAccount(-5)
        self.assertEqual(0, bank_object3._balance)

    #Second test: used to ensure deposit method functions properly.
    def test_deposit(self) :

        #Test the positive value scenario. (Edge Case)
        bank_object = BankAccount(0)
        bank_object.deposit(5)
        self.assertEqual(5, bank_object._balance)

        #Test the negative value scenario. (Edge Case)
        #A deposit is a positive value. This should not be allowed.
        bank_object.deposit(-5)
        self.assertEqual(5, bank_object._balance)

    #Third test: used to ensure withdraw method functions properly and the penalty is added
    #if an overdraft is attempted.
    def test_withdraw(self) :

        #Test balance > withdraw scenario. (Edge Case)
        bank_object = BankAccount(20)
        bank_object.withdraw(5)
        self.assertEqual(15, bank_object._balance)

        #Test balance < withdraw scenario. (Edge Case)
        bank_object.withdraw(1000)
        self.assertEqual(5, bank_object._balance)

        #Test balance == withdraw scenario. (Edge Case)
        bank_object.withdraw(5)
        self.assertEqual(0, bank_object._balance)

    #Fourth test: used to ensure addInterest method functions properly.
    def test_addInterest(self) :

        #Test positive value scenario. (Edge Case)
        bank_object1 = BankAccount(10)
        bank_object1.addInterest(10)
        self.assertEqual(11, bank_object1._balance)

        #Test zero value scenario. (Edge Case)
        bank_object2 = BankAccount(10)
        bank_object2.addInterest(0)
        self.assertEqual(10, bank_object2._balance)

        #Test negative value scenario. (Edge Case)
        #There is no such thing as a negative interest. Do not allow.
        bank_object3 = BankAccount(10)
        bank_object3.addInterest(-10)
        self.assertEqual(10, bank_object3._balance)

    #Fifth test: used to ensure getBalance method functions properly.
    def test_getBalance(self) :

        #Test positive value scenario. (Edge Case)
        bank_object = BankAccount(10)
        self.assertEqual(10, bank_object._balance)

        #Test zero value scenario. (Edge Case)
        bank_object = BankAccount(0)
        self.assertEqual(0, bank_object._balance)

        #Test negative value scenario. (Edge Case)
        bank_object = BankAccount(-10)
        self.assertEqual(-10, bank_object._balance)        

#Run unnittest main if ran as main.
if __name__ == '__main__':
    unittest.main()