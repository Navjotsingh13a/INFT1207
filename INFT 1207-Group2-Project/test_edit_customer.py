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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Declare the URL thst will be used
URL = "https://demo.guru99.com/V4/manager/EditCustomer.php"
LOGIN_URL = "https://demo.guru99.com/V4/"

# Declare the login details
USER_ID = "mngr582991"
PASSWORD = "AtUmujE"

# Declare the input to be entered in the text box fields
BLANK = ""
WORD_CHARACTER = "AWERT"
SPECIAL_CHARACTERS = "@#!"
VALID_CUSTOMER_ID = "64772"
NUMBERS = "1234"
LESS_THAN_SIX_DIGITS = "123"
INVALID_EMAIL = "gumball99@gmail"

# Declare the expected messages
EXPECTED_MESSAGE = "Customer ID is required"
EXPECTED_MESSAGE_1 = "Characters are not allowed"
EXPECTED_MESSAGE_2 = "Special characters are not allowed"
EXPECTED_MESSAGE_3 = "Address Field must not be blank"
EXPECTED_MESSAGE_4 = "City Field must not be blank"
EXPECTED_MESSAGE_5 = "Numbers are not allowed"
EXPECTED_MESSAGE_6 = "State must be blank"
EXPECTED_MESSAGE_7 = "PIN Code must not be blank"
EXPECTED_MESSAGE_8 = "PIN Code must have 6 Digits"
EXPECTED_MESSAGE_9 = "Telephone no must not be blank"
EXPECTED_MESSAGE_10 = "Email-ID must not be blank"
EXPECTED_MESSAGE_11 = "Email-ID is not valid"

# Create the class for the test cases
class EditCustomerTest(unittest.TestCase):

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

            # Log in to the website using password and user id
            user_id = driver.find_element(By.NAME, "uid")
            user_id.send_keys(USER_ID)

            password = driver.find_element(By.NAME, "password")
            password.send_keys(PASSWORD)
            time.sleep(1)

            login = driver.find_element(By.NAME, "btnLogin")
            login.click()

            # Find and click on the edit customer module
            edit_customer_tab = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/ul[1]/li[3]/a[1]")
            edit_customer_tab.click()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")
  

    # For Customer id
    # Test Case when the input is blank in the customer id field
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
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")


    # Test Case when the input are word characters in the customer id field
    def test_Case_02(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and word characters
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(WORD_CHARACTER)
            time.sleep(2)
            
            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

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
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when valid input is entered in the customer id field
    def test_Case_04(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            
            # Submit button
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()
            time.sleep(1)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # In the edit page
    # For Address field
    # Test Case when the input entered in the address field is blank
    def test_Case_05(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the address field and enter blank input
            address = driver.find_element(By.NAME, "addr")
            address.clear()
            address.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[7]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_3, actual_message.text)

        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For city field
    # Test Case when blank input is entered in the city field
    def test_Case_06(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the city field and enter blank input
            city = driver.find_element(By.NAME, "city")
            city.send_keys(Keys.TAB)
            city.clear()
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_4, actual_message.text)
            
    
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when nurmeric values are entered in the city field
    def test_Case_07(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the city field and enter numbers
            city= driver.find_element(By.NAME, "city")
            city.clear()
            city.send_keys(NUMBERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_5, actual_message.text)
            
    
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when special characters are entered in the city field
    def test_Case_08(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the city field and enter special characters
            city= driver.find_element(By.NAME, "city")
            city.clear()
            city.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[8]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
            
    
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For State field
    # Test Case when no input is entered in the state field
    def test_Case_09(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the state field and enter blank input
            state = driver.find_element(By.NAME, "state")
            state.clear()
            state.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_6, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when numeric values are entered in the state field
    def test_Case_10(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the state field and enter numbers
            state = driver.find_element(By.NAME, "state")
            state.clear()
            state.send_keys(NUMBERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_5, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when special characters are entered in the state field
    def test_Case_11(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the state field and enter special characters
            state = driver.find_element(By.NAME, "state")
            state.clear()
            state.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[9]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case for PIN field
    # Test Case when word characters are entered in the PIN field
    def test_Case_12(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the state field and enter word characters
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(WORD_CHARACTER)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_1, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")   

    # Test Case when blank input is entered in the PIN field
    def test_Case_13(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the pin field and enter blank input
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(BLANK)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_7, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}") 

    # Test Case when less than 6 digits are entered in the PIN field
    def test_Case_14(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

             # Clear the pin field and enter few numbers
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(LESS_THAN_SIX_DIGITS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_8, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when special characters are entered in the PIN field
    def test_Case_15(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

             # Clear the pin field and enter special characters
            pin_field = driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[10]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For Mobile Number field
    # Test Case when emputy input is entered in the mobile number field
    def test_Case_16(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the mobile number field and enter blank input
            mobile_number = driver.find_element(By.NAME, "telephoneno")
            mobile_number.clear()
            mobile_number.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_9, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # Test Case when special chracters are entered in the mobile number field
    def test_Case_17(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the mobile number field and enter special characters
            mobile_number = driver.find_element(By.NAME, "telephoneno")
            mobile_number.clear()
            mobile_number.send_keys(SPECIAL_CHARACTERS)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[11]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_2, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For Email Field
    # Test Case when empty input is entered in the email field
    def test_Case_18(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the email field and enter blank input
            email = driver.find_element(By.NAME, "emailid")
            email.clear()
            email.send_keys(Keys.TAB)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[12]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_10, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")             

    # Test Case when an invalid email format is entered in the email field
    def test_Case_19(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Clear the email field and enter an invalid email
            email = driver.find_element(By.NAME, "emailid")
            email.clear()
            email.send_keys(INVALID_EMAIL)
            time.sleep(1)

            # Check whether the actual message is equal to the expected message
            actual_message = driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[12]/td[2]/label[1]")
            self.assertEqual(EXPECTED_MESSAGE_11, actual_message.text)
        
        except WebDriverException as e:
            print(f"Web driver exception occured {e}")

    # For submit button
    def test_Case_20(self):
        try:
            driver = self.driver
            driver.get(URL)
            time.sleep(2)

            # Find the input box and enter a valid customer id to go to the next page
            customer_id = driver.find_element(By.NAME, "cusid")
            customer_id.send_keys(VALID_CUSTOMER_ID)
            time.sleep(1)
            button = driver.find_element(By.NAME, "AccSubmit")
            button.click()

            # Press the submit button
            submit_button = driver.find_element(By.NAME, "sub")
            submit_button.click()

            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)
            
            # Fail the test because the changes werent saved
            self.fail("Test failed because the fields changed, remained the same")

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