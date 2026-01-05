#strings - set or collection of characters , represented in " " or ' '
cousrse = "Python Programming"
print(cousrse)  # Output: Python Programming
print(type(cousrse))  # Output: <class 'str'>
# Multiline string - used to represent string in multiple lines by using triple quotes """ or '''"
message = """
This is a multiline string.
It can span multiple lines.
You can include line breaks and indentation.
"""
print(message)
# Output:
# This is a multiline string.   
# It can span multiple lines.
# You can include line breaks and indentation.
print(type(message))  # Output: <class 'str'>
#String functions - length , used to calculate or count the no of characeters in a sting , it is a built in finction
len(course)#here course is the argument accepted by the len function
print(len(cousrse))  # Output: 18
# String indexing - accessing individual characters in a string using their position (index)
print(cousrse[0])  # Output: P
print(cousrse[7])  # Output: P  
print(cousrse[-1])  # Output: g
print(cousrse[-3])  # Output: i
# String slicing - extracting a portion of a string using a range of indices
print(cousrse[0:6])  # Output: Python
print(cousrse[7:18])  # Output: Programming
print(cousrse[:6])  # Output: Python    
print(cousrse[7:])  # Output: Programming
print(cousrse[:])  # Output: Python Programming 
# String methods - built-in functions that perform specific operations on strings
print(cousrse.upper())  # Output: PYTHON PROGRAMMING    
print(cousrse.lower())  # Output: python programming
print(cousrse.replace("Python", "Java"))  # Output: Java Programming
print(cousrse.find("Pro"))  # Output: 7
print(cousrse.find("Java"))  # Output: -1 (not found)
print(cousrse.split(" "))  # Output: ['Python', 'Programming']
print(cousrse.split("g"))  # Output: ['Python Pro', 'rammin', '']   
# Escape sequences - special characters that are used to represent certain characters within a string
print("Hello\nWorld")  # Output:
# Hello
# World 
print("Hello\tWorld")  # Output: Hello    World
print("He said, \"Python is awesome!\"")  # Output: He said,
# Python is awesome!
print('It\'s a beautiful day!')  # Output: It's a beautiful day!
print("C:\\Users\\Username")  # Output: C:\Users\Username
# Raw strings - strings that treat backslashes as literal characters, useful for file paths and regular expressions
raw_string = r"C:\Users\Username"
print(raw_string)  # Output: C:\Users\Username
print(type(raw_string))  # Output: <class 'str'>
# String concatenation - combining multiple strings into one using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name    
print(full_name)  # Output: John Doe
# String formatting - inserting values into a string using placeholders
age = 25
formatted_string = "My name is {} and I am {} years old.".format(full_name, age)
print(formatted_string)  # Output: My name is John Doe and I am 25
# f-strings (formatted string literals) - a more concise way to format strings using expressions inside curly braces
f_string = f"My name is {full_name} and I am {age} years old"               .
print(f_string)  # Output: My name is John Doe and I am 25 years old.
print(type(f_string))  # Output: <class 'str'>  
# String immutability - strings cannot be changed after they are created
original_string = "Hello"
modified_string = original_string.replace("H", "J")
print(original_string)  # Output: Hello
print(modified_string)  # Output: Jello
print(type(original_string))  # Output: <class 'str'>
print(type(modified_string))  # Output: <class 'str'>
print(id(original_string))  # Output: (some memory address)
print(id(modified_string))  # Output: (different memory address)
# This shows that original_string and modified_string are different objects in memory
print()
# String membership - checking if a substring exists within a string using the in operator
print("Python" in cousrse)  # Output: True
print("Java" in cousrse)  # Output: False
print("Pro" in cousrse)  # Output: True
print("gram" in cousrse)  # Output: True
print("C++" not in cousrse)  # Output: True
print("Python" not in cousrse)  # Output: False
print()
# String comparison - comparing two strings using comparison operators
string1 = "apple"
string2 = "banana"
print(string1 == string2)  # Output: False
print(string1 != string2)  # Output: True
print(string1 < string2)  # Output: True
print(string1 > string2)  # Output: False
print(string1 <= string2)  # Output: True
print(string1 >= string2)  # Output: False
print()
# String iteration - looping through each character in a string using a for loop
for char in cousrse:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n
#  
# P
# r
# o
# g
# r
# a
# m
# m
# i
# n
# g
print()
# String conversion - converting other data types to strings using the str() function       
num = 42
float_num = 3.14
bool_value = True
str_num = str(num)
str_float = str(float_num)
str_bool = str(bool_value)
print(str_num)  # Output: 42
print(str_float)  # Output: 3.14    
print(str_bool)  # Output: True
print(type(str_num))  # Output: <class 'str'>
print(type(str_float))  # Output: <class 'str'>
print(type(str_bool))  # Output: <class 'str'>
print()
# String stripping - removing leading and trailing whitespace using the strip() method
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)  # Output: Hello, World!
print(type(stripped_string))  # Output: <class 'str'>
print()
# String justification - aligning strings using ljust(), rjust(), and center() methods
text = "Hello"
left_justified = text.ljust(10) 
right_justified = text.rjust(10)
centered = text.center(10)
print(f"'{left_justified}'")  # Output: 'Hello     '
print(f"'{right_justified}'")  # Output: '     Hello'
print(f"'{centered}'")  # Output: '  Hello   '
print()
# String counting - counting occurrences of a substring using the count() method
sample_text = "banana"
count_a = sample_text.count("a")
count_an = sample_text.count("an")
print(count_a)  # Output: 3
print(count_an)  # Output: 2
print()
# String startswith() and endswith() - checking the beginning and end of a string
filename = "document.txt"
print(filename.startswith("doc"))  # Output: True
print(filename.endswith(".txt"))  # Output: True
print(filename.startswith("txt"))  # Output: False
print(filename.endswith("doc"))  # Output: False
print()
# String zfill() - padding a string with leading zeros to a specified width
number_string = "42"
padded_string = number_string.zfill(5)
print(padded_string)  # Output: 00042
print(type(padded_string))  # Output: <class 'str'>
print()
# String ord() and chr() - converting characters to their Unicode code points and vice versa
char = 'A'
code_point = ord(char)
print(code_point)  # Output: 65
retrieved_char = chr(code_point)
print(retrieved_char)  # Output: A
print(type(code_point))  # Output: <class 'int'>
print(type(retrieved_char))  # Output: <class 'str'>
print()
# String partition() - splitting a string into three parts based on a separator
text = "hello world"
before, sep, after = text.partition(" ")
print(before)  # Output: hello
print(sep)     # Output:
print(after)   # Output: world
print()
# String rpartition() - splitting a string into three parts based on the last occurrence of a separator
text = "hello world example"
before, sep, after = text.rpartition(" ")
print(before)  # Output: hello world
print(sep)     # Output:
print(after)   # Output: example
print()
# String isalpha(), isdigit(), isspace() - checking the nature of characters in a
alpha_string = "Hello"
digit_string = "12345"
space_string = "   "
print(alpha_string.isalpha())  # Output: True
print(digit_string.isdigit())  # Output: True
print(space_string.isspace())  # Output: True
print(alpha_string.isdigit())  # Output: False
print(digit_string.isalpha())  # Output: False
print(space_string.isalpha())  # Output: False
print()
# String title() - converting the first character of each word to uppercase
sentence = "hello world from python"
title_case = sentence.title()
print(title_case)  # Output: Hello World From Python
print(type(title_case))  # Output: <class 'str'>
print()
# String swapcase() - swapping the case of each character in a string
mixed_case = "Hello World"
swapped_case = mixed_case.swapcase()
print(swapped_case)  # Output: hELLO wORLD
print(type(swapped_case))  # Output: <class 'str'>  
print()
# String encode() and decode() - converting strings to bytes and vice versa
original_string = "Hello, World!"
encoded_string = original_string.encode("utf-8")
print(encoded_string)  # Output: b'Hello, World!'
decoded_string = encoded_string.decode("utf-8")
print(decoded_string)  # Output: Hello, World!
print(type(encoded_string))  # Output: <class 'bytes'>
print(type(decoded_string))  # Output: <class 'str'>
print()
# String format_map() - formatting a string using a dictionary
data = {"name": "Alice", "age": 30}
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.
print(type(formatted_string))  # Output: <class 'str'>
print()
# String maketrans() and translate() - replacing characters in a string using a translation table   
translation_table = str.maketrans("aeiou", "12345")
original_text = "hello world"
translated_text = original_text.translate(translation_table)
print(translated_text)  # Output: h2ll4 w4rld
print(type(translated_text))  # Output: <class 'str'>
print()
# String count() - counting occurrences of a substring in a string
text = "the quick brown fox jumps over the lazy dog"
count_the = text.count("the")
print(count_the)  # Output: 2
print(type(count_the))  # Output: <class 'int'>
print()
# String islower() and isupper() - checking if all characters in a string are lowercase or uppercase
lowercase_string = "hello"
uppercase_string = "WORLD"
print(lowercase_string.islower())  # Output: True
print(uppercase_string.isupper())  # Output: True
print(lowercase_string.isupper())  # Output: False
print(uppercase_string.islower())  # Output: False
print()
# String expandtabs() - replacing tab characters with spaces
tabbed_string = "Hello\tWorld"
expanded_string = tabbed_string.expandtabs(4)
print(expanded_string)  # Output: Hello   World
print(type(expanded_string))  # Output: <class 'str'>
print()
# String center() - centering a string within a specified width
text = "Python"
centered_text = text.center(20) 
print(f"'{centered_text}'")  # Output: '       Python        '
print(type(centered_text))  # Output: <class 'str'>
print()
# String lstrip() and rstrip() - removing leading and trailing whitespace respectively
whitespace_string = "   Hello, World!   "
left_stripped = whitespace_string.lstrip()
right_stripped = whitespace_string.rstrip()
print(f"'{left_stripped}'")  # Output: 'Hello, World!   '
print(f"'{right_stripped}'")  # Output: '   Hello, World!'
print(type(left_stripped))  # Output: <class 'str'>
print(type(right_stripped))  # Output: <class 'str'>
print()
# String casefold() - converting a string to lowercase for case-insensitive comparisons
mixed_case_string = "Hello World"
casefolded_string = mixed_case_string.casefold()
print(casefolded_string)  # Output: hello world
print(type(casefolded_string))  # Output: <class 'str'>
print()
# String partition() - splitting a string into three parts based on a separator
text = "key:value:extra"
before, sep, after = text.partition(":")
print(before)  # Output: key
print(sep)     # Output: :
print(after)   # Output: value:extra
print()
# String rfind() - finding the last occurrence of a substring in a string
text = "hello world, welcome to the world"
last_index = text.rfind("world")
print(last_index)  # Output: 21
print(type(last_index))  # Output: <class 'int'>
print()
# String isdecimal() - checking if all characters in a string are decimal characters
decimal_string = "12345"
print(decimal_string.isdecimal())  # Output: True
non_decimal_string = "123a45"
print(non_decimal_string.isdecimal())  # Output: False
print()
# String isprintable() - checking if all characters in a string are printable
printable_string = "Hello, World!"
print(printable_string.isprintable())  # Output: True   
non_printable_string = "Hello\x00World"
print(non_printable_string.isprintable())  # Output: False
print()
# String join() - joining a list of strings into a single string using a specified separator
string_list = ["Hello", "World", "from", "Python"]
joined_string = " ".join(string_list)
print(joined_string)  # Output: Hello World from Python
print(type(joined_string))  # Output: <class 'str'>
print()
# String removeprefix() and removesuffix() - removing a specified prefix or suffix from a
text = "unhappy"
without_prefix = text.removeprefix("un")
print(without_prefix)  # Output: happy
text2 = "running"
without_suffix = text2.removesuffix("ing")
print(without_suffix)  # Output: run
print()
# String format() with named placeholders - formatting a string using named placeholders
formatted_string = "My name is {name} and I am {age} years old.".format(name="Bob", age=28)
print(formatted_string)  # Output: My name is Bob and I am 28 years old.
print(type(formatted_string))  # Output: <class 'str'>
print()
# String encode() with different encodings - converting strings to bytes using different encodings
original_string = "Hello, World!"
encoded_utf16 = original_string.encode("utf-16")
print(encoded_utf16)  # Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00'
decoded_utf16 = encoded_utf16.decode("utf-16")
print(decoded_utf16)  # Output: Hello, World!
print()
print(type(encoded_utf16))  # Output: <class 'bytes'>
print(type(decoded_utf16))  # Output: <class 'str'>
print()
# String zfill() with negative numbers - padding negative number strings with leading zeros
negative_number_string = "-42"
padded_negative_string = negative_number_string.zfill(5)
print(padded_negative_string)  # Output: -0042
print(type(padded_negative_string))  # Output: <class 'str'>
print()
# String isidentifier() - checking if a string is a valid Python identifier
identifier1 = "valid_name"
identifier2 = "1invalid_name"
print(identifier1.isidentifier())  # Output: True
print(identifier2.isidentifier())  # Output: False
print()
# String encode() and decode() with errors parameter - handling encoding/decoding errors
original_string = "Hello, World! ñ"
encoded_string = original_string.encode("ascii", errors="ignore")
print(encoded_string)  # Output: b'Hello, World! '
decoded_string = encoded_string.decode("ascii", errors="ignore")
print(decoded_string)  # Output: Hello, World!
print()
print(type(encoded_string))  # Output: <class 'bytes'>
print(type(decoded_string))  # Output: <class 'str'>
print()
# String removeprefix() and removesuffix() with non-matching cases
text = "HelloWorld"
without_prefix = text.removeprefix("hello")
print(without_prefix)  # Output: HelloWorld
text2 = "HelloWorld"
without_suffix = text2.removesuffix("WORLD")
print(without_suffix)  # Output: HelloWorld
print()
# String format() with alignment specifiers - formatting a string with alignment options
name = "Alice"
age = 30
formatted_string = "Name: {:<10} Age: {:>3}".format(name, age)
print(formatted_string)  # Output: Name: Alice      Age:  30
print(type(formatted_string))  # Output: <class 'str'>
print()
# String encode() and decode() with BOM (Byte Order Mark) - handling Unicode strings with BOM
original_string = "Hello, World!"
encoded_string = original_string.encode("utf-8-sig")
print(encoded_string)  # Output: b'\xef\xbb\xbfHello, World!'
decoded_string = encoded_string.decode("utf-8-sig")
print(decoded_string)  # Output: Hello, World!
print()
print(type(encoded_string))  # Output: <class 'bytes'>
print(type(decoded_string))  # Output: <class 'str'>
print()
# String casefold() for case-insensitive comparisons - comparing two strings ignoring case
string1 = "Hello"
string2 = "hello"
print(string1.casefold() == string2.casefold())  # Output: True
print()
# String translate() with complex translation table - replacing multiple characters in a string
translation_table = str.maketrans({"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"})
original_text = "hello universe"
translated_text = original_text.translate(translation_table)    
print(translated_text)  # Output: h2ll4 5n3v2rs2
print(type(translated_text))  # Output: <class 'str'>   
print()
# String isascii() - checking if all characters in a string are ASCII characters
ascii_string = "Hello"
print(ascii_string.isascii())  # Output: True
non_ascii_string = "Hello ñ"
print(non_ascii_string.isascii())  # Output: False
print()
# String removeprefix() and removesuffix() with overlapping substrings
text = "aaaaabbbb"
without_prefix = text.removeprefix("aaa")
print(without_prefix)  # Output: aabbbb
text2 = "bbbbbaaaa"
without_suffix = text2.removesuffix("aaa")
print(without_suffix)  # Output: bbbbba
print()