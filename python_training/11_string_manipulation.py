"""
Python Training - File 11: String Manipulation

This file covers:
- String methods and operations
- String formatting
- Regular expressions
- String searching and replacing
- Working with text data
"""

# Basic string operations
text = "  Hello, Python World!  "
print(f"Original text: '{text}'")
print(f"Length: {len(text)}")

# String case methods
print(f"\nCase methods:")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# String trimming methods
print(f"\nTrimming methods:")
print(f"Strip: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

# String searching methods
print(f"\nSearching methods:")
search_text = "Python"
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with 'World!': {text.endswith('World!')}")
print(f"Contains '{search_text}': {search_text in text}")
print(f"Find '{search_text}': {text.find(search_text)}")
print(f"Index of '{search_text}': {text.index(search_text)}")

# Count occurrences
print(f"\nCounting:")
print(f"Count of 'o': {text.count('o')}")
print(f"Count of 'l': {text.count('l')}")

# String splitting and joining
sentence = "Python,is,awesome,for,data,processing"
print(f"\nSplitting and joining:")
words = sentence.split(',')
print(f"Split by comma: {words}")
joined = ' '.join(words)
print(f"Joined with space: '{joined}'")
joined_hyphen = '-'.join(words)
print(f"Joined with hyphen: '{joined_hyphen}'")

# Partitioning strings
full_name = "John-Doe-Smith"
first, sep, last = full_name.partition('-')
print(f"\nPartitioning '{full_name}': '{first}', '{sep}', '{last}'")

# String replacement
original = "I love Java. Java is great!"
print(f"\nReplacement:")
print(f"Original: {original}")
print(f"Replace 'Java' with 'Python': {original.replace('Java', 'Python')}")
print(f"Replace only first occurrence: {original.replace('Java', 'Python', 1)}")

# String formatting methods
name = "Alice"
age = 30
city = "New York"

print(f"\nString formatting methods:")
# Old-style formatting with %
print("Old style: %s is %d years old and lives in %s" % (name, age, city))

# New-style formatting with .format()
print("New style: {} is {} years old and lives in {}".format(name, age, city))
print("New style with indices: {0} is {1} years old and lives in {2}".format(name, age, city))
print("New style with names: {name} is {age} years old and lives in {city}".format(name=name, age=age, city=city))

# F-strings (recommended for Python 3.6+)
print(f"F-string: {name} is {age} years old and lives in {city}")
print(f"F-string with expressions: {name.upper()} will be {age + 1} next year")

# Advanced string formatting
import math
print(f"\nAdvanced formatting:")
print(f"Pi rounded to 2 decimal places: {math.pi:.2f}")
print(f"Large number with commas: {1234567:,}")
print(f"Percentage: {0.85:.1%}")

# Padding and alignment
print(f"\nPadding and alignment:")
print(f"Left aligned: '{name:<10}'")
print(f"Right aligned: '{name:>10}'")
print(f"Center aligned: '{name:^10}'")
print(f"Padded with zeros: '{age:0>5}'")

# Working with different string types
multiline = """
This is a
multiline
string
"""
print(f"\nMultiline string: {multiline}")

# Raw strings (useful for regex and file paths)
raw_string = r"C:\Users\Name\Documents\file.txt"
print(f"Raw string (path): {raw_string}")

# Working with escape sequences
escape_example = "Line 1\nLine 2\tTabbed"
print(f"Escape sequences: {escape_example}")

# String validation methods
test_strings = ["hello", "Hello123", "12345", "Hello World", "   ", ""]
print(f"\nString validation:")
for s in test_strings:
    print(f"'{s}' - isalpha: {s.isalpha()}, isalnum: {s.isalnum()}, isdigit: {s.isdigit()}, isspace: {s.isspace()}")

# Using regular expressions
import re

print(f"\nRegular expressions:")
text_to_search = "The quick brown fox jumps over the lazy dog. Contact: john@example.com"

# Find all words starting with 'th'
th_matches = re.findall(r'\bth\w*', text_to_search, re.IGNORECASE)
print(f"Words starting with 'th': {th_matches}")

# Find email pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email_matches = re.findall(email_pattern, text_to_search)
print(f"Emails found: {email_matches}")

# Replace digits with 'X'
text_with_numbers = "Call me at 555-123-4567 or 987-654-3210"
masked_text = re.sub(r'\d', 'X', text_with_numbers)
print(f"Masked phone numbers: {masked_text}")

# Split by multiple delimiters
mixed_delimiters = "apple,banana;orange:grape"
fruits = re.split(r'[,;:]', mixed_delimiters)
print(f"Split by multiple delimiters: {fruits}")

# Practical example: Processing user input
def clean_user_input(user_input):
    """Clean and validate user input"""
    # Remove leading/trailing whitespace
    cleaned = user_input.strip()
    
    # Remove extra spaces between words
    cleaned = ' '.join(cleaned.split())
    
    # Validate if not empty
    if not cleaned:
        raise ValueError("Input cannot be empty")
    
    return cleaned

try:
    user_input = "  Hello    world   with    extra   spaces  "
    cleaned = clean_user_input(user_input)
    print(f"\nCleaned input: '{cleaned}'")
except ValueError as e:
    print(f"Error: {e}")

# Practical example: Text analysis
sample_text = """
Python is a high-level programming language. 
Python is known for its simplicity and readability.
Many developers choose Python for web development, data science, and automation.
"""

# Count sentences, words, and characters
sentences = [s.strip() for s in sample_text.split('.') if s.strip()]
words = sample_text.split()
char_count = len(sample_text)
alpha_char_count = sum(1 for c in sample_text if c.isalpha())

print(f"\nText analysis:")
print(f"Sentences: {len(sentences)}")
print(f"Words: {len(words)}")
print(f"Total characters: {char_count}")
print(f"Alphabetic characters: {alpha_char_count}")

# Count occurrences of a word (case-insensitive)
word_to_count = "Python"
word_count = sum(1 for word in words if word.lower().strip('.,!?') == word_to_count.lower())
print(f"'{word_to_count}' appears {word_count} times")

print("\nString manipulation completed!")