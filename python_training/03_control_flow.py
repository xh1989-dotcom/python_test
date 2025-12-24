"""
Python Training - File 03: Control Flow

This file covers:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Break and continue statements
- Nested conditions and loops
"""

# Conditional Statements
age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Comparison and logical operators
x = 10
y = 20
if x < y and y > 15:
    print("Both conditions are true")

if x < y or x > 15:
    print("At least one condition is true")

if not x > y:
    print("x is not greater than y")

# For loops
print("\nFor loop examples:")
for i in range(5):
    print(f"Iteration {i}")

# Looping through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Looping through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# While loops
print("\nWhile loop example:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Break statement
print("\nBreak statement example:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
print("\nContinue statement example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# Nested loops
print("\nNested loops example:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")