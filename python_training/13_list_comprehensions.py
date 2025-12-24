"""
Python Training - File 13: List Comprehensions and Generators

This file covers:
- List comprehensions
- Set comprehensions
- Dictionary comprehensions
- Generator expressions
- Generator functions
- Memory efficiency
- Practical examples
"""

# List comprehensions basics
print("List comprehensions basics:")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# List comprehension with complex expression
words = ["hello", "world", "python", "comprehension"]
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# List comprehension with multiple conditions
numbers_range = range(1, 21)
filtered_numbers = [x for x in numbers_range if x % 2 == 0 and x > 10]
print(f"Even numbers > 10: {filtered_numbers}")

# List comprehension with transformation
names = ["alice", "bob", "charlie", "diana"]
capitalized_names = [name.capitalize() for name in names]
print(f"Capitalized names: {capitalized_names}")

# Nested list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Original matrix: {matrix}")
print(f"Flattened: {flattened}")

# List comprehension with nested condition
matrix_with_negatives = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
positive_only = [num for row in matrix_with_negatives for num in row if num > 0]
print(f"Positive numbers only: {positive_only}")

# Set comprehensions
print(f"\nSet comprehensions:")
unique_squares = {x**2 for x in [1, 2, 3, 2, 4, 3, 5]}
print(f"Unique squares: {unique_squares}")

vowels = {char for char in "hello world" if char in "aeiou"}
print(f"Unique vowels: {vowels}")

# Dictionary comprehensions
print(f"\nDictionary comprehensions:")
word_lengths_dict = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(f"Word lengths dictionary: {word_lengths_dict}")

# Dictionary comprehension with condition
squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even number squares: {squares_dict}")

# Dictionary comprehension with transformation
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
transformed_dict = {key.upper(): value*2 for key, value in original_dict.items()}
print(f"Transformed dictionary: {transformed_dict}")

# Generator expressions
print(f"\nGenerator expressions:")
gen_squares = (x**2 for x in range(1, 6))
print(f"Generator object: {gen_squares}")
print(f"Generator squares: {list(gen_squares)}")

# Generator expression with condition
gen_even = (x for x in range(1, 11) if x % 2 == 0)
print(f"Generator evens: {list(gen_even)}")

# Memory efficiency comparison
import sys

# List comprehension (stores all values in memory)
list_comp = [x**2 for x in range(1000)]
list_memory = sys.getsizeof(list_comp)

# Generator expression (generates values on demand)
gen_exp = (x**2 for x in range(1000))
gen_memory = sys.getsizeof(gen_exp)

print(f"\nMemory comparison:")
print(f"List comprehension (1000 items): {list_memory} bytes")
print(f"Generator expression (1000 items): {gen_memory} bytes")
print(f"Generator is {list_memory // gen_memory}x more memory efficient")

# Generator functions
print(f"\nGenerator functions:")

def simple_generator():
    """A simple generator function"""
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(f"Generator values: {list(gen)}")

def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print(f"Fibonacci generator (first 10): {list(fibonacci_generator(10))}")

def square_generator(numbers):
    """Generate squares of numbers"""
    for num in numbers:
        yield num ** 2

numbers = [1, 2, 3, 4, 5]
squares_gen = square_generator(numbers)
print(f"Square generator: {list(squares_gen)}")

# Generator with filtering
def even_numbers(start, end):
    """Generate even numbers in a range"""
    for num in range(start, end):
        if num % 2 == 0:
            yield num

print(f"Even numbers 1-10: {list(even_numbers(1, 11))}")

# Practical example: Processing large datasets
def process_large_file_simulation():
    """Simulate processing a large dataset efficiently"""
    # Instead of loading all data into memory, process one item at a time
    data = range(1, 1000001)  # Simulate large dataset
    
    # Using generator to process data efficiently
    processed = (x * 2 for x in data if x % 1000 == 0)  # Process every 1000th item
    
    # Take only first 10 results
    return [next(processed) for _ in range(10)]

print(f"\nLarge dataset processing (first 10 results): {process_large_file_simulation()}")

# Practical example: Prime number generator
def prime_generator(limit):
    """Generate prime numbers up to limit"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, limit):
        if is_prime(num):
            yield num

print(f"Prime numbers up to 30: {list(prime_generator(30))}")

# Practical example: Text processing with generators
def word_processor(text):
    """Process words in text using generator"""
    words = text.split()
    for word in words:
        # Clean the word
        clean_word = ''.join(char.lower() for char in word if char.isalnum())
        if clean_word:  # Only yield non-empty words
            yield clean_word

text = "Hello, World! This is a sample text with punctuation."
processed_words = list(word_processor(text))
print(f"\nProcessed words: {processed_words}")

# Generator for file reading (memory efficient)
def read_large_file(file_path):
    """Simulate reading a large file line by line"""
    # Instead of reading entire file, yield one line at a time
    lines = [
        "Line 1 of large file",
        "Line 2 of large file", 
        "Line 3 of large file",
        "Line 4 of large file"
    ]
    for line in lines:
        yield line

print(f"Simulated file reading: {list(read_large_file('large_file.txt'))}")

# Practical example: Data transformation pipeline
def data_pipeline(data):
    """Create a data processing pipeline using generators"""
    # Step 1: Filter positive numbers
    filtered = (x for x in data if x > 0)
    
    # Step 2: Square the numbers
    squared = (x**2 for x in filtered)
    
    # Step 3: Keep only numbers less than 100
    final = (x for x in squared if x < 100)
    
    return list(final)

raw_data = [-5, -2, 0, 1, 3, 5, 8, 10, 12]
processed_data = data_pipeline(raw_data)
print(f"\nData pipeline - Input: {raw_data}")
print(f"Data pipeline - Output: {processed_data}")

# Performance comparison: List vs Generator
import time

def time_list_vs_generator():
    # List comprehension timing
    start_time = time.time()
    list_result = [x**2 for x in range(100000) if x % 2 == 0]
    list_time = time.time() - start_time
    
    # Generator expression timing (converting to list for fair comparison)
    start_time = time.time()
    gen_result = list(x**2 for x in range(100000) if x % 2 == 0)
    gen_time = time.time() - start_time
    
    print(f"\nPerformance comparison (100,000 items):")
    print(f"List comprehension: {list_time:.4f} seconds")
    print(f"Generator expression: {gen_time:.4f} seconds")

time_list_vs_generator()

# Practical example: Infinite sequence generator
def infinite_sequence():
    """Generate an infinite sequence"""
    num = 0
    while True:
        yield num
        num += 1

# Use with caution - we'll limit the output
infinite_gen = infinite_sequence()
limited_sequence = [next(infinite_gen) for _ in range(10)]
print(f"\nLimited infinite sequence: {limited_sequence}")

print("\nList comprehensions and generators completed!")