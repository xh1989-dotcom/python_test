"""
Python Training - File 14: Lambda Functions and Functional Programming

This file covers:
- Lambda functions
- Map, filter, reduce functions
- Higher-order functions
- Functional programming concepts
- Decorators basics
- Practical examples
"""

# Lambda functions basics
print("Lambda functions basics:")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"Add 3 and 4: {add(3, 4)}")

# Lambda with conditional expression
max_value = lambda a, b: a if a > b else b
print(f"Max of 10 and 7: {max_value(10, 7)}")

# Using lambda with map()
print(f"\nUsing lambda with map():")
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")

# Map with multiple iterables
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"Numbers1: {numbers1}")
print(f"Numbers2: {numbers2}")
print(f"Sums: {sums}")

# Using lambda with filter()
print(f"\nUsing lambda with filter():")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Even numbers: {even_numbers}")

# Filter with strings
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"Words: {words}")
print(f"Words with length > 5: {long_words}")

# Using reduce() (needs to be imported)
from functools import reduce

print(f"\nUsing lambda with reduce():")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product: {product}")

# Sum using reduce
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum using reduce: {sum_result}")

# Finding maximum using reduce
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Max using reduce: {max_result}")

# Higher-order functions
print(f"\nHigher-order functions:")

def apply_operation(numbers, operation):
    """Apply an operation to each number in the list"""
    return [operation(num) for num in numbers]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
cubed = apply_operation(numbers, cube)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Cubed: {cubed}")

# Using lambda as higher-order function argument
doubled = apply_operation(numbers, lambda x: x * 2)
print(f"Doubled: {doubled}")

# Function that returns another function
def create_multiplier(factor):
    """Create a function that multiplies by the given factor"""
    return lambda x: x * factor

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(f"\nFunction factories:")
print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print(f"Quadruple 5: {quadruple(5)}")

# Using map, filter, and reduce together
print(f"\nChaining functional operations:")
numbers = list(range(1, 11))
print(f"Original: {numbers}")

# Square even numbers and sum them
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(f"Sum of squares of even numbers: {result}")

# Alternative approach using list comprehension (more Pythonic)
result_alt = sum(x**2 for x in numbers if x % 2 == 0)
print(f"Alternative approach: {result_alt}")

# Sorting with custom key functions (using lambda)
print(f"\nSorting with lambda key functions:")
students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 78),
    ("Diana", 92)
]

# Sort by grade (second element)
sorted_by_grade = sorted(students, key=lambda student: student[1], reverse=True)
print(f"Students: {students}")
print(f"Sorted by grade: {sorted_by_grade}")

# Sort by name length
sorted_by_name_length = sorted(students, key=lambda student: len(student[0]))
print(f"Sorted by name length: {sorted_by_name_length}")

# Working with dictionaries
data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 55000},
    {"name": "Diana", "age": 28, "salary": 65000}
]

# Sort by salary
sorted_by_salary = sorted(data, key=lambda person: person["salary"], reverse=True)
print(f"\nSorted by salary:")
for person in sorted_by_salary:
    print(f"  {person['name']}: ${person['salary']}")

# Filter high earners
high_earners = list(filter(lambda person: person["salary"] > 55000, data))
print(f"\nHigh earners (salary > 55000):")
for person in high_earners:
    print(f"  {person['name']}: ${person['salary']}")

# Map to extract specific data
names = list(map(lambda person: person["name"], data))
salaries = list(map(lambda person: person["salary"], data))
print(f"\nNames: {names}")
print(f"Salaries: {salaries}")

# Partial functions concept with lambda
print(f"\nPartial functions concept:")
from functools import partial

# Instead of lambda, we can use partial for some cases
def multiply(x, y):
    return x * y

# Create a function that always multiplies by 10
multiply_by_10 = partial(multiply, 10)
print(f"Multiply 10 by 5: {multiply_by_10(5)}")

# Using lambda for the same purpose
multiply_by_10_lambda = lambda y: multiply(10, y)
print(f"Multiply 10 by 5 (lambda): {multiply_by_10_lambda(5)}")

# Decorators basics (simple example)
print(f"\nBasic decorators:")

def simple_decorator(func):
    """A simple decorator that adds functionality"""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """Greet someone"""
    return f"Hello, {name}!"

print(f"Calling decorated function: {greet('Alice')}")

# Practical example: Data processing pipeline
print(f"\nPractical example: Data processing pipeline:")

# Sample data
sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 5},
    {"product": "Mouse", "price": 25, "quantity": 50},
    {"product": "Keyboard", "price": 75, "quantity": 30},
    {"product": "Monitor", "price": 300, "quantity": 10},
    {"product": "Headphones", "price": 100, "quantity": 25}
]

# Calculate total revenue for each product
calculate_revenue = lambda item: item["price"] * item["quantity"]
revenues = list(map(calculate_revenue, sales_data))

print("Revenues per product:")
for item, revenue in zip(sales_data, revenues):
    print(f"  {item['product']}: ${revenue}")

# Find high-revenue products (revenue > 500)
high_revenue_items = list(filter(lambda item: calculate_revenue(item) > 500, sales_data))
print(f"\nHigh-revenue products (revenue > $500):")
for item in high_revenue_items:
    print(f"  {item['product']}: ${calculate_revenue(item)}")

# Calculate total revenue
total_revenue = reduce(lambda acc, item: acc + calculate_revenue(item), sales_data, 0)
print(f"\nTotal revenue: ${total_revenue}")

# Extract product names with high margins (price > 100)
high_value_products = list(map(
    lambda item: item["product"],
    filter(lambda item: item["price"] > 100, sales_data)
))
print(f"\nHigh-value products (price > $100): {high_value_products}")

# Practical example: Functional approach to string processing
print(f"\nFunctional string processing:")

text = "The quick brown fox jumps over the lazy dog"
words = text.split()

# Convert to uppercase
uppercase_words = list(map(lambda word: word.upper(), words))
print(f"Uppercase: {' '.join(uppercase_words)}")

# Get words with even length
even_length_words = list(filter(lambda word: len(word) % 2 == 0, words))
print(f"Even-length words: {even_length_words}")

# Count total characters
total_chars = reduce(lambda acc, word: acc + len(word), words, 0)
print(f"Total characters (excluding spaces): {total_chars}")

# Performance consideration example
import time

def performance_comparison():
    """Compare performance between functional and loop approaches"""
    numbers = list(range(1, 100001))
    
    # Using map and lambda
    start_time = time.time()
    squared_map = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
    map_time = time.time() - start_time
    
    # Using list comprehension (more Pythonic)
    start_time = time.time()
    squared_comp = [x**2 for x in numbers if x % 2 == 0]
    comp_time = time.time() - start_time
    
    print(f"\nPerformance comparison (100,000 items):")
    print(f"Map + Filter: {map_time:.4f} seconds")
    print(f"List comprehension: {comp_time:.4f} seconds")
    print(f"Results equal: {squared_map == squared_comp}")

performance_comparison()

print("\nLambda functions and functional programming completed!")