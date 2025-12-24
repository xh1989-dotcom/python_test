"""
Python Training - File 02: Data Types

This file covers:
- Python data types
- Numbers (int, float, complex)
- Strings
- Booleans
- Type conversion
"""

# Numbers
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

print("Integer:", integer_num)
print("Float:", float_num)
print("Complex:", complex_num)

# Strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a
multiline string"""

print("Single quote string:", single_quote)
print("Double quote string:", double_quote)
print("Triple quote string:", triple_quote)

# String operations
name = "Python"
print("Length of name:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("First letter:", name[0])
print("Last letter:", name[-1])

# Boolean
is_true = True
is_false = False

print("Boolean True:", is_true)
print("Boolean False:", is_false)

# Type conversion
str_num = "123"
int_num = int(str_num)
float_num = float(str_num)
str_float = str(45.67)

print("String to integer:", int_num, type(int_num))
print("String to float:", float_num, type(float_num))
print("Float to string:", str_float, type(str_float))

# Converting to boolean
bool_false = bool(0)  # False
bool_true = bool(1)   # True
bool_empty_str = bool("")  # False
bool_nonempty_str = bool("hello")  # True

print("Bool from 0:", bool_false)
print("Bool from 1:", bool_true)
print("Bool from empty string:", bool_empty_str)
print("Bool from non-empty string:", bool_nonempty_str)