# input() - is a built-in function in Python that reads a line from input, converts it into a string (stripping a trailing newline), and returns that, it helps to get input from the user.
x = input("x:")
y = x + 1  # This will raise an error because x is a string
print(y)
# To fix the error, we need to convert the input string to an integer
x = int(input("x:"))    
y = x + 1  # Now this works because x is an integer
print(y)
# example 
x = input("x:")    
y = int(x) + 1
print(f"x: {x}, y: {y}")    
# 0,None,Falsy,"",[],() are considered False in Python and remaining values are considered True

# int() - is a built-in function in Python that converts a specified value into an integer number. It can convert strings, floats, and other types to integers.
# float() - is a built-in function in Python that converts a specified value into a floating-point number. It can convert strings, integers, and other types to floats.
# str() - is a built-in function in Python that converts a specified value into a string. It can convert numbers, lists, tuples, and other types to strings.
# Example usage of type conversion functions
a = "10"
b = int(a)  # Convert string to integer
c = float(a)  # Convert string to float
d = str(b)  # Convert integer to string
print(f"a: {a}, b: {b}, c: {c}, d: {d}")
# Example of converting different types
num_str = "25"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_int)  # Convert integer to float
str_from_float = str(num_float)  # Convert float to string
print(f"num_str: {num_str}, num_int: {num_int}, num_float: {num_float}, str_from_float: {str_from_float}")
