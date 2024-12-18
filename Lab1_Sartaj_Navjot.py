# Name: Sartaj Singh, Navjot Singh
# Program Name: Software Testing and Automation
# Date: 22 May 2024
# Modified: 22 May 2024
# Strong password-  Lab1_Group 1
# Description: Program that generate strong password

import random
import string

print("Random Password Generator")

# Variables
password_length = 0
is_valid_length = False
remaining_characters = 0
count_letters = 0
count_digits = 0
count_symbols = 0
total_letters = 0
total_digits = 0
total_symbols = 0

# Password Generator
def generate_password(total_letters, total_digits, total_symbols):
    letter_list = random.choices(string.ascii_letters, k=total_letters)
    digit_list = random.choices(string.digits, k=total_digits)
    symbol_list = random.choices(string.punctuation, k=total_symbols)
    password_list = letter_list + digit_list + symbol_list
    random.shuffle(password_list)
    return ''.join(password_list)

# Validates that a string is an integer
def validate_int(input_str: str):
    if input_str.isnumeric():
        return int(input_str)
    else:
        print("Please enter a positive number")
        return None

# Entering Password Length
while not is_valid_length:
    length_input = input("Enter the length of the password: ")
    password_length = validate_int(length_input)
    if password_length is not None:
        if password_length >= 8:
            is_valid_length = True
        else:
            print("Password must be contain 8 or more characters.")

remaining_characters = password_length

# Asking user for types of letters in password
while remaining_characters > 0:
    is_valid_letters = False
    while not is_valid_letters:
        letters_input = input("Enter the number of letters desired in the password: ")
        count_letters = validate_int(letters_input)
        if count_letters is not None:
            if 0 <= count_letters <= remaining_characters:
                is_valid_letters = True
                total_letters += count_letters
                remaining_characters -= count_letters
            else:
                print(f"The number of letters should be in the range of 0 and {remaining_characters}.")

# Asking user for how many digit they want to be in password.
    if remaining_characters == 0:
        is_valid_digits = True
    else:
        is_valid_digits = False
        while not is_valid_digits:
            digits_input = input("Enter the number of digits desired in the password: ")
            count_digits = validate_int(digits_input)
            if count_digits is not None:
                if 0 <= count_digits <= remaining_characters:
                    total_digits += count_digits
                    remaining_characters -= count_digits
                    is_valid_digits = True
                else:
                    print(f"The number of digits should be in the range of 0 and {remaining_characters}.")

# Asking user for how many special characters they want to be in password.
        if remaining_characters == 0:
            is_valid_symbols = True
        else:
            is_valid_symbols = False
            while not is_valid_symbols:
                symbols_input = input("Enter the number of special characters desired in the password: ")
                count_symbols = validate_int(symbols_input)
                if count_symbols is not None:
                    if 0 <= count_symbols <= remaining_characters:
                        total_symbols += count_symbols
                        remaining_characters -= count_symbols
                        is_valid_symbols = True
                    else:
                        print(f"The number of special characters should be in the range of 0 and {remaining_characters}.")

print(f"Your desired password is: {generate_password(total_letters, total_digits, total_symbols)}.")
