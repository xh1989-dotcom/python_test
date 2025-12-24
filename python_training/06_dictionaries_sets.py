"""
Python Training - File 06: Dictionaries and Sets

This file covers:
- Dictionaries: creation, access, methods
- Dictionary operations and comprehension
- Sets: creation, operations
- Set methods and operations
- Practical examples
"""

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

# Different ways to create dictionaries
empty_dict = {}
dict_constructor = dict(name="Bob", age=25, city="New York")
dict_from_pairs = dict([("fruit", "apple"), ("color", "red")])

print("Student dictionary:", student)
print("Constructor dictionary:", dict_constructor)
print("Pairs dictionary:", dict_from_pairs)

# Accessing dictionary values
print("\nAccessing dictionary values:")
print("Student name:", student["name"])
print("Student age:", student.get("age"))
print("Student phone (default):", student.get("phone", "Not provided"))

# Adding and updating dictionary values
student["year"] = 3  # Add new key-value pair
student["gpa"] = 3.9  # Update existing value
print("\nUpdated student:", student)

# Dictionary methods
print("\nDictionary methods:")
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Dictionary operations
person = {"name": "Charlie", "age": 30}
person.update({"city": "Boston", "job": "Engineer"})  # Add multiple key-value pairs
print("\nUpdated person:", person)

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(f"\nSquares dictionary: {squares_dict}")

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Creating sets
fruits = {"apple", "banana", "orange"}
numbers_set = {1, 2, 3, 4, 5}
mixed_set = {"hello", 42, 3.14, True}

print("\nSets:")
print("Fruits set:", fruits)
print("Numbers set:", numbers_set)
print("Mixed set:", mixed_set)

# Creating empty set (note: {} creates empty dict, not set)
empty_set = set()

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union
union_set = set_a | set_b
print(f"Union (A | B): {union_set}")

# Intersection
intersection_set = set_a & set_b
print(f"Intersection (A & B): {intersection_set}")

# Difference
difference_set = set_a - set_b
print(f"Difference (A - B): {difference_set}")

# Symmetric difference
sym_diff_set = set_a ^ set_b
print(f"Symmetric difference (A ^ B): {sym_diff_set}")

# Set methods
print("\nSet methods:")
fruits.add("grape")  # Add single item
print("After adding grape:", fruits)

fruits.update(["kiwi", "mango"])  # Add multiple items
print("After updating with more fruits:", fruits)

removed_fruit = fruits.pop()  # Remove and return random item
print(f"Randomly removed fruit: {removed_fruit}")
print("After pop:", fruits)

fruits.discard("banana")  # Remove item if present (no error if not found)
print("After discarding banana:", fruits)

# Check set membership
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'mango' not in fruits? {'mango' not in fruits}")

# Set comprehensions
squares_set = {x**2 for x in range(1, 6)}
print(f"\nSquares set: {squares_set}")

# Practical example: Counting character frequencies
text = "hello world"
char_count = {}
for char in text:
    if char != ' ':  # Don't count spaces
        char_count[char] = char_count.get(char, 0) + 1
print(f"\nCharacter count in '{text}': {char_count}")

# Practical example: Removing duplicates from a list
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print(f"\nOriginal list: {original_list}")
print(f"Unique list: {unique_list}")

# Practical example: Finding common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print(f"\nList 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {common_elements}")