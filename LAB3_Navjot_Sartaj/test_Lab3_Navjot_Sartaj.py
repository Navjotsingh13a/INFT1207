# Name: Navjot Singh and Sartaj Singh
# Date: June 22, 2024.
# Modified: June 22, 2024.
# Description: This program allows user to run the "unittest" test cases
# Based on the users input.

import unittest
from Lab3_Navjot_Sartaj import*

# Define the test case class for area calculations.
class TestCaseCalculations(unittest.TestCase):

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("End of the test: ", self.shortDescription())

    # A function for area of circle.
    def test_area_circle(self):
        # Test cases for test_area_circle function.
        """ Test Area of Circle when radius  >= 0, =< 0"""
        self.assertEqual(test_area_circle(0), 0)
        self.assertEqual(test_area_circle(1), 22/7)
        self.assertEqual(test_area_circle(2), 22/7 * 4)
        self.assertEqual(test_area_circle(3), 22/7 * 9)

    # A function for area of trapezium.
    def test_area_trapezium(self):
        # Test cases for test_area_trapezium function.
        """ Test Area of trapezium when radius  >= 0, =< 0 """
        self.assertEqual(test_area_trapezium(0, 0, 0), 0)
        self.assertEqual(test_area_trapezium(1, 2, 3), 4.5)
        self.assertEqual(test_area_trapezium(2, 2, 2), 4)
        self.assertEqual(test_area_trapezium(3, 1, 4), 8)

    # A function for area of ellipse.
    def test_area_ellipse(self):
        # Test cases for test_area_ellipse function.
        """ Test Area of ellipse when radius >= 0, =< 0 """
        self.assertEqual(test_area_ellipse(0, 0), 0)
        self.assertEqual(test_area_ellipse(1, 2), 22/7 * 1 * 2)
        self.assertEqual(test_area_ellipse(2, 3), 22/7 * 2 * 3)
        self.assertEqual(test_area_ellipse(3, 4), 22/7 * 3 * 4)

    # A function for area of rhombus..
    def test_area_rhombus(self):
        # Test cases for test_area_rhombus function.
        """ Test Area of rhombus when radius >= 0, =< 0 """
        self.assertEqual(test_area_rhombus(0, 0), 0)
        self.assertEqual(test_area_rhombus(1, 2), 1)
        self.assertEqual(test_area_rhombus(2, 3), 3)
        self.assertEqual(test_area_rhombus(3, 4), 6)

if __name__ == '__name__':
    unittest.main()