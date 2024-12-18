# Author: Navjot Singh
# Date: 13/08/2024
# Description: Testing the manager module functions on a banking website to see if the website is working well
# Module: New Account

# Import all the important functions
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  WebDriverException
import time 
from selenium.webdriver.common.keys import Keys

# Declare the URL that will be used
URL = "https://demo.guru99.com/V4/manager/addAccount.php"
LOGIN_URL = "https://demo.guru99.com/V4/"

# Declare the login details
USER_ID = "mngr582991"
PASSWORD = "AtUmujE"

# Declare the input to be entered in the text box fields
BLANK = ""
WORD_CHARACTER = "nine"
NUMBERS_WITH_SPACE = "23 456"
SPECIAL_CHARACTERS = "@#!"
FIRST_CHARACTER_IS_BLANK = " "
VALID_INPUT = "64772"
INVALID_INPUT = "987654"
NEW_CUSTOMER_ID = "12345"
NEW_INITIAL_DEPOSIT = "400000"
EXISTING_DEPOSIT = "10000"
MANAGER_ID = "Manger Id : mngr582991"

# Declare the expected messages
ERROR_MESSAGE = "Customer ID is required"
ERROR_MESSAGE_2 = "Characters are not allowed"
ERROR_MESSAGE_3 = "Special characters are not allowed"
ERROR_MESSAGE_4 = "First character cannot have space"
ERROR_MESSAGE_5 = "Initial Deposit must not be blank"
ERROR_MESSAGE_6 =  "Customer does not exist!!"
SUCCESS_MESSAGE = "Account Generated Successfully!!!"

# Create the class for the test cases
class NewAccountTest(unittest.TestCase):

    # Create a setup method for the class
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()

            # Call the login function
            cls.login(cls)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Create a function that will log into the website at the beginning of the test
    def login(self):
        try:
            driver = self.driver
            driver.get(LOGIN_URL)
            time.sleep(2)

            # Log into the website using password and user id
            user_id = driver.find_element(By.NAME, "uid")
            user_id.send_keys(USER_ID)

            password = driver.find_element(By.NAME, "password")
            password.send_keys(PASSWORD)
            time.sleep(1)

            login = driver.find_element(By.NAME, "btnLogin")
            login.click()
            time.sleep(1)

            # Find and click on the new account module
            new_account_tab = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/ul[1]/li[5]/a[1]")
            new_account_tab.click()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For customer id field
    # Test Case when blank input is entered in the customer id field
    def test_Case_01(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the blank input
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(BLANK)
            customer_id.send_keys(Keys.TAB)
            time.sleep(2)

            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when characters are entered in the customer id field
    def test_Case_02(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter word characters
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(WORD_CHARACTER)
            time.sleep(2)

            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_2, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when special characters are entered in the customer id field
    def test_Case_03(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter special characters
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(SPECIAL_CHARACTERS)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_3, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when numbers with spaces are entered in the customer id field
    def test_Case_04(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter numbers with space
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(NUMBERS_WITH_SPACE)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_2, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when the first character entered in the customer id field is blank
    def test_Case_05(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter the first character as a blank space
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(FIRST_CHARACTER_IS_BLANK)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_4, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # For initial deposit field
    # Test Case when blank input is entered in the initial deposit field
    def test_Case_06(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter blank input
            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(BLANK)
            initial_deposit.send_keys(Keys.TAB)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_5, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when word characters are entered in the initial deposit field
    def test_Case_07(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter word characters
            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(WORD_CHARACTER)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_2, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when special characters are entered in the initial deposit field
    def test_Case_08(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter special characters
            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(SPECIAL_CHARACTERS)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_3, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when numbers with blank spaces are entered in the initial deposit field
    def test_Case_09(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter numbers with space
            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(NUMBERS_WITH_SPACE)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_3, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when the first character entered in the initial deposit field is blank
    def test_Case_10(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter the first character as a blank space
            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(FIRST_CHARACTER_IS_BLANK)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_4, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # For Account type field
    # Test Case when the the savings account type is selected
    def test_Case_11(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Click the savings account
            account_type = driver.find_element(By.NAME, "selaccount")
            account_type.click()
            account_type.click()
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when the the current account type is selected
    def test_Case_12(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Click the current account
            account_type = driver.find_element(By.NAME, "selaccount")
            account_type.click()
            account_type.click()
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # For reset button
    # Test Case the reset button is pressed
    def test_Case_13(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Enter input into all fields
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(SPECIAL_CHARACTERS)
            time.sleep(2)

            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(VALID_INPUT)
            time.sleep(2)
 
            # Click the reset button
            reset_button = driver.find_element(By.NAME, "reset")
            reset_button.click()
            time.sleep(2)
 
            # Check whether the fields are blank after clicking the reset button         
            self.assertEqual(BLANK, customer_id.text)
            self.assertEqual(BLANK, initial_deposit.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # For submit button
    # Test Case an incorrect customer id is entred
    def test_Case_14(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Enter input into all fields
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(INVALID_INPUT)
            time.sleep(2)

            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(VALID_INPUT)
            time.sleep(2)
 
            # Click the submit button
            submit_button = driver.find_element(By.NAME, "button2")
            submit_button.click()
            time.sleep(2)

            # Check whether the actual message on the alert is equal to the expected message
            alert = driver.switch_to.alert
            self.assertEqual(ERROR_MESSAGE_6, alert.text)
            alert.accept()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when a correct customer id is entred
    def test_Case_15(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Enter input into all fields
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_INPUT)
            time.sleep(2)

            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(EXISTING_DEPOSIT)
            time.sleep(2)
 
            # Click the submit button
            submit_button = driver.find_element(By.NAME, "button2")
            submit_button.click()
            time.sleep(2)

            # Check whether the actual message is equal to the expected message
            success_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/p[1]")
            self.assertEqual(SUCCESS_MESSAGE, success_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Clicking on continue on the next page
    def test_Case_16(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Enter input into all fields
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_INPUT)
            time.sleep(2)

            initial_deposit = driver.find_element(By.NAME, "inideposit")
            initial_deposit.send_keys(EXISTING_DEPOSIT)
            time.sleep(2)
 
            # Click the submit button
            submit_button = driver.find_element(By.NAME, "button2")
            submit_button.click()
            time.sleep(2)

            # Next page
            continue_link = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[1]/a[1]")
            continue_link.click()
            time.sleep(2)

            # Home page
            manager_id = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[1]")
            self.assertEqual(MANAGER_ID, manager_id.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Create a teardown method for the class
    @classmethod
    def tearDownClass(cls) :
        try:
            cls.driver.quit()

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

# Used to execute the code
if __name__== "__main__":
    unittest.main()