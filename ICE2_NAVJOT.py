# Name: Navjot Singh
# Date: 30 May, 2024
# Modified: 30 May, 2024
# Description: This program finds the smallest number among a list of
# numbers, with handeling non-numeric inputs.


def smallest_number(numbers: list) -> int:
    # if there is only one number, return it
    if len(numbers) == 1: 
        return numbers[0]

    smallest = numbers[0]

    for index in range(len(numbers)):
        if numbers[index] < smallest:
            smallest = numbers[index]
    # return the smallest number
    return smallest

# Prompt the user to enter the list of numbers separated by space.
user_input = input("Enter a set of elements separated by space: ")
list_of_numbers = user_input.split()
valid_numbers = []

# Iterate through each number of the input list
for number in list_of_numbers:
    try:
        valid_numbers.append(int(number))
    except ValueError:
        print("Error Message")
        
# If there are valid numbers in the list, print the smallest one
if valid_numbers:
    smallest = smallest_number(valid_numbers)
    print("The smallest element entered is:", smallest)
else:
    # If there are no valid numbers, print
    print("Invalid Numbers.")