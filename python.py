# problematic_code.py

# This module lacks a docstring and will trigger an error in pylint for missing module docstring

def example_function():
    pass  # This function lacks a docstring and will trigger a warning in pylint

def another_function(param1, param2):
    # Function with an overly long line and no docstring
    result = param1 + param2  # This line of code is intentionally long to exceed the default line length limit in pylint and trigger a warning
    return result

bad_variable = 42  # This variable is declared but never used, which will trigger a warning

def function_with_long_line():
    # This line is intentionally long to trigger a warning for line length
    print("This line is so long that it will definitely exceed the default maximum line length set by pylint and should cause a line-too-long warning")

class BadClass:
    def __init__(self):
        self.value = 10
    
    def method_without_docstring(self, arg):
        # Method lacks docstring and will trigger a warning
        return arg * self.value

    def method_with_long_line(self):
        # Function with a line that is longer than the allowed limit
        return "This method contains a very long line that is intended to exceed the maximum line length allowed by pylint, which should trigger a line-too-long warning"