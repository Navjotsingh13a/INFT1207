# Name: Navjot Singh and Sartaj Singh
# Date: June 22, 2024.
# Modified: June 22, 2024.
# Description: This program allows user to run the "unittest" test cases
# Based on the users input.


# The approximate value of pie.
pie = 22/7

# A function to calculate the area of circle based on the provided radius.
def test_area_circle(radius):
    return pie * radius * radius

# A function to calculate the area of trapezium based on the provided length(a), breadth(b), and height(h).
def test_area_trapezium(a, b, height):
    return 0.5 * (a + b) * height

# A function to calculate the area of ellipse based on the provided major and minor axis.
def test_area_ellipse(a, b):
    return pie * a * b

# A function to calculate the area of rhombus based on the length of one digonal(d1) and other diagonal(d2).
def test_area_rhombus(d1, d2):
    return 0.5 * d1 * d2