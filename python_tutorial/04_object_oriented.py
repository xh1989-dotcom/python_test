"""
Python面向对象编程
==================

本教程介绍Python中的类、对象、继承和多态等面向对象概念
"""

print("=" * 60)
print("Python面向对象编程教程")
print("=" * 60)

# 1. 类和对象基础
print("\n1. 类和对象基础")
print("-" * 60)

class Person:
    """人类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """自我介绍"""
        print(f"大家好，我是{self.name}，今年{self.age}岁")

person1 = Person("张三", 25)
person2 = Person("李四", 30)

person1.introduce()
person2.introduce()

print(f"person1.name = {person1.name}")
print(f"person2.age = {person2.age}")

# 2. 类属性和实例属性
print("\n2. 类属性和实例属性")
print("-" * 60)

class Dog:
    """狗类"""
    species = "犬科"  # 类属性
    
    def __init__(self, name, breed):
        self.name = name  # 实例属性
        self.breed = breed  # 实例属性

dog1 = Dog("旺财", "金毛")
dog2 = Dog("咪咪", "哈士奇")

print(f"Dog.species = {Dog.species}")
print(f"dog1.name = {dog1.name}, dog1.breed = {dog1.breed}")
print(f"dog2.name = {dog2.name}, dog2.breed = {dog2.breed}")

# 3. 类方法
print("\n3. 类方法")
print("-" * 60)

class Circle:
    """圆形类"""
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """计算面积"""
        return self.pi * self.radius ** 2
    
    def circumference(self):
        """计算周长"""
        return 2 * self.pi * self.radius
    
    @classmethod
    def from_diameter(cls, diameter):
        """从直径创建圆形"""
        radius = diameter / 2
        return cls(radius)

circle1 = Circle(5)
print(f"半径为{circle1.radius}的圆:")
print(f"  面积 = {circle1.area():.2f}")
print(f"  周长 = {circle1.circumference():.2f}")

circle2 = Circle.from_diameter(10)
print(f"\n直径为10的圆:")
print(f"  半径 = {circle2.radius}")
print(f"  面积 = {circle2.area():.2f}")

# 4. 静态方法
print("\n4. 静态方法")
print("-" * 60)

class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def add(a, b):
        """加法"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """乘法"""
        return a * b

print(f"MathUtils.add(3, 5) = {MathUtils.add(3, 5)}")
print(f"MathUtils.multiply(4, 6) = {MathUtils.multiply(4, 6)}")

# 5. 继承
print("\n5. 继承")
print("-" * 60)

class Animal:
    """动物基类"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """发出声音"""
        pass

class Dog(Animal):
    """狗类，继承自动物"""
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    """猫类，继承自动物"""
    def speak(self):
        return "喵喵喵"

dog = Dog("旺财")
cat = Cat("咪咪")

print(f"{dog.name}说: {dog.speak()}")
print(f"{cat.name}说: {cat.speak()}")

# 6. 方法重写和super()
print("\n6. 方法重写和super()")
print("-" * 60)

class Vehicle:
    """交通工具基类"""
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def describe(self):
        return f"这是一辆{self.color}的{self.brand}"

class Car(Vehicle):
    """汽车类"""
    def __init__(self, brand, color, seats):
        super().__init__(brand, color)
        self.seats = seats
    
    def describe(self):
        base_desc = super().describe()
        return f"{base_desc}，有{self.seats}个座位"

car = Car("丰田", "白色", 5)
print(car.describe())

# 7. 多重继承
print("\n7. 多重继承")
print("-" * 60)

class Flyable:
    """可飞行的"""
    def fly(self):
        return "会飞"

class Swimmable:
    """可游泳的"""
    def swim(self):
        return "会游泳"

class Duck(Flyable, Swimmable):
    """鸭子类"""
    def __init__(self, name):
        self.name = name

duck = Duck("鸭子")
print(f"{duck.name}: {duck.fly()}, {duck.swim()}")

# 8. 封装
print("\n8. 封装")
print("-" * 60)

class BankAccount:
    """银行账户类"""
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # 私有属性
        self.__balance = initial_balance  # 私有属性
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存款{amount}元，余额{self.__balance}元")
    
    def withdraw(self, amount):
        """取款"""
        if amount > self.__balance:
            print("余额不足")
        elif amount > 0:
            self.__balance -= amount
            print(f"取款{amount}元，余额{self.__balance}元")
    
    def get_balance(self):
        """查询余额"""
        return self.__balance
    
    def get_account_number(self):
        """查询账号"""
        return self.__account_number

account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
print(f"账号: {account.get_account_number()}, 余额: {account.get_balance()}")

# 9. 属性装饰器
print("\n9. 属性装饰器")
print("-" * 60)

class Temperature:
    """温度类"""
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        """获取摄氏度"""
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self.__celsius = value
    
    @property
    def fahrenheit(self):
        """获取华氏度"""
        return self.__celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """设置华氏度"""
        self.__celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"摄氏度: {temp.celsius}°C")
print(f"华氏度: {temp.fahrenheit:.2f}°F")

temp.fahrenheit = 86
print(f"\n设置华氏度为86°F后:")
print(f"摄氏度: {temp.celsius}°C")

# 10. 多态
print("\n10. 多态")
print("-" * 60)

class Shape:
    """形状基类"""
    def area(self):
        pass

class Rectangle(Shape):
    """矩形"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    """三角形"""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Rectangle(5, 4), Triangle(6, 3)]
for shape in shapes:
    print(f"{shape.__class__.__name__}面积: {shape.area()}")

# 11. 魔术方法
print("\n11. 魔术方法")
print("-" * 60)

class Vector:
    """向量类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")

# 12. 实战练习
print("\n12. 实战练习")
print("-" * 60)

# 练习1：学生管理系统
print("练习1：学生管理系统")
class Student:
    """学生类"""
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, subject, score):
        """添加成绩"""
        self.grades.append({"subject": subject, "score": score})
    
    def get_average(self):
        """计算平均分"""
        if not self.grades:
            return 0
        total = sum(grade["score"] for grade in self.grades)
        return total / len(self.grades)
    
    def __str__(self):
        return f"学号: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}, 平均分: {self.get_average():.2f}"

student = Student("1001", "张三", 20)
student.add_grade("数学", 90)
student.add_grade("英语", 85)
student.add_grade("语文", 88)
print(student)

# 练习2：图书管理系统
print("\n练习2：图书管理系统")
class Book:
    """图书类"""
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        """借书"""
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"成功借阅《{self.title}》")
        else:
            print(f"《{self.title}》已被借出")
    
    def return_book(self):
        """还书"""
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"成功归还《{self.title}》")
        else:
            print(f"《{self.title}》未被借出")

book = Book("978-7-111", "Python编程", "张三")
book.borrow()
book.borrow()
book.return_book()

print("\n" + "=" * 60)
print("教程完成！")
print("=" * 60)
