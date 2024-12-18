# Name: Navjot Singh
# Date: June 13, 2024
# Modified: June 13, 2024
# Description: Unit Test for the 'find_minimum' program in the "app" file.


import unittest
from app import find_minimum

class TestFindMinimumFunction(unittest.TestCase):
    # Set method runs before the each test case.
    def setUp(self):
        print("Set up things...")

    # Set method runs after the each test case.
    def tearDown(self):
        print("Tearing down...")

    # Test Case 1: A very short list (of inputs) with the size of 1, 2, or 3 elements.
    def test_short_list(self):
        expected_result = 1
        result = find_minimum([1, 2, 3])
        self.assertEqual(result, expected_result)

    # Test Case 2: An empty list i.e., of size 0.
    def test_empty_list(self):
        expected_result = None
        result = find_minimum([])
        self.assertIsNone(result, expected_result)

    # Test Case 3: A list where the minimum element is the first or last element.
    def test_first_last_minimum(self):
        expected_result = 1
        result = find_minimum([3, 2, 1])
        self.assertEqual(result, expected_result)
        

    # Test Case 4: A list where the minimum element is negative.   
    def test_negative_minimum(self):
        expected_result = -1
        result = find_minimum([3, 2, -1, 5])
        self.assertEqual(result, expected_result)

    # Test Case 5: A list where all elements are negative.
    def test_all_negative(self):
        expected_result = -5
        result = find_minimum([-3,-2, -1, -5])    
        self.assertEqual(result, expected_result)

    # Test Case 6: A list where some elements are real numbers.
    def test_real_numbers(self):
        expected_result = 1.2
        result = find_minimum([3.5, 2.1, 1.2, 5.3])
        self.assertEqual(result, expected_result)

    # Test Case 7: A list where some elements are alphabetic characters and special characters.
    def test_alphabetic_special_characters(self):
        expected_result = None
        result = find_minimum(['a', 'b', 'c', '1', '2', '$'])
        self.assertIsNot(result, expected_result)

    # Test Case 8: A list with duplicate elements.
    def test_duplicate_elements(self):
        expected_result = 2
        result = find_minimum([3, 2, 2, 5, 3])
        self.assertEqual(result, expected_result)

    # Test Case 9: A list where one element has a value greater than the maximum permissible limit of an integer.
    def test_large_element(self):
        expected_result = 2
        result = find_minimum([3, 2, 2145678, 5])
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()