# Author: Malaekah Khan
# Date: 13/08/2024
# Description: Testing the manager module functions on a banking website to see if the website is working well
# Module: Delete Customer

# Import all the important functions
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

# Declare the URL thst will be used
URL = "https://demo.guru99.com/V4/manager/DeleteCustomerInput.php"
LOGIN_URL = "https://demo.guru99.com/V4/"

# Declare the login details
USER_ID = "mngr582991"
PASSWORD = "AtUmujE"

# Declare the expected messages
ERROR_MESSAGE = "Customer ID is required"
ERROR_MESSAGE_1 = "Characters are not allowed"
ERROR_MESSAGE_2 = "Special characters are not allowed"
ERROR_MESSAGE_3 = "First character can not have space"
ERROR_MESSAGE_4 = "Customer does not exist!!"
ERROR_MESSAGE_5 = "Customer could not be deleted!!. First delete all accounts of this customer then delete the customer"

# Declare the input to be entered in the text box fields
BLANK = ""
VALID_CUSTOMER_ID = "583541"
WORD_CHARACTER = "WER"
SPECIAL_CHAR_CUSTOMER_ID = "583541!@#$"
CUSTOMER_ID_WITH_SPACES = "583 541"
LEADING_SPACE_CUSTOMER_ID = " 583541"
TRAILING_SPACE_CUSTOMER_ID = "583541 "
NON_EXISTENT_CUSTOMER_ID = "99999"
CORRECT_CUSTOMER_ID = "64772"

# Create the class for the test cases
class DeleteCustomerTest(unittest.TestCase):
    
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

            # Find and click on the delete customer module
            delete_customer_tab = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/ul[1]/li[4]/a[1]")
            delete_customer_tab.click()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when blank input is entered in the Customer id field
    def test_Case_01(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)
 
            # Find the input box and enter the blank space
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(BLANK)
            customer_id.send_keys(Keys.TAB)
            time.sleep(2)

            # Assert the expected message and actual message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE, error_message.text)
            time.sleep(2)
 
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when word characters are entered in the Customer id field
    def test_Case_02(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the word characters
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(WORD_CHARACTER)
            time.sleep(2)

            # Assert the expected message and actual message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_1, error_message.text)
            time.sleep(2)
            
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when special characters are entered in the Customer id field
    def test_Case_03(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter special characters
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(SPECIAL_CHAR_CUSTOMER_ID)
            customer_id.send_keys(Keys.TAB)
            time.sleep(2)

            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_2, error_message.text)
            time.sleep(2)
            
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when numbers with spaces entered in the Customer id field
    def test_Case_04(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter an id with spaces
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(CUSTOMER_ID_WITH_SPACES)
            customer_id.send_keys(Keys.TAB)
            time.sleep(2)

            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_1, error_message.text)
            time.sleep(2)

        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when the first charater entered is a blank space in the Customer id field
    def test_Case_05(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the first character as a blank space
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(LEADING_SPACE_CUSTOMER_ID)
            customer_id.send_keys(Keys.TAB)
            time.sleep(2)

            # Check whether the actual message is equal to the expected message
            error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]")
            self.assertEqual(ERROR_MESSAGE_3, error_message.text)
            time.sleep(2)
            
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when incorrect customer id is entered in the Customer id field
    def test_Case_06(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a non existent customer id
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(NON_EXISTENT_CUSTOMER_ID)
            time.sleep(1)

            # Click the submit button
            submit_button = driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            time.sleep(1)

            # Accept the first alert
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)

            # Check whether the actual message on the alert matches the expected messsage
            alert_2 = driver.switch_to.alert
            time.sleep(1)
            self.assertEqual(ERROR_MESSAGE_4, alert_2.text)
            alert.accept()

            
        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Test Case when correct customer id is entered in the Customer id field
    def test_Case_07(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a correct customer id
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(CORRECT_CUSTOMER_ID)
            time.sleep(2)

            # Submit button
            submit_button = driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            time.sleep(1)

            # Click the firs alert
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)

            # Check whether the actual message on the alert matches the expected messsage
            alert_2 = driver.switch_to.alert
            self.assertEqual(ERROR_MESSAGE_5, alert_2.text)
            alert.accept()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occurred: {e}")

    # Reset button
    def test_Case_08(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter a valid customer id
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)

            # Click the reset button
            reset_button = driver.find_element(By.NAME, "res")
            reset_button.click()
            time.sleep(1)

            # Check whether the customer id field is empty after the reset button is clicked
            self.assertEqual(customer_id.text, BLANK)
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
