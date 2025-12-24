"""
Python Training - File 10: Modules and Packages

This file covers:
- Importing modules
- Creating and using modules
- Standard library modules
- Third-party packages
- Package structure
- __init__.py files
- Importing with aliases
"""

# Importing standard library modules
import math
import random
import datetime
import os

print("Using standard library modules:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number between 1 and 10: {random.randint(1, 10)}")
print(f"Current date and time: {datetime.datetime.now()}")
print(f"Current working directory: {os.getcwd()}")

# Importing specific functions from a module
from math import pi, e, sin, cos
print(f"\nMath constants - Pi: {pi}, e: {e}")
print(f"sin(pi/2): {sin(pi/2)}")
print(f"cos(0): {cos(0)}")

# Importing with aliases
import numpy as np  # This might not be installed, so let's use a standard library example
from datetime import datetime as dt
print(f"\nUsing alias - Current time: {dt.now()}")

# Creating and importing a custom module
# First, let's create a simple utility module
utils_code = '''
"""
Utility functions module
"""

def calculate_area(length, width):
    """Calculate area of rectangle"""
    return length * width

def calculate_circle_area(radius):
    """Calculate area of circle"""
    import math
    return math.pi * radius ** 2

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Module-level variable
MODULE_NAME = "Math Utilities"
'''

# Write the utility module to a file
with open("math_utils.py", "w", encoding="utf-8") as f:
    f.write(utils_code)

# Now import and use the custom module
import math_utils

print(f"\nUsing custom module:")
print(f"Area of 5x3 rectangle: {math_utils.calculate_area(5, 3)}")
print(f"Area of circle with radius 4: {math_utils.calculate_circle_area(4):.2f}")
print(f"Is 17 prime? {math_utils.is_prime(17)}")
print(f"Factorial of 5: {math_utils.factorial(5)}")
print(f"Module name: {math_utils.MODULE_NAME}")

# Import specific functions from custom module
from math_utils import calculate_area, is_prime
print(f"\nImported functions - Area of 4x6: {calculate_area(4, 6)}")
print(f"Is 20 prime? {is_prime(20)}")

# Using the * operator to import all (not recommended for production)
from math_utils import *
print(f"\nUsing * import - Circle area (radius 3): {calculate_circle_area(3):.2f}")

# Working with packages
# Create a simple package structure
import os

# Create package directory
os.makedirs("mypackage", exist_ok=True)

# Create __init__.py file (makes it a package)
init_code = '''
"""
My custom package
"""

# Package-level variables
VERSION = "1.0.0"
AUTHOR = "Python Trainer"

def package_info():
    return f"MyPackage v{VERSION} by {AUTHOR}"

# Import submodules when package is imported
from . import arithmetic
from . import string_utils

__all__ = ["arithmetic", "string_utils", "package_info", "VERSION", "AUTHOR"]
'''

with open("mypackage/__init__.py", "w", encoding="utf-8") as f:
    f.write(init_code)

# Create a submodule for arithmetic operations
arithmetic_code = '''
"""
Arithmetic operations submodule
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    return base ** exponent
'''

with open("mypackage/arithmetic.py", "w", encoding="utf-8") as f:
    f.write(arithmetic_code)

# Create a submodule for string operations
string_utils_code = '''
"""
String utilities submodule
"""

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def word_count(s):
    return len(s.split())
'''

with open("mypackage/string_utils.py", "w", encoding="utf-8") as f:
    f.write(string_utils_code)

# Now import and use the package
import mypackage
print(f"\nUsing custom package:")
print(f"Package info: {mypackage.package_info()}")
print(f"Addition: {mypackage.arithmetic.add(10, 5)}")
print(f"Reverse 'hello': {mypackage.string_utils.reverse_string('hello')}")
print(f"Vowel count in 'beautiful': {mypackage.string_utils.count_vowels('beautiful')}")

# Import specific submodules
from mypackage import arithmetic, string_utils
print(f"\nUsing imported submodules:")
print(f"Multiplication: {arithmetic.multiply(7, 8)}")
print(f"Is 'racecar' palindrome? {string_utils.is_palindrome('racecar')}")

# Import specific functions from submodules
from mypackage.arithmetic import divide, power
print(f"\nDirect function imports:")
print(f"Division: {divide(15, 3)}")
print(f"Power: {power(2, 8)}")

# Using __name__ to control execution
print(f"\nDemonstrating __name__ usage:")

# Create a script that can be both imported and run directly
script_code = '''
"""
Demonstration of __name__ usage
"""

def greet(name):
    return f"Hello, {name}!"

def main():
    print("This script is being run directly")
    print(greet("World"))

if __name__ == "__main__":
    main()
else:
    print("This script is being imported")
'''

with open("demo_script.py", "w", encoding="utf-8") as f:
    f.write(script_code)

# Import the script to see the difference
import demo_script
print(f"Imported function from script: {demo_script.greet('Python Learner')}")

# Run the script directly (we'll just show the code content)
print("\nContent of demo_script.py:")
with open("demo_script.py", "r", encoding="utf-8") as f:
    print(f.read())

# Working with sys.path to add module locations
import sys
print(f"\nPython path: {sys.path[:3]}...")  # Show first 3 entries

# Demonstrating relative imports (within the same package)
relative_import_code = '''
"""
Demonstrating relative imports
"""

def function_a():
    return "Function A from relative module"

def function_b():
    # This would normally be used within a package
    # from . import arithmetic
    # return arithmetic.add(1, 2)
    return "Simulated relative import usage"
'''

with open("mypackage/relative_demo.py", "w", encoding="utf-8") as f:
    f.write(relative_import_code)

# Using the collections module (standard library)
from collections import Counter, defaultdict, namedtuple, deque

print(f"\nUsing collections module:")
# Counter example
text = "hello world"
char_counts = Counter(text)
print(f"Character counts in '{text}': {dict(char_counts)}")

# defaultdict example
dd = defaultdict(int)
for char in text:
    dd[char] += 1
print(f"Defaultdict result: {dict(dd)}")

# namedtuple example
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"Named tuple points: {p1}, {p2}")

# deque example
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(f"Deque: {list(d)}")

# Clean up created files
import os
for file in ["math_utils.py", "demo_script.py"]:
    if os.path.exists(file):
        os.remove(file)

import shutil
if os.path.exists("mypackage"):
    shutil.rmtree("mypackage")

print("\nModules and packages demonstration completed!")