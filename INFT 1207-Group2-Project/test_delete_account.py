# Author: Malaekah Khan
# Date: 13/08/2024
# Description: Testing the manager module functions on a banking website to see if the website is working well
# Module: Delete account

# Import all the important functions
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

# Declare the URL thst will be used
URL = "https://demo.guru99.com/V4/manager/deleteAccountInput.php"
LOGIN_URL = "https://demo.guru99.com/V4/"

# Declare the login details
USER_ID = "mngr582991"
PASSWORD = "AtUmujE"

# Declare the input to be entered in the text box fields
BLANK = ""
WORD_CHARACTERS = "seven"
SPECIAL_CHARACTERS = "@#"
NUMBERS_WITH_SPACES = "23 456"
FIRST_CHARACTER_IS_BLANK = " "
VALID_INPUT = "136424"
INVALID_INPUT = "000000000"

# Declare the expected messages
ERROR_MESSAGE = "Account Number must not be blank"
ERROR_MESSAGE_2 = "Characters are not allowed"
ERROR_MESSAGE_3 = "Special characters are not allowed"
ERROR_MESSAGE_4 = "First character cannot have space"
ERROR_MESSAGE_5 = "Account deleted successfully"
ERROR_MESSAGE_6 = "Account does not exist"

# Create the class for the test cases
class DeleteAccountTest(unittest.TestCase):

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

            # Find and click on the delete account module
            delete_account_tab = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/ul[1]/li[7]/a[1]")
            delete_account_tab.click()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For Account number field
    # Test Case when blank input is entered in the account number field
    def test_Case_01(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter a blank input
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(BLANK)
            account_number.send_keys(Keys.TAB)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when word characters are entered in the account number field
    def test_Case_02(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter a word characters
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(WORD_CHARACTERS)
            account_number.send_keys(Keys.TAB)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_2, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when special characters are entered in the account number field
    def test_Case_03(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter a special characters
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(SPECIAL_CHARACTERS)
            account_number.send_keys(Keys.TAB)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_3, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when numbers with spaces are entered in the account number field
    def test_Case_04(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter blank input
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(NUMBERS_WITH_SPACES)
            account_number.send_keys(Keys.TAB)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_2, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when the first character entered in the account number field is blank
    def test_Case_05(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter the first character as a blank space
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(FIRST_CHARACTER_IS_BLANK)
            time.sleep(2)
 
            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_4, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # For Submit button
    # Test Case when the valid input entered in the account number field is blank
    def test_Case_06(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter a valid input
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(VALID_INPUT)
            time.sleep(1)

            # Submit Button
            submit_button = driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            time.sleep(1)

            # Check whether the actual message on the alert is equal to the expected message
            alert = driver.switch_to.alert
            time.sleep(1)
            self.assertEqual(ERROR_MESSAGE_5, alert.text)
            time.sleep(1)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when the invalid input entered in the account number field is blank
    def test_Case_07(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter a invalid input
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(INVALID_INPUT)
            time.sleep(1)

            # Submit Button
            submit_button = driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            time.sleep(1)

            # Accept the first alert
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)

            # Check whether the actual message on the second alert is equal to the expected message
            alert_2 = driver.switch_to.alert
            self.assertEqual(ERROR_MESSAGE_6, alert_2.text)
            alert_2.accept()
            time.sleep(1)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # For reset button
    # Test Case when the invalid input entered in the account number field is valid
    def test_Case_08(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter any input
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(INVALID_INPUT)
            time.sleep(1)

            # Reset Button
            reset_button = driver.find_element(By.NAME, "res")
            reset_button.click()
            time.sleep(1)

            # Check whether the account number field is empty after the reset button is clicked
            self.assertEqual(BLANK, account_number.text)
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
if __name__ == "__main__":
    unittest.main()

