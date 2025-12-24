"""
Python Training - File 07: File Handling

This file covers:
- Reading from files
- Writing to files
- Appending to files
- Working with different file modes
- Context managers (with statement)
- Working with CSV and JSON files
"""

# Writing to a file
print("Writing to a file...")
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python file handling!\n")
    file.write("This is the second line.\n")
    file.write("File handling is important in Python.\n")

print("File written successfully!")

# Reading from a file - method 1: read()
print("\nReading entire file content:")
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Reading from a file - method 2: readline()
print("Reading line by line:")
with open("sample.txt", "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

# Reading from a file - method 3: readlines()
print("\nReading all lines as a list:")
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# Appending to a file
print("\nAppending to the file...")
with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

print("Content after appending:")
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Writing multiple lines
students = [
    "Alice,22,Computer Science",
    "Bob,20,Mathematics", 
    "Charlie,23,Physics"
]

with open("students.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write(student + "\n")

print("\nStudents file created:")
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Working with CSV-like data
print("\nWorking with CSV-like data:")
import csv

# Writing CSV data
with open("data.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Boston"])
    writer.writerow(["Charlie", 35, "Seattle"])

print("CSV file created successfully!")

# Reading CSV data
print("\nReading CSV data:")
with open("data.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Working with JSON
print("\nWorking with JSON data:")
import json

# Creating JSON data
person_data = {
    "name": "David",
    "age": 28,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "city": "San Francisco",
        "zip": "94105"
    }
}

# Writing JSON to file
with open("person.json", "w", encoding="utf-8") as jsonfile:
    json.dump(person_data, jsonfile, indent=2)

print("JSON file created successfully!")

# Reading JSON from file
with open("person.json", "r", encoding="utf-8") as jsonfile:
    loaded_data = json.load(jsonfile)
    print("Loaded JSON data:", loaded_data)

# Different file modes
print("\nFile modes explanation:")
modes = {
    "r": "Read only (default)",
    "w": "Write only (overwrites existing file)",
    "a": "Append only",
    "r+": "Read and write",
    "w+": "Write and read (overwrites existing file)",
    "a+": "Append and read"
}

for mode, description in modes.items():
    print(f"{mode}: {description}")

# Error handling with file operations
print("\nError handling with files:")
try:
    with open("nonexistent.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Creating it instead...")
    with open("nonexistent.txt", "w", encoding="utf-8") as file:
        file.write("This file was created because it didn't exist.")

# Working with binary files
print("\nWorking with binary files:")
# Writing binary data
with open("binary_example.bin", "wb") as binary_file:
    binary_file.write(b"This is binary data")

# Reading binary data
with open("binary_example.bin", "rb") as binary_file:
    binary_content = binary_file.read()
    print(f"Binary content: {binary_content}")

# Removing created files (cleanup)
import os
for filename in ["sample.txt", "students.txt", "data.csv", "person.json", "nonexistent.txt", "binary_example.bin"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed {filename}")