# Author: Edwinah Lynn Ninsiima
# Date: 13/08/2024
# Description: Testing the manager module functions on a banking website to see if the website is working well
# Module: Test suite

# Import Unnittest
import unittest

# Imoport the nine module files,import all the classes
from test_new_Customer import TestNewCustomer
from test_customized_statement import CustomizedStatement
from test_balance_enquiry import BalanceEnquiryTest
from test_delete_customer import DeleteCustomerTest
from test_mini_statement import MiniStatementTest
from test_delete_account import DeleteAccountTest
from test_edit_customer import EditCustomerTest
from test_edit_account import EditAccountTest
from test_new_account import NewAccountTest


# Create function that diplays a menu the manager will pick from 
def menu():
    menu = """
    Welcome Manager
    What module would you like to test:
    - '1' New Customer module
    - '2' Edit Customer module
    - '3' Delete customer module
    - '4' New Account module
    - '5' Edit Account module
    - '6' Delete Account module
    - '7' Balance Enquiry module
    - '8' Mini Statement module
    - '9' Customerized Statement module
    - 'x' Press x to exit the program
    """
    # Create a variable for the while loop
    is_valid = True
  
    # Create a while loop
    while is_valid == True:

        # Call the function with the menu
        number = input(menu)
        
        # If the input is 1
        if number == "1":
            # Test and run all the test case functions for the new customer module
            suite = unittest.TestSuite()
            suite.addTest(TestNewCustomer('test_Case_01'))
            suite.addTest(TestNewCustomer('test_Case_02'))
            suite.addTest(TestNewCustomer('test_Case_03'))
            suite.addTest(TestNewCustomer('test_Case_04'))
            suite.addTest(TestNewCustomer('test_Case_05'))
            suite.addTest(TestNewCustomer('test_Case_06'))
            suite.addTest(TestNewCustomer('test_Case_07'))
            suite.addTest(TestNewCustomer('test_Case_08'))
            suite.addTest(TestNewCustomer('test_Case_09'))
            suite.addTest(TestNewCustomer('test_Case_10'))
            suite.addTest(TestNewCustomer('test_Case_11'))
            suite.addTest(TestNewCustomer('test_Case_12'))
            suite.addTest(TestNewCustomer('test_Case_13'))
            suite.addTest(TestNewCustomer('test_Case_14'))
            suite.addTest(TestNewCustomer('test_Case_15'))
            suite.addTest(TestNewCustomer('test_Case_16'))
            suite.addTest(TestNewCustomer('test_Case_17'))
            suite.addTest(TestNewCustomer('test_Case_18'))
            suite.addTest(TestNewCustomer('test_Case_19'))
            suite.addTest(TestNewCustomer('test_Case_20'))
            suite.addTest(TestNewCustomer('test_Case_21'))
            suite.addTest(TestNewCustomer('test_Case_22'))
            suite.addTest(TestNewCustomer('test_Case_23'))
            suite.addTest(TestNewCustomer('test_Case_24'))
            suite.addTest(TestNewCustomer('test_Case_25'))
            suite.addTest(TestNewCustomer('test_Case_26'))
            suite.addTest(TestNewCustomer('test_Case_27'))
            suite.addTest(TestNewCustomer('test_Case_28'))

            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the entered input and loop back to the menu
            number = " "

        # If the input is 2
        elif number == "2":
            # Test and run all the test case functions for the edit customer module
            suite = unittest.TestSuite()
            suite.addTest(EditCustomerTest('test_Case_01'))
            suite.addTest(EditCustomerTest('test_Case_02'))
            suite.addTest(EditCustomerTest('test_Case_03'))
            suite.addTest(EditCustomerTest('test_Case_04'))
            suite.addTest(EditCustomerTest('test_Case_05'))
            suite.addTest(EditCustomerTest('test_Case_06'))
            suite.addTest(EditCustomerTest('test_Case_07'))
            suite.addTest(EditCustomerTest('test_Case_08'))
            suite.addTest(EditCustomerTest('test_Case_09'))
            suite.addTest(EditCustomerTest('test_Case_10'))
            suite.addTest(EditCustomerTest('test_Case_11'))
            suite.addTest(EditCustomerTest('test_Case_12'))
            suite.addTest(EditCustomerTest('test_Case_13'))
            suite.addTest(EditCustomerTest('test_Case_14'))
            suite.addTest(EditCustomerTest('test_Case_15'))
            suite.addTest(EditCustomerTest('test_Case_16'))
            suite.addTest(EditCustomerTest('test_Case_17'))
            suite.addTest(EditCustomerTest('test_Case_18'))
            suite.addTest(EditCustomerTest('test_Case_19'))
            suite.addTest(EditCustomerTest('test_Case_20'))

            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the entered input and loop back to the menu
            number = " "

        # If the input is 3
        elif number == "3":
            # Test and run all the test case functions for delete customer module
            suite = unittest.TestSuite()
            suite.addTest(DeleteCustomerTest('test_Case_01'))
            suite.addTest(DeleteCustomerTest('test_Case_02'))
            suite.addTest(DeleteCustomerTest('test_Case_03'))
            suite.addTest(DeleteCustomerTest('test_Case_04'))
            suite.addTest(DeleteCustomerTest('test_Case_05'))
            suite.addTest(DeleteCustomerTest('test_Case_06'))
            suite.addTest(DeleteCustomerTest('test_Case_07'))
            suite.addTest(DeleteCustomerTest('test_Case_08'))

            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the entered input and loop back to the menu
            number = " "

        # If the input is 4
        elif number == "4":
            # Test and run all the test case functions for the new account module
            suite = unittest.TestSuite()
            suite.addTest(NewAccountTest('test_Case_01'))
            suite.addTest(NewAccountTest('test_Case_02'))
            suite.addTest(NewAccountTest('test_Case_03'))
            suite.addTest(NewAccountTest('test_Case_04'))
            suite.addTest(NewAccountTest('test_Case_05'))
            suite.addTest(NewAccountTest('test_Case_06'))
            suite.addTest(NewAccountTest('test_Case_07'))
            suite.addTest(NewAccountTest('test_Case_08'))
            suite.addTest(NewAccountTest('test_Case_09'))
            suite.addTest(NewAccountTest('test_Case_10'))
            suite.addTest(NewAccountTest('test_Case_11'))
            suite.addTest(NewAccountTest('test_Case_12'))
            suite.addTest(NewAccountTest('test_Case_13'))
            suite.addTest(NewAccountTest('test_Case_14'))
            suite.addTest(NewAccountTest('test_Case_15'))
            suite.addTest(NewAccountTest('test_Case_16'))

            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the enetered input and loop back to the menu
            number = " "

        # If the input is 5
        elif number == "5":
            # Test and run all the test case functions for edit account module
            suite = unittest.TestSuite()
            suite.addTest(EditAccountTest('test_Case_01'))
            suite.addTest(EditAccountTest('test_Case_02'))
            suite.addTest(EditAccountTest('test_Case_03'))
            suite.addTest(EditAccountTest('test_Case_04'))
            suite.addTest(EditAccountTest('test_Case_05'))
            suite.addTest(EditAccountTest('test_Case_06'))
            suite.addTest(EditAccountTest('test_Case_07'))
            suite.addTest(EditAccountTest('test_Case_08'))

            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the enetered input and loop back to the menu
            number = " "

        # If the input is 6
        elif number == "6":
            # Test and run all the test case functions for delete account module
            suite = unittest.TestSuite()
            suite.addTest(DeleteAccountTest('test_Case_01'))
            suite.addTest(DeleteAccountTest('test_Case_02'))
            suite.addTest(DeleteAccountTest('test_Case_03'))
            suite.addTest(DeleteAccountTest('test_Case_04'))
            suite.addTest(DeleteAccountTest('test_Case_05'))
            suite.addTest(DeleteAccountTest('test_Case_06'))
            suite.addTest(DeleteAccountTest('test_Case_07'))
            suite.addTest(DeleteAccountTest('test_Case_08'))

            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the enetered input and loop back to the menu
            number = " "
        
        # If the input is 7
        elif number == "7":
            # Test and run all the test case functions for balance enquiry module
            suite = unittest.TestSuite()
            suite.addTest(BalanceEnquiryTest('test_Case_01'))
            suite.addTest(BalanceEnquiryTest('test_Case_02'))
            suite.addTest(BalanceEnquiryTest('test_Case_03'))
            suite.addTest(BalanceEnquiryTest('test_Case_04'))
            suite.addTest(BalanceEnquiryTest('test_Case_05'))
            suite.addTest(BalanceEnquiryTest('test_Case_06'))
            suite.addTest(BalanceEnquiryTest('test_Case_07'))
            
            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the enetered input and loop back to the menu
            number = " "

        # If the input is 8
        elif number == "8":
            # Test and run all the test case functions for the mini statment module
            suite = unittest.TestSuite()
            suite.addTest(MiniStatementTest('test_Case_01'))
            suite.addTest(MiniStatementTest('test_Case_02'))
            suite.addTest(MiniStatementTest('test_Case_03'))
            suite.addTest(MiniStatementTest('test_Case_04'))
            suite.addTest(MiniStatementTest('test_Case_05'))
            suite.addTest(MiniStatementTest('test_Case_06'))
            suite.addTest(MiniStatementTest('test_Case_07'))
            suite.addTest(MiniStatementTest('test_Case_08'))
            
            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the enetered input and loop back to the menu
            number = " "

        # If the input is nine
        elif number == "9":
            # Test and run all the test case functions for the customized statment module
            suite = unittest.TestSuite()
            suite.addTest(CustomizedStatement('test_Case_01'))
            suite.addTest(CustomizedStatement('test_Case_02'))
            suite.addTest(CustomizedStatement('test_Case_03'))
            suite.addTest(CustomizedStatement('test_Case_04'))
            suite.addTest(CustomizedStatement('test_Case_05'))
            suite.addTest(CustomizedStatement('test_Case_06'))
            suite.addTest(CustomizedStatement('test_Case_07'))
            suite.addTest(CustomizedStatement('test_Case_08'))
            suite.addTest(CustomizedStatement('test_Case_09'))
            suite.addTest(CustomizedStatement('test_Case_10'))
            suite.addTest(CustomizedStatement('test_Case_11'))
            suite.addTest(CustomizedStatement('test_Case_12'))
            suite.addTest(CustomizedStatement('test_Case_13'))
            suite.addTest(CustomizedStatement('test_Case_14'))
            suite.addTest(CustomizedStatement('test_Case_15'))
            suite.addTest(CustomizedStatement('test_Case_16'))
            suite.addTest(CustomizedStatement('test_Case_17'))

            # Create an instance of TextTestRunner,execute the test suite and print the results
            runner = unittest.TextTestRunner()
            print(runner.run(suite))

            # Remove the enetered input and loop back to the menu
            number = " "

        # If the input is x or X, exit the program
        elif number == "x" or number == "X":
            is_valid = False

        # If the input is anything else
        else:
            # Display an error message and remove the entered input and loop back to the menu
            print("Please enter a choice from the menu")
            number = " "

menu()