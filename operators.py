#comparison operators - are the operators that compare two values and return a boolean result based on the comparison.
def equal(a, b):
    return a == b
def not_equal(a, b):
    return a != b
def greater_than(a, b):
    return a > b
def less_than(a, b):
    return a < b
def greater_than_or_equal(a, b):
    return a >= b
def less_than_or_equal(a, b):
    return a <= b
#logical operators - are used to combine multiple boolean expressions and return a boolean result.
def logical_and(a, b):
    return a and b  
def logical_or(a, b):
    return a or b
def logical_not(a):
    return not a
#arithmetic operators - are used to perform mathematical operations on numeric values.
def add(a, b):
    return a + b    
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def modulus(a, b):
    return a % b
def exponent(a, b): 
    return a ** b       
def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b
#bitwise operators - are used to perform bit-level operations on integer values.
def bitwise_and(a, b):
    return a & b
def bitwise_or(a, b):
    return a | b    
def bitwise_xor(a, b):
    return a ^ b
def bitwise_not(a):
    return ~a
def left_shift(a, b):
    return a << b
def right_shift(a, b):
    return a >> b
#assignment operators - are used to assign values to variables.
def assign(value):
    return value
def add_assign(a, b):
    a += b
    return a    
def subtract_assign(a, b):
    a -= b
    return a    
def multiply_assign(a, b):
    a *= b
    return a
def divide_assign(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    a /= b
    return a
def modulus_assign(a, b):
    a %= b
    return a
def exponent_assign(a, b):
    a **= b
    return a
def floor_divide_assign(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    a //= b
    return a
def bitwise_and_assign(a, b):
    a &= b
    return a
def bitwise_or_assign(a, b):
    a |= b
    return a
def bitwise_xor_assign(a, b):
    a ^= b
    return a
def left_shift_assign(a, b):
    a <<= b
    return a
def right_shift_assign(a, b):
    a >>= b
    return a    
#ternary operator - is a shorthand way of writing an if-else statement.
def ternary(condition, true_value, false_value):
    return true_value if condition else false_value
#identity operators - are used to compare the memory locations of two objects.
def is_operator(a, b):
    return a is b
def is_not_operator(a, b):
    return a is not b
#membership operators - are used to test whether a value is present in a sequence (like a list, tuple, or string).
def in_operator(a, b):
    return a in b
def not_in_operator(a, b):
    return a not in b
#unary operators - are operators that operate on a single operand to produce a new value.
def unary_plus(a):
    return +a
def unary_minus(a):
    return -a
def increment(a):
    return a + 1
def decrement(a):
    return a - 1
def logical_negation(a):
    return not a
def bitwise_negation(a):
    return ~a   
def absolute_value(a):
    return abs(a)
def square(a):
    return a * a    
def cube(a):
    return a * a * a
def factorial(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result
def square_root(a):
    if a < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return a ** 0.5
def negate(a):
    return -a
def increment_by(a, value):
    return a + value
def decrement_by(a, value):
    return a - value
def double(a):
    return a * 2
def halve(a):
    return a / 2
def invert_boolean(a):
    return not a
def bitwise_left_shift(a, n):
    return a << n
def bitwise_right_shift(a, n):
    return a >> n
def identity(a):
    return a    
def to_string(a):
    return str(a)
def to_integer(a):
    return int(a)
def to_float(a):
    return float(a) 
def to_boolean(a):
    return bool(a)
def to_list(a):
    return list(a)
def to_tuple(a):
    return tuple(a)
def to_set(a):  
    return set(a)
def to_dict(a):
    return dict(a)
def length(a):
    return len(a)                                               
def type_of(a):
    return type(a)
def hash_of(a):
    return hash(a)
def id_of(a):
    return id(a)    
def round_value(a, n=0):
    return round(a, n)  
def ceil_value(a):
    import math
    return math.ceil(a) 
def floor_value(a):
    import math
    return math.floor(a)
def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0
def is_even(a):
    return a % 2 == 0   
def is_odd(a):
    return a % 2 != 0
def is_positive(a):
    return a > 0
def is_negative(a):
    return a < 0    
def is_zero(a):
    return a == 0
def is_nonzero(a):
    return a != 0
def is_nan(a):
    import math
    return math.isnan(a)    
def is_infinite(a):
    import math
    return math.isinf(a)
def clamp(a, min_value, max_value):
    return max(min(a, max_value), min_value)
def swap(a, b):
    return b, a
def average(a, b):
    return (a + b) / 2
def midpoint(a, b):
    return (a + b) / 2
def distance(a, b):
    return abs(a - b)
def power_of_two(a):
    return 2 ** a
def logarithm(a, base=10):
    import math
    if a <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    return math.log(a, base)
def sine(a):
    import math
    return math.sin(a)
def cosine(a):
    import math
    return math.cos(a)
def tangent(a):
    import math
    return math.tan(a)  
def arcsine(a):
    import math
    if a < -1 or a > 1:
        raise ValueError("Arcsine is only defined for values in the range [-1, 1].")
    return math.asin(a)
def arccosine(a):
    import math
    if a < -1 or a > 1:
        raise ValueError("Arccosine is only defined for values in the range [-1, 1].")
    return math.acos(a)
def arctangent(a):
    import math
    return math.atan(a)
def degrees(a):
    import math
    return math.degrees(a)
def radians(a):
    import math
    return math.radians(a)
def factorial_recursive(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if a == 0 or a == 1:
        return 1
    return a * factorial_recursive(a - 1)
def gcd(a, b):
    import math
    return math.gcd(a, b)   
def lcm(a, b):
    import math
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)
def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
def next_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    next_num = a + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num
def previous_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    prev_num = a - 1
    while prev_num > 1 and not is_prime(prev_num):
        prev_num -= 1
    return prev_num if prev_num > 1 else None   
def fibonacci(n):
    if n <= 0:
        raise ValueError("Fibonacci is not defined for non-positive integers.")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
def lucas(n):
    if n < 0:
        raise ValueError("Lucas is not defined for negative integers.")
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def collatz_steps(n):
    if n <= 0:
        raise ValueError("Collatz sequence is not defined for non-positive integers.")
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
def collatz_sequence(n):
    if n <= 0:
        raise ValueError("Collatz sequence is not defined for non-positive integers.")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
def harmonic_number(n):
    if n <= 0:
        raise ValueError("Harmonic number is not defined for non-positive integers.")
    harmonic_sum = 0.0
    for i in range(1, n + 1):
        harmonic_sum += 1 / i
    return harmonic_sum
def geometric_mean(a, b):
    if a < 0 or b < 0:
        raise ValueError("Geometric mean is not defined for negative numbers.")
    return (a * b) ** 0.5
def arithmetic_mean(a, b):
    return (a + b) / 2
def quadratic_mean(a, b):   
    return ((a**2 + b**2) / 2) ** 0.5
def cubic_mean(a, b):
    return ((a**3 + b**3) / 2) ** (1/3)
def weighted_mean(values, weights):
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight
def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]
def mode(values):
    from collections import Counter
    if not values:
        raise ValueError("Mode is not defined for an empty list.")
    count = Counter(values)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    if len(modes) == 1:
        return modes[0]
    else:
        return modes  # Return all modes if there's a tie
def variance(values):
    if len(values) == 0:
        raise ValueError("Variance is not defined for an empty list.")
    mean_value = sum(values) / len(values)
    return sum((x - mean_value) ** 2 for x in values) / len(values)
def standard_deviation(values):
    import math
    return math.sqrt(variance(values))
def z_score(value, values):
    mean_value = sum(values) / len(values)
    std_dev = standard_deviation(values)
    if std_dev == 0:
        raise ValueError("Standard deviation cannot be zero for z-score calculation.")
    return (value - mean_value) / std_dev
def percentile(value, values):
    sorted_values = sorted(values)
    count = sum(1 for v in sorted_values if v < value)
    return (count / len(values)) * 100
def quartiles(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        lower_half = sorted_values[:mid]
        upper_half = sorted_values[mid:]
    else:
        lower_half = sorted_values[:mid]
        upper_half = sorted_values[mid + 1:]
    q1 = median(lower_half)
    q2 = median(sorted_values)
    q3 = median(upper_half)
    return q1, q2, q3       
def interquartile_range(values):
    q1, _, q3 = quartiles(values)
    return q3 - q1  
def skewness(values):   
    mean_value = sum(values) / len(values)
    std_dev = standard_deviation(values)
    n = len(values)
    if std_dev == 0:
        raise ValueError("Standard deviation cannot be zero for skewness calculation.")
    skew = sum((x - mean_value) ** 3 for x in values) / n
    skew /= std_dev ** 3
    return skew
def kurtosis(values):
    mean_value = sum(values) / len(values)
    std_dev = standard_deviation(values)
    n = len(values)
    if std_dev == 0:
        raise ValueError("Standard deviation cannot be zero for kurtosis calculation.")
    kurt = sum((x - mean_value) ** 4 for x in values) / n
    kurt /= std_dev ** 4
    return kurt - 3  # Excess kurtosis
def covariance(X, Y):
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    cov = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / n
    return cov
def correlation_coefficient(X, Y):
    import math
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    std_dev_X = math.sqrt(sum((x - mean_X) ** 2 for x in X) / n)
    std_dev_Y = math.sqrt(sum((y - mean_Y) ** 2 for y in Y) / n)
    if std_dev_X == 0 or std_dev_Y == 0:
        raise ValueError("Standard deviation cannot be zero for correlation coefficient calculation.")
    cov = covariance(X, Y)
    return cov / (std_dev_X * std_dev_Y)
def linear_regression(X, Y):
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(n))
    if denominator == 0:
        raise ValueError("Denominator cannot be zero for linear regression calculation.")
    slope = numerator / denominator
    intercept = mean_Y - slope * mean_X
    return slope, intercept
def predict_linear_regression(slope, intercept, x):
    return slope * x + intercept
def moving_average(values, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be a positive integer.")
    if len(values) < window_size:
        raise ValueError("Values length must be greater than or equal to window size.")
    moving_averages = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        moving_averages.append(sum(window) / window_size)
    return moving_averages
def exponential_moving_average(values, alpha):
    if not (0 < alpha <= 1):
        raise ValueError("Alpha must be in the range (0, 1].")
    ema = []
    ema_current = values[0]
    ema.append(ema_current)
    for value in values[1:]:
        ema_current = alpha * value + (1 - alpha) * ema_current
        ema.append(ema_current)
    return ema
def weighted_moving_average(values, weights):
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")
    wma = []
    for i in range(len(values)):
        weighted_sum = sum(values[j] * weights[j] for j in range(i + 1))
        wma.append(weighted_sum / total_weight)
    return wma