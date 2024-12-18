# Name: Navjot Singh and Sartaj Singh
# Date: June 22, 2024.
# Modified: June 22, 2024.
# Description: This program allows user to run the "unittest" test cases
# Based on the users input.

import unittest
from test_Lab3_Navjot_Sartaj import TestCaseCalculations

# A function to define the menu options.
def my_suite():
    # Define the menu options to be displayed to the user.
    menu = """
    Please enter one of the following options:
    - 'c' for testing area of circle.
    - 't' for testing area of trapezium.
    - 'e' for testing area of ellipse.
    - 'r' for testing area of rhombus.
    - 'q' to quit the program.
    What would you like to do?
    """
    # Ask the user to enter the choice.
    selected_option = input(menu)

    while selected_option != "q":
        # A new test suite for each selected option
        suite = unittest.TestSuite()

        # Add the test case for testing area of circle.
        if selected_option == "c":
            suite.addTest(TestCaseCalculations('test_area_circle'))
        # Add the test case for testing area of trapezium.
        elif selected_option == "t":
            suite.addTest(TestCaseCalculations('test_area_trapezium'))
        # Add the test case for testing area of ellipse.
        elif selected_option == "e":
            suite.addTest(TestCaseCalculations('test_area_ellipse'))
        # Add the test case for testing area of rhombus.
        elif selected_option == "r":
            suite.addTest(TestCaseCalculations('test_area_rhombus'))
        # If choice is anything other, print error message.
        else:
            print("Please try again.")

        if selected_option in ['c', 't', 'e', 'r']:
            # A new test runner for running the test suite
            runner = unittest.TextTestRunner()
            runner.run(suite)

        # Ask the user again for next option.
        selected_option = input(menu)

    # Greet the user at the end.
    print("Have a Good Day!")

my_suite()