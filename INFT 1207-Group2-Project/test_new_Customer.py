# Author: Edwinah Lynn Ninsiima
# Date: 13/08/2024
# Description: Testing the manager module functions on a banking website to see if the website is working well
# Module: New Customer

# Import all the important functions
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  WebDriverException
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Declare the URL thst will be used
URL = "https://demo.guru99.com/V4/manager/addcustomerpage.php"
LOGIN_URL = "https://demo.guru99.com/V4/"

# Declare the login details
USER_ID = "mngr582991"
PASSWORD = "AtUmujE"

# Declare the input to be entered in the text box fields
BLANK = ""
NUMBER = "1234"
SPECIAL_CHARACTERS = "@#!"
FIRST_BLANK_CHARACTER = " T" 
FIRST_BLANK_CHARACTER_ADDRESS = " ninsiimaedwinah@gmail.com"
CHARACTER = "petr"
LESS_THAN_6_DIGITS = "5736"
SPACE_BETWEEN_NUMBERS = "23 567"
INVALID_EMAIL_FORMAT = "guru99@gmail"
SPACE_IN_EMAIL = "gumball @gmail"

# Declare the expected messages
EXPECTED_MESSAGE_FOR_SPECIAL_CHARACTERS = "Special characters are not allowed"
EXPECTED_MESSAGE = "Customer name must not be blank"
EXPECTED_MESSAGE_2 = "Numbers are not allowed"
EXPECTED_MESSAGE_3 = "First character can not have space"
EXPECTED_MESSAGE_4 = "ADDRESS Field must not be blank"
EXPECTED_MESSAGE_5 = "City Field must not be blank"
EXPECTED_MESSAGE_6 = "Numbers are not allowed"
EXPECTED_MESSAGE_7 = "Special characters are not allowed"
EXPECTED_MESSAGE_8 = "State must not be blank"
EXPECTED_MESSAGE_9 = "Characters are not allowed"
EXPECTED_MESSAGE_10 = "PIN Code must not be blank"
EXPECTED_MESSAGE_11 = "PIN Code must have 6 Digits"
EXPECTED_MESSAGE_12 = "Mobile no must not be blank"
EXPECTED_MESSAGE_13 = "Email-ID must not be blank"
EXPECTED_MESSAGE_14 = "Email-ID is not valid"
EXPECTED_MESSAGE_15 = "Password must not be blank"

# Create the class for the test cases
class TestNewCustomer(unittest.TestCase):

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

            # Find and click on the new customer module
            new_customer_tab = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/ul[1]/li[2]/a[1]")
            new_customer_tab.click()
            time.sleep(1)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when the input is blank in the name field
    def test_Case_01(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter the blank space
            first_name = driver.find_element(By.NAME, "name")
            first_name.send_keys(BLANK)
            first_name.send_keys(Keys.TAB)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            error_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")))
            self.assertEqual(EXPECTED_MESSAGE, error_message.text)
            time.sleep(2)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")


    # Test case when a number is entered in the name field
    def test_Case_02(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter numbers
            first_name = driver.find_element(By.NAME, "name")
            first_name.send_keys(NUMBER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            number_error_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, number_error_message.text)
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when special characters are entred in the name field
    def test_Case_03(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and special characters
            customer_name = driver.find_element(By.NAME, "name")
            customer_name.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_FOR_SPECIAL_CHARACTERS, actual_message.text)
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when first character is blank in  the name field
    def test_Case_04(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and a blank space as the first character
            customer_name = driver.find_element(By.NAME, "name")
            customer_name.send_keys(FIRST_BLANK_CHARACTER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For the address
    # Test case when input is blank in the address field
    def test_Case_05(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter blank input
            address_field = driver.find_element(By.NAME, "addr")
            address_field.send_keys(BLANK)
            address_field.send_keys(Keys.TAB)
        
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[7]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_4, actual_message.text)
            time.sleep(1)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")


    #Test case when first charecter is blank in the address in field
    def test_Case_06(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and the first character as a blank space
            address_field = driver.find_element(By.NAME, "addr")
            address_field.send_keys(FIRST_BLANK_CHARACTER_ADDRESS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[7]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For the City field
    # Test case when blank input is entered in the city field
    def test_Case_07(self):
            
        try:
            driver = self.driver
            driver.get(URL)

            # Find the input box and enter blank input
            city = driver.find_element(By.NAME, "city")
            city.send_keys(BLANK)
            city.send_keys(Keys.TAB)

            # Check whether the actual message is equal to the expected message
            actual_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")))
            self.assertEqual(EXPECTED_MESSAGE_5, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when numeric value is entered in the city field
    def test_Case_08(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter numbers
            city = driver.find_element(By.NAME, "city")
            city.send_keys(NUMBER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")
    
    # Test case when special characters are entered in the city field
    def test_Case_09(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter special characters
            city = driver.find_element(By.NAME, "city")
            city.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_FOR_SPECIAL_CHARACTERS, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when numeric value is entered in the city field
    def test_Case_10(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter numbers
            city = driver.find_element(By.NAME, "city")
            city.send_keys(NUMBER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For the state
    # Test case when input is blank in the state field        
    def test_Case_11(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter blank input
            state = driver.find_element(By.NAME, "state")
            state.send_keys(BLANK)
            state.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_8, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when input is a numeric value in the state field
    def test_Case_12(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter numbers
            state = driver.find_element(By.NAME, "state")
            state.send_keys(NUMBER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")
    
    # Test case when input are special characters in the state field
    def test_Case_13(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter special characters
            state = driver.find_element(By.NAME, "state")
            state.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_7, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")
    
    # Test case when first character is a blank space  in the state field
    def test_Case_14(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter the first character as a blank space
            state = driver.find_element(By.NAME, "state")
            state.send_keys(FIRST_BLANK_CHARACTER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For Pin field
    # Test case when character in the pin field
    def test_Case_15(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter word characters
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.send_keys(CHARACTER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_9, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when empty input is entered in the  pin field
    def test_Case_16(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter blank input
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.send_keys(BLANK)
            pin_field.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_10, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when more than 6 digits are entered in the pin field
    def test_Case_17(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter numebrs that are less than 6 in total
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.send_keys(LESS_THAN_6_DIGITS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_11, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when special characters are entered in the pin field
    def test_Case_18(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter special characters            
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_7, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when first character in the pin field is a blank space
    def test_Case_19(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter a blank space as the first character
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.send_keys(FIRST_BLANK_CHARACTER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when blank space is included between numbers in the pin field
    def test_Case_20(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter numbers with space in between
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.send_keys(SPACE_BETWEEN_NUMBERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_9, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For Mobile Number field
    # Test case when empty input is entered  in the mobile number field
    def test_Case_21(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter blank input
            mobile_number = driver.find_element(By.NAME, "telephoneno")
            mobile_number.send_keys(BLANK)
            mobile_number.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_12, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when the first character entered  is blank in the mobile number field
    def test_Case_22(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter a blank space as the first character
            mobile_number = driver.find_element(By.NAME, "telephoneno")
            mobile_number.send_keys(FIRST_BLANK_CHARACTER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when there is space between the numbers entered in the mobile number field
    def test_Case_23(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter numbers with spaces in between
            mobile_number = driver.find_element(By.NAME, "telephoneno")
            mobile_number.send_keys(SPACE_BETWEEN_NUMBERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_9, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when special characters are entered in the mobile number field
    def test_Case_24(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter special characters
            mobile_number = driver.find_element(By.NAME, "telephoneno")
            mobile_number.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_7, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For Email field
    # Test case when value entered is blank in the email field
    def test_Case_25(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter blank input
            email = driver.find_element(By.NAME, "emailid")
            email.send_keys(BLANK)
            email.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[12]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_13, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when value is an invalid format is entered in the email fieled
    def test_Case_26(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter an invalid email format
            email = driver.find_element(By.NAME, "emailid")
            email.send_keys(INVALID_EMAIL_FORMAT)
            email.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[12]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_14, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test case when a space character is entered in the email fieled
    def test_Case_27(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter an email with spaces in between
            email = driver.find_element(By.NAME, "emailid")
            email.send_keys(SPACE_IN_EMAIL)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[12]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_14, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For password field
    # Test case when value entered is blank in the password field
    def test_Case_28(self):
            
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(1)

            # Find the input box and enter blank input
            password = driver.find_element(By.NAME, "password")
            password.send_keys(BLANK)
            password.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[13]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_15, actual_message.text)
        
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
