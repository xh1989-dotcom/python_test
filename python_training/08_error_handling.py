"""
Python Training - File 08: Error Handling

This file covers:
- Try, except, else, finally blocks
- Specific exception handling
- Raising exceptions
- Custom exceptions
- Best practices for error handling
"""

# Basic try-except block
print("Basic try-except example:")
try:
    result = 10 / 0
    print("This won't be printed")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exceptions
print("\nHandling multiple exceptions:")
try:
    value = int("not_a_number")
except ValueError:
    print("Invalid number format!")
except TypeError:
    print("Wrong type provided!")
except Exception as e:
    print(f"Unexpected error: {e}")

# Using else and finally
print("\nUsing else and finally:")
try:
    number = 10
    result = number / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Division successful: {result}")
finally:
    print("This always executes")

# More complex example with file handling
print("\nError handling with file operations:")
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied to read the file!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Handling different types of errors in a calculation
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None
    except TypeError:
        print("Error: Please provide numeric values")
        return None

print("\nSafe division examples:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")

# Using raise to throw exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

print("\nUsing raise to throw exceptions:")
try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

try:
    validate_age(200)
except ValueError as e:
    print(f"Validation error: {e}")

print("Valid age (25):", validate_age(25))

# Creating custom exceptions
class CustomError(Exception):
    """Custom exception class"""
    pass

class InsufficientFundsError(Exception):
    """Exception raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance ${balance}, Requested ${amount}")

# Using custom exceptions
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

print("\nUsing custom exceptions:")
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

# Nested exception handling
print("\nNested exception handling:")
def process_data(data):
    try:
        # Outer try block
        result = 0
        for item in data:
            try:
                # Inner try block
                result += 1 / item
            except ZeroDivisionError:
                print(f"Skipping division by zero for item: {item}")
                continue
        return result
    except TypeError:
        print("Data must be iterable")
        return 0

data1 = [1, 2, 0, 4, 5]
print(f"Processing {data1}: {process_data(data1)}")

data2 = "not_iterable"
print(f"Processing {data2}: {process_data(data2)}")

# Exception hierarchy example
print("\nException hierarchy example:")
def demonstrate_hierarchy():
    test_cases = [
        (lambda: 10/0, "Division by zero"),
        (lambda: int("abc"), "Invalid integer conversion"),
        (lambda: [1,2,3][10], "Index out of range"),
        (lambda: {"a": 1}["b"], "Key not found")
    ]
    
    for test_func, description in test_cases:
        try:
            test_func()
        except ArithmeticError:
            print(f"{description}: Caught by ArithmeticError")
        except LookupError:
            print(f"{description}: Caught by LookupError")
        except ValueError:
            print(f"{description}: Caught by ValueError")
        except Exception:
            print(f"{description}: Caught by general Exception")

demonstrate_hierarchy()

# Practical example: Safe input processing
def safe_input_processor():
    while True:
        try:
            user_input = input("Enter a number (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            number = float(user_input)
            print(f"You entered: {number}, squared: {number**2}")
        except ValueError:
            print("That's not a valid number! Please try again.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

print("\nInput processor example (commented out to avoid blocking execution)")
# safe_input_processor()  # Commented to avoid blocking execution

print("\nError handling best practices demonstrated!")