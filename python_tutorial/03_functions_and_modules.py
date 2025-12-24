"""
Python函数和模块
================

本教程介绍Python中的函数定义、参数传递和模块使用
"""

print("=" * 60)
print("Python函数和模块教程")
print("=" * 60)

# 1. 函数基础
print("\n1. 函数基础")
print("-" * 60)

def greet():
    """这是一个简单的问候函数"""
    print("Hello, World!")

print("调用greet():")
greet()

# 2. 带参数的函数
print("\n2. 带参数的函数")
print("-" * 60)

def greet_person(name):
    """向指定的人问好"""
    print(f"Hello, {name}!")

greet_person("张三")
greet_person("李四")

# 3. 带返回值的函数
print("\n3. 带返回值的函数")
print("-" * 60)

def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(3, 5)
print(f"add(3, 5) = {result}")

def multiply(a, b):
    """返回两个数的积"""
    return a * b

print(f"multiply(4, 6) = {multiply(4, 6)}")

# 4. 默认参数
print("\n4. 默认参数")
print("-" * 60)

def greet_with_default(name, greeting="Hello"):
    """使用默认问候语"""
    print(f"{greeting}, {name}!")

greet_with_default("王五")
greet_with_default("赵六", "Hi")

def calculate_area(length, width=1):
    """计算面积，默认宽度为1"""
    return length * width

print(f"calculate_area(5) = {calculate_area(5)}")
print(f"calculate_area(5, 3) = {calculate_area(5, 3)}")

# 5. 关键字参数
print("\n5. 关键字参数")
print("-" * 60)

def describe_pet(name, animal_type="dog"):
    """描述宠物"""
    print(f"{name} 是一只 {animal_type}")

describe_pet("旺财")
describe_pet("咪咪", "cat")
describe_pet(animal_type="bird", name="小鸟")

# 6. 可变参数
print("\n6. 可变参数")
print("-" * 60)

def sum_all(*numbers):
    """求任意数量数字的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20) = {sum_all(10, 20)}")

def print_info(**info):
    """打印任意数量的键值对"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("print_info(name='张三', age=25, city='北京'):")
print_info(name="张三", age=25, city="北京")

# 7. 函数返回多个值
print("\n7. 函数返回多个值")
print("-" * 60)

def get_name_age():
    """返回姓名和年龄"""
    return "张三", 25

name, age = get_name_age()
print(f"姓名: {name}, 年龄: {age}")

def calculate_stats(numbers):
    """计算统计信息"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

nums = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = calculate_stats(nums)
print(f"列表: {nums}")
print(f"最小值: {min_val}, 最大值: {max_val}, 平均值: {avg_val}")

# 8. 函数作为参数
print("\n8. 函数作为参数")
print("-" * 60)

def apply_operation(x, y, operation):
    """应用指定的运算"""
    return operation(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(f"apply_operation(10, 5, add) = {apply_operation(10, 5, add)}")
print(f"apply_operation(10, 5, subtract) = {apply_operation(10, 5, subtract)}")

# 9. lambda函数
print("\n9. lambda函数（匿名函数）")
print("-" * 60)

square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

add = lambda a, b: a + b
print(f"add(3, 4) = {add(3, 4)}")

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"map(lambda x: x**2, {numbers}) = {squared}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x%2==0, {numbers}) = {even_numbers}")

# 10. 递归函数
print("\n10. 递归函数")
print("-" * 60)

def factorial(n):
    """计算阶乘"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")

def fibonacci(n):
    """斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(10) = {fibonacci(10)}")

# 11. 变量作用域
print("\n11. 变量作用域")
print("-" * 60)

x = "全局变量"

def test_scope():
    x = "局部变量"
    print(f"  函数内: {x}")

test_scope()
print(f"  函数外: {x}")

def use_global():
    global x
    x = "修改后的全局变量"
    print(f"  函数内修改: {x}")

use_global()
print(f"  函数外: {x}")

# 12. 装饰器基础
print("\n12. 装饰器基础")
print("-" * 60)

def my_decorator(func):
    """简单的装饰器"""
    def wrapper():
        print("  函数执行前...")
        func()
        print("  函数执行后...")
    return wrapper

@my_decorator
def say_hello():
    print("    Hello!")

print("使用装饰器的函数:")
say_hello()

# 13. 模块使用
print("\n13. 模块使用")
print("-" * 60)

import math
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pow(2, 3) = {math.pow(2, 3)}")

import random
print(f"\nrandom.randint(1, 10) = {random.randint(1, 10)}")
print(f"random.choice(['a', 'b', 'c']) = {random.choice(['a', 'b', 'c'])}")

from datetime import datetime
print(f"\n当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 14. 实战练习
print("\n14. 实战练习")
print("-" * 60)

# 练习1：计算器
print("练习1：简单计算器")
def calculator(a, b, operation):
    """简单计算器"""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "错误：除数不能为0"
    else:
        return "错误：不支持的运算"

print(f"calculator(10, 5, '+') = {calculator(10, 5, '+')}")
print(f"calculator(10, 5, '-') = {calculator(10, 5, '-')}")
print(f"calculator(10, 5, '*') = {calculator(10, 5, '*')}")
print(f"calculator(10, 5, '/') = {calculator(10, 5, '/')}")

# 练习2：验证密码强度
print("\n练习2：验证密码强度")
def check_password_strength(password):
    """检查密码强度"""
    if len(password) < 8:
        return "弱：密码长度至少8位"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score == 4:
        return "强：密码非常安全"
    elif score >= 2:
        return "中：密码强度一般"
    else:
        return "弱：密码需要改进"

print(f"check_password_strength('abc123') = {check_password_strength('abc123')}")
print(f"check_password_strength('Abc123!@') = {check_password_strength('Abc123!@')}")

# 练习3：生成随机密码
print("\n练习3：生成随机密码")
import string

def generate_password(length=12):
    """生成随机密码"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(f"generate_password(8) = {generate_password(8)}")
print(f"generate_password(12) = {generate_password(12)}")

print("\n" + "=" * 60)
print("教程完成！")
print("=" * 60)
