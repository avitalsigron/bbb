import math

def calc_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius ** 2

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b
def print_result(result):
    """Print the result in a formatted way."""
    print(f"The result is: {result}")

def main():
    """Main function to demonstrate usage."""
    radius = 10
    area = calc_area(radius)
    print_result(area)

    number1 = 5
    number2 = 3
    sum_result = add_numbers(number1, number2)
    print_result(sum_result)

if __name__ == "__main__":
    main()
