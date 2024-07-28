import math
import sys

def calc_area(radius):
    return math.pi * radius * radius

def add_numbers(a, b):
    return a + b

def print_result(result):
    print("The result is: ", result)

result = calc_area(10)
print_result(result)

# פקודה שאינה בשימוש, עלולה להוביל לבעיה בלינטר
unused_variable = 42

# שגיאת קידוד
def example_function():
    x =  5
    if x > 10:
      print("x is greater than 10")  # בעיית הזחה (indentation)
    else:
        print("x is not greater than 10")

example_function()
