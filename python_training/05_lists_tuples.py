"""
Python Training - File 05: Lists and Tuples

This file covers:
- Lists: creation, indexing, slicing
- List methods and operations
- Tuples: creation and usage
- List vs Tuple differences
- List comprehensions
"""

# Creating lists
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]

print("Fruits list:", fruits)
print("Numbers list:", numbers)
print("Mixed list:", mixed_list)

# List indexing
print("\nList indexing:")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Third fruit:", fruits[2])

# List slicing
print("\nList slicing:")
print("First 3 fruits:", fruits[0:3])
print("Last 2 fruits:", fruits[-2:])
print("Every other fruit:", fruits[::2])

# List methods
print("\nList methods:")
fruits.append("mango")  # Add item to end
print("After append:", fruits)

fruits.insert(1, "pear")  # Insert at specific position
print("After insert:", fruits)

removed_fruit = fruits.pop()  # Remove and return last item
print(f"Removed fruit: {removed_fruit}")
print("After pop:", fruits)

fruits.remove("orange")  # Remove specific item
print("After remove:", fruits)

fruits.sort()  # Sort the list
print("After sort:", fruits)

fruits.reverse()  # Reverse the list
print("After reverse:", fruits)

# List operations
print("\nList operations:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined list: {combined}")

list1.extend(list2)  # Extend list1 with elements from list2
print(f"After extend: {list1}")

# Checking membership
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4, 2]
print(f"Number 2 appears {numbers.count(2)} times in the list")

# Creating tuples
colors = ("red", "green", "blue")
single_item = ("single",)  # Note the comma for single-item tuple
empty_tuple = ()

print("\nTuples:")
print("Colors tuple:", colors)
print("Single item tuple:", single_item)
print("Empty tuple:", empty_tuple)

# Tuple indexing and slicing
print("\nTuple indexing and slicing:")
print("First color:", colors[0])
print("Last color:", colors[-1])
print("First two colors:", colors[:2])

# Tuple methods
print(f"Count of 'red' in colors: {colors.count('red')}")
print(f"Index of 'green': {colors.index('green')}")

# Tuple unpacking
r, g, b = colors
print(f"Unpacked colors: red={r}, green={g}, blue={b}")

# List vs Tuple differences
print("\nList vs Tuple differences:")
print("- Lists are mutable, tuples are immutable")
print("- Lists use [], tuples use ()")
print("- Lists have more methods than tuples")
print("- Tuples can be used as dictionary keys, lists cannot")

# List comprehensions
print("\nList comprehensions:")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)

uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatrix:")
for row in matrix:
    print(row)

# Accessing nested list elements
print("Element at row 1, col 2:", matrix[1][2])