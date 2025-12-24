"""
Python Training - File 04: Functions

This file covers:
- Defining and calling functions
- Function parameters and arguments
- Return values
- Scope and global vs local variables
- Lambda functions
"""

# Basic function definition
def greet(name):
    """A simple function that greets a person"""
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)

# Function with multiple parameters
def add_numbers(a, b):
    """Function that adds two numbers"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameters
def introduce(name, age=25, city="Unknown"):
    """Function with default parameters"""
    return f"I'm {name}, {age} years old, from {city}"

print(introduce("Bob"))
print(introduce("Charlie", 30))
print(introduce("David", 28, "Boston"))

# Function with variable number of arguments (*args)
def sum_all(*args):
    """Function that sums all arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

# Function with variable keyword arguments (**kwargs)
def create_profile(**kwargs):
    """Function that creates a profile from keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user_profile = create_profile(name="Eve", age=27, job="Engineer", city="Seattle")
print("User profile:", user_profile)

# Function with both *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts both *args and **kwargs"""
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Frank", age=35)

# Scope example
x = 10  # Global variable

def scope_example():
    y = 5  # Local variable
    print(f"Inside function - x (global): {x}")
    print(f"Inside function - y (local): {y}")
    
    # Modifying global variable
    global x
    x = 20

scope_example()
print(f"Outside function - x (modified): {x}")

# Recursive function example
def factorial(n):
    """Recursive function to calculate factorial"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Lambda functions
square = lambda x: x ** 2
print(f"Square of 4 using lambda: {square(4)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")