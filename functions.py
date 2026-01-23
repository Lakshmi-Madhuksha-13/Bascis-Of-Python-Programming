# functions in python - A function is a block of reusable code that is used to perform a specific task.
# Functions help to break our program into smaller and modular chunks.
# This makes the code more organized, manageable, and reusable.
#there are two types of functions in python:
#1. Built-in functions - print(), input(), len(), type(), etc.
#2. User-defined functions
# Syntax of user-defined functions:
# def function_name(parameters):    
#     """docstring"""
#     statement(s)
# Example of a user-defined function:
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}! Welcome to the world of Python functions.")
# Calling the function
greet("Alice")  
# Output: Hello, Alice! Welcome to the world of Python functions.
# Function with return statement
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b
# Calling the function and storing the result
result = add(5, 3)
print(f"The sum is: {result}")
# Output: The sum is: 8
# Function with default parameters
def power(base, exponent=2):
    """This function returns the power of a number."""
    return base ** exponent 
# Calling the function with and without the default parameter
print(power(4))        # Output: 16 (4^2)
print(power(4, 3))     # Output: 64 (4^3)
# Function with variable-length arguments
def multiply(*args):
    """This function returns the product of all the numbers passed as arguments."""
    product = 1
    for num in args:
        product *= num
    return product  
# Calling the function with different number of arguments
print(multiply(2, 3))          # Output: 6
print(multiply(2, 3, 4))       # Output: 24
print(multiply(2, 3, 4, 5))    # Output:120
# Function with keyword arguments
def introduce(**kwargs):    
    """This function introduces a person using keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")                
# Calling the function with keyword arguments
introduce(name="Bob", age=30, city="New York")
# Output:
# name: Bob
# age: 30   
# city: New York
# Lambda function (anonymous function)
square = lambda x: x ** 2
# Calling the lambda function
print(f"The square of 5 is: {square(5)}")
# Output: The square of 5 is: 25
# Function documentation
print(greet.__doc__)    
# Output: This function greets the person passed in as a parameter.
print(add.__doc__)
# Output: This function returns the sum of two numbers.
# Function annotations
def divide(a: float, b: float) -> float:
    """This function returns the division of two numbers."""
    return a / b
# Calling the function
result = divide(10, 2)
print(f"The division result is: {result}")
# Output: The division result is: 5.0
print(divide.__annotations__)
# Output: {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
# Recursive function
def factorial(n):
    """This function returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Calling the recursive function
print(f"The factorial of 5 is: {factorial(5)}")
# Output: The factorial of 5 is: 120
# Nested function
def outer_function(text):
    """This function contains a nested function."""
    def inner_function():
        """This is the inner function."""
        print(text)
    inner_function()
# Calling the outer function
outer_function("Hello from the nested function!")
# Output: Hello from the nested function!   
# Function scope
x = 10  # Global variable
def function_scope():
    """This function demonstrates variable scope."""
    x = 5  # Local variable
    print(f"Local x: {x}")
    print(f"Global x: {globals()['x']}")
# Calling the function  
function_scope()
# Output:
# Local x: 5
# Global x: 10
# Using global keyword
def modify_global():
    """This function modifies the global variable."""
    global x
    x = 20
    print(f"Modified global x: {x}")
modify_global()
print(f"Global x after modification: {x}")
# Output:   
# Modified global x: 20
# Global x after modification: 20
# Using nonlocal keyword
def outer():
    """This function demonstrates the use of nonlocal keyword."""
    y = 10
    def inner():
        nonlocal y
        y = 20
        print(f"Inner y: {y}")
    inner()
    print(f"Outer y: {y}")
outer()
# Output:   
# Inner y: 20
# Outer y: 20
# Function to demonstrate docstring and help()
def sample_function():
    """This is a sample function to demonstrate docstring and help()."""
    pass    
# Using help() to display the docstring
help(sample_function)
# Output:
# Help on function sample_function in module __main__:  
# sample_function()
#     This is a sample function to demonstrate docstring and help().        

# Function with type hints
def concatenate_strings(a: str, b: str) -> str:  
    """This function concatenates two strings."""
    return a + b
# Calling the function
result = concatenate_strings("Hello, ", "World!")
print(result)
# Output: Hello, World!
print(concatenate_strings.__annotations__)
# Output: {'a': <class 'str'>, 'b': <class 'str
#>, 'return': <class 'str'>}
# Function with exception handling
def safe_divide(a, b):
    """This function safely divides two numbers and handles division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
# Calling the function
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed.    
# Function with docstring examples
def multiply_by_two(n):
    """This function multiplies the input number by two.
    
    Examples:
    >>> multiply_by_two(3)
    6
    >>> multiply_by_two(-1)
    -2
    >>> multiply_by_two(0)
    0
    """
    return n * 2
# Using doctest to test the examples in the docstring
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Calling the function
    print(multiply_by_two(4))  # Output: 8  
