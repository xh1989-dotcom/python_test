"""
Python Training - File 09: Classes and Objects

This file covers:
- Creating classes and objects
- Instance variables and methods
- Class variables and methods
- Inheritance
- Encapsulation
- Polymorphism
- Special methods (dunder methods)
"""

# Basic class definition
class Person:
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age, city="Unknown"):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.city = city
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, from {self.city}."
    
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."
    
    # Class method
    @classmethod
    def get_species(cls):
        return f"All humans belong to the species: {cls.species}"
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating objects (instances)
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "Boston")

print("Basic class usage:")
print(person1.introduce())
print(person2.introduce())

# Using methods
print(f"\n{person1.have_birthday()}")
print(f"Is {person1.name} an adult? {Person.is_adult(person1.age)}")

# Accessing class variable
print(f"\nClass variable - Species: {Person.species}")
print(f"Class method: {Person.get_species()}")

# Inheritance example
class Student(Person):
    def __init__(self, name, age, city, student_id, major):
        super().__init__(name, age, city)  # Call parent constructor
        self.student_id = student_id
        self.major = major
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    # Override parent method (polymorphism)
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I'm a {self.major} student with ID: {self.student_id}."

# Creating a Student object
student1 = Student("Charlie", 20, "Chicago", "S12345", "Computer Science")
print(f"\nStudent introduction: {student1.introduce()}")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)
print(f"Grades: {student1.grades}")
print(f"Average grade: {student1.get_average_grade():.2f}")

# Another inheritance example - Teacher class
class Teacher(Person):
    def __init__(self, name, age, city, employee_id, subject):
        super().__init__(name, age, city)
        self.employee_id = employee_id
        self.subject = subject
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I teach {self.subject} and have {len(self.students)} students."

teacher1 = Teacher("Dr. Smith", 45, "Seattle", "T98765", "Mathematics")
print(f"\nTeacher introduction: {teacher1.introduce()}")

# Add students to teacher
teacher1.add_student(student1)
print(f"After adding student: {teacher1.introduce()}")

# Encapsulation example
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute (name mangling)
        self._account_number = "ACCT" + str(id(self))  # Protected attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        return self.__balance
    
    # Property decorator for balance (getter and setter)
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

# Using encapsulation
account = BankAccount(1000)
print(f"\nInitial balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Final balance: ${account.balance}")

# Trying to access private attribute directly (will show name mangling)
try:
    print(f"Direct access to __balance: {account.__balance}")
except AttributeError as e:
    print(f"Cannot access private attribute directly: {e}")
    
print(f"Access with name mangling: {account._BankAccount__balance}")

# Special methods (dunder methods)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

# Using special methods
book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)
book3 = Book("Python Basics", "John Doe", 250)

print(f"\nString representation: {book1}")
print(f"Length of book1: {len(book1)} pages")
print(f"Is book1 equal to book3? {book1 == book3}")
print(f"Is book1 shorter than book2? {book1 < book2}")

# List of books and sorting
books = [book1, book2, book3]
sorted_books = sorted(books)  # Uses __lt__ method
print(f"Books sorted by pages: {[str(book) for book in sorted_books]}")

# Polymorphism example
def introduce_person(person_obj):
    print(person_obj.introduce())

print("\nPolymorphism example:")
people = [person1, student1, teacher1]
for person in people:
    introduce_person(person)

# Multiple inheritance example
class Swimmer:
    def swim(self):
        return "Swimming in the pool"
    
    def get_exercise_type(self):
        return "Cardiovascular exercise"

class Runner:
    def run(self):
        return "Running on the track"
    
    def get_exercise_type(self):
        return "Cardiovascular and endurance exercise"

class Triathlete(Swimmer, Runner):
    def __init__(self, name):
        self.name = name
    
    def train(self):
        return f"{self.name} is training: {self.swim()} and {self.run()}"

triathlete = Triathlete("Alex")
print(f"\nMultiple inheritance - {triathlete.train()}")
print(f"Exercise type: {triathlete.get_exercise_type()}")  # Uses first parent's method

print("\nMethod Resolution Order:", Triathlete.__mro__)