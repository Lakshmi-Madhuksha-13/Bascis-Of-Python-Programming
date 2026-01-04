# numbers - int, float, complex
x = 1
x = 1.1
x = 1 + 2j # a + bi
#arithmetic operations
print(10 + 3) # addition
print(10 - 3) # subtraction 
print(10 * 3) # multiplication
print(10 / 3) # division (float)    
print(10 // 3) # floor division
print(10 % 3) # modulus 
print(10 ** 3) # exponentiation 
# operator precedence
print(10 + 3 * 2) # multiplication first
print((10 + 3) * 2) # parentheses first
# augmented assignment
x = 10  
x += 3  # x = x + 3
x *= 2  # x = x * 2
x -= 5  # x = x - 5
x /= 4  # x = x / 4
x **= 3 # x = x ** 3
print(x)
# built-in functions
print(abs(-10))  # absolute value
print(round(3.6)) # round to nearest integer
print(round(3.4)) # round to nearest integer    
print(pow(2, 3)) # exponentiation
print(max(1, 5, 3)) # maximum value
print(min(1, 5, 3)) # minimum value
print(int(3.7)) # convert to integer
print(float(5)) # convert to float
print(complex(2, 3)) # convert to complex number
# math module
import math 
print(math.sqrt(16)) # square root
print(math.ceil(3.2)) # ceiling
print(math.floor(3.8)) # floor
print(math.factorial(5)) # factorial    
print(math.gcd(12, 15)) # greatest common divisor
print(math.sin(math.pi / 2)) # sine
print(math.cos(0)) # cosine
print(math.log(100, 10)) # logarithm base 10
print(math.exp(2)) # exponential e^2
print(math.radians(180)) # degrees to radians
print(math.degrees(math.pi)) # radians to degrees   
# random module
import random
print(random.randint(1, 10)) # random integer between 1 and 10
print(random.uniform(1.0, 10.0)) # random float between 1
print(random.choice(['apple', 'banana', 'cherry'])) # random choice from list
print(random.shuffle([1, 2, 3, 4, 5])) # shuffle list in place
print(random.sample([1, 2, 3, 4, 5], 3)) # random sample of 3 elements from list
# constants
print(math.pi) # value of pi
print(math.e)  # value of e
print(math.tau) # value of tau (2 * pi)
print(math.inf) # infinity
print(math.nan) # not a number

