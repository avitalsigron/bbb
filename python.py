# Example of problematic Python code

# This is a sample Python script that is intentionally written to trigger pylint errors

def example_function():
    pass  # This function does nothing and will trigger a warning for missing function docstring

# A missing module docstring warning
print("Hello, World!")  # This line will trigger a warning for having a print statement without proper context

# This variable is declared but never used
unused_variable = 42

def another_function(param1, param2):
    # The function is missing a docstring and has a line that exceeds the recommended length
    result = param1 + param2  # This line has a comment that is too long and will trigger a warning for too long line
    return result

