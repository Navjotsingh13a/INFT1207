# Author: Edwinah Lynn Ninsiima
# Date: 13/08/2024
# Description: Testing the manager module functions on a banking website to see if the website is working well
# Module: Edit Customer

# Import all the important functions
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  WebDriverException
import time 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Declare the URL that will be used
URL = "https://demo.guru99.com/V4/manager/CustomisedStatementInput.php"
LOGIN_URL = "https://demo.guru99.com/V4/"

# Declare the login details
USER_ID = "mngr582991"
PASSWORD = "AtUmujE"

# Declare the input to be entered in the text box fields
BLANK = ""
WORD_CHARACTER = "123Tea"
SPECIAL_CHARACTERS = "@#$"
NUMBERS_WITH_SPACE = "12 456"
FIRST_CHARACTER_IS_SPACE = " ETY"
ACCOUNT_NUMBER = "136424"
FROM_DATE = "2023-05-23"
TO_DATE = "2023-07-23"
MINIMUM_TRANSACTION = "1"
NUMBER_OF_TRANSACTIONS = "4"

# Declare the expected messages
EXPECTED_MESSAGE = "Account Number must not be blank"
EXPECTED_MESSAGE_1 = "Characters are not allowed"
EXPECTED_MESSAGE_2 = "Special characters are not allowed"
EXPECTED_MESSAGE_3 = "First Character cannot have space"
EXPECTED_MESSAGE_4 = "From Date Field must not be blank"
EXPECTED_MESSAGE_5 = "To Date Field must not be blank"
EXPECTED_MESSAGE_6 = "Please fill all fields"
EXPECTED_MESSAGE_7 = "Number of Transaction cannot have special character"

# Create the class for the test cases
class CustomizedStatement(unittest.TestCase):

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
        # Create a try and catch block
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

            # Find and click on the customize statement module
            customized_statement_tab = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/ul[1]/li[14]/a[1]")
            customized_statement_tab.click()
            time.sleep(1)
        
        # Catch any errors
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test for account number field
    # Test case when the input is empty in the name field
    def test_Case_01(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the blank space
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(BLANK)
            account_number.send_keys(Keys.TAB)
            time.sleep(2)
            
            # Assert the expected message and actual message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when non numeric characters are entered in the account number field.
    def test_Case_02(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter word characters
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(WORD_CHARACTER)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when special characters are entered in the account number field
    def test_Case_03(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter special characters
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(SPECIAL_CHARACTERS)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when there is space between the numbers entered in the  account number field
    def test_Case_04(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter numbers with space
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(NUMBERS_WITH_SPACE)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")


    # Test case when the the first character entered in the account number field is blank
    def test_Case_05(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a blank space as the first character
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(FIRST_CHARACTER_IS_SPACE)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test for date field
    # Test case when the input is empty in the from date field
    def test_Case_06(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter blank input
            from_date = driver.find_element(By.NAME, "fdate")
            from_date.click()
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[7]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_4, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when the input is empty in the to date field
    def test_Case_07(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter blank input
            to_date = driver.find_element(By.NAME, "tdate")
            to_date.click()
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_5, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Minimum transaction value
    # Test case when non numeric characters are entered in the minimum transaction field
    def test_Case_08(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter word characters
            minimum_transaction = driver.find_element(By.NAME, "amountlowerlimit")
            minimum_transaction.send_keys(WORD_CHARACTER)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when special characters are entered in the minimum transaction field
    def test_Case_09(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter special characters
            minimum_transaction = driver.find_element(By.NAME, "amountlowerlimit")
            minimum_transaction.send_keys(SPECIAL_CHARACTERS)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when the numeric values entered in the minimum transaction field have space between them
    def test_Case_10(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter numbers with spaces in between
            minimum_transaction = driver.find_element(By.NAME, "amountlowerlimit")
            minimum_transaction.send_keys(NUMBERS_WITH_SPACE)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self .assertEqual(EXPECTED_MESSAGE_1, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when the first character entered in the minimum transaction field is blank
    def test_Case_11(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the first character as a blank space
            minimum_transaction = driver.find_element(By.NAME, "amountlowerlimit")
            minimum_transaction.send_keys(FIRST_CHARACTER_IS_SPACE)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
            
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For number of transactions field
    # Test case when a non numeric character is entered in the numnber of transactions field
    def test_Case_12(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter word characters
            number_of_transaction = driver.find_element(By.NAME, "numtransaction")
            number_of_transaction.send_keys(WORD_CHARACTER)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when special characters are entered in the numnber of transactions field
    def test_Case_13(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter special characters
            number_of_transaction = driver.find_element(By.NAME, "numtransaction")
            number_of_transaction.send_keys(SPECIAL_CHARACTERS)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_7, actual_message.text)
            
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when there is blank space between the numbers entered in the numnber of transactions field
    def test_Case_14(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter numbers with space
            number_of_transaction = driver.find_element(By.NAME, "numtransaction")
            number_of_transaction.send_keys(NUMBERS_WITH_SPACE)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)
            
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when the first character entered in the numnber of transactions field is blank
    def test_Case_15(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the firs character as a blank space
            number_of_transaction = driver.find_element(By.NAME, "numtransaction")
            number_of_transaction.send_keys(FIRST_CHARACTER_IS_SPACE)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
           
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Rest button
    def test_Case_16(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Enter input into all fields
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(ACCOUNT_NUMBER)

            from_date = driver.find_element(By.NAME, "fdate")
            from_date.send_keys(FROM_DATE)

            to_date = driver.find_element(By.NAME, "tdate")
            to_date.send_keys(TO_DATE)

            minimum_transaction = driver.find_element(By.NAME, "amountlowerlimit")
            minimum_transaction.send_keys(MINIMUM_TRANSACTION)

            number_of_transaction = driver.find_element(By.NAME, "numtransaction")
            number_of_transaction.send_keys(NUMBER_OF_TRANSACTIONS)
            
            # Click the reset Button
            reset_button = driver.find_element(By.NAME, "res")
            reset_button.click()
            time.sleep(2)

            # Check if the fields are empty
            self.assertEqual(BLANK,account_number.text)
            self.assertEqual(BLANK,from_date.text)
            self.assertEqual(BLANK,to_date.text)
            self.assertEqual(BLANK,minimum_transaction.text)
            self.assertEqual(BLANK,number_of_transaction.text)
            time.sleep(2)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    def test_Case_17(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Enter input into all fields
            account_number = driver.find_element(By.NAME, "accountno")
            account_number.send_keys(ACCOUNT_NUMBER)

            from_date = driver.find_element(By.NAME, "fdate")
            from_date.send_keys(FROM_DATE)

            to_date = driver.find_element(By.NAME, "tdate")
            to_date.click()

            minimum_transaction = driver.find_element(By.NAME, "amountlowerlimit")
            minimum_transaction.send_keys(MINIMUM_TRANSACTION)

            number_of_transaction = driver.find_element(By.NAME, "numtransaction")
            number_of_transaction.send_keys(NUMBER_OF_TRANSACTIONS)
            
            # Submit Button
            submit_button = driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            time.sleep(2)

            # Error message
            actual_message = driver.find_element(By.XPATH,"/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_6, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

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
