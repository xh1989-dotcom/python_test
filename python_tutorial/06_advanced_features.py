"""
Python高级特性
==============

本教程介绍Python中的高级特性，包括列表推导式、生成器、装饰器等
"""

print("=" * 60)
print("Python高级特性教程")
print("=" * 60)

# 1. 列表推导式
print("\n1. 列表推导式")
print("-" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 基本列表推导式
squares = [x**2 for x in numbers]
print(f"平方数: {squares}")

# 带条件的列表推导式
evens = [x for x in numbers if x % 2 == 0]
print(f"偶数: {evens}")

# 嵌套列表推导式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3矩阵: {matrix}")

# 多条件列表推导式
filtered = [x for x in numbers if x > 5 and x < 9]
print(f"大于5小于9: {filtered}")

# 2. 字典推导式
print("\n2. 字典推导式")
print("-" * 60)

squares_dict = {x: x**2 for x in range(5)}
print(f"平方字典: {squares_dict}")

# 带条件的字典推导式
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"偶数平方字典: {even_squares}")

# 字典转换
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"键值互换: {swapped}")

# 3. 集合推导式
print("\n3. 集合推导式")
print("-" * 60)

squares_set = {x**2 for x in range(5)}
print(f"平方集合: {squares_set}")

# 去重
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers_with_dupes}
print(f"去重后: {unique}")

# 4. 生成器表达式
print("\n4. 生成器表达式")
print("-" * 60)

# 生成器表达式（节省内存）
gen = (x**2 for x in range(10))
print(f"生成器: {gen}")
print(f"生成器元素: {list(gen)}")

# 与列表推导式的区别
import sys
list_comp = [x**2 for x in range(1000000)]
gen_exp = (x**2 for x in range(1000000))
print(f"列表推导式内存: {sys.getsizeof(list_comp)} 字节")
print(f"生成器表达式内存: {sys.getsizeof(gen_exp)} 字节")

# 5. 生成器函数
print("\n5. 生成器函数")
print("-" * 60)

def count_up_to(n):
    """计数生成器"""
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
print(f"生成器: {counter}")
print(f"next(counter): {next(counter)}")
print(f"next(counter): {next(counter)}")
print(f"剩余: {list(counter)}")

# 斐波那契数列生成器
def fibonacci(n):
    """斐波那契数列生成器"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"斐波那契数列前10项: {list(fibonacci(10))}")

# 6. 迭代器
print("\n6. 迭代器")
print("-" * 60)

class Countdown:
    """倒计时迭代器"""
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

countdown = Countdown(5)
for num in countdown:
    print(f"  {num}")

# 7. 装饰器
print("\n7. 装饰器")
print("-" * 60)

def timer(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.6f}秒")
        return result
    return wrapper

@timer
def slow_function():
    """慢函数"""
    import time
    time.sleep(0.1)
    return "完成"

slow_function()

# 带参数的装饰器
def repeat(times):
    """重复执行装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    """问候"""
    print("  Hello!")

print("重复3次:")
greet()

# 8. 类装饰器
print("\n8. 类装饰器")
print("-" * 60)

class CountCalls:
    """计数装饰器类"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    """说你好"""
    print("  Hello!")

say_hello()
say_hello()

# 9. functools.wraps
print("\n9. functools.wraps")
print("-" * 60)

from functools import wraps

def debug(func):
    """调试装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    """加法函数"""
    return a + b

add(3, 5)
print(f"函数名: {add.__name__}")
print(f"文档字符串: {add.__doc__}")

# 10. 闭包
print("\n10. 闭包")
print("-" * 60)

def make_multiplier(factor):
    """创建乘法器"""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# 计数器闭包
def make_counter():
    """创建计数器"""
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(f"counter() = {counter()}")
print(f"counter() = {counter()}")
print(f"counter() = {counter()}")

# 11. 高阶函数
print("\n11. 高阶函数")
print("-" * 60)

# map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"map: {squared}")

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter: {evens}")

# reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"reduce: {product}")

# sorted with key
students = [("张三", 85), ("李四", 92), ("王五", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"sorted: {sorted_students}")

# 12. 偏函数
print("\n12. 偏函数")
print("-" * 60)

from functools import partial

def power(base, exponent):
    """幂运算"""
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5) = {square(5)}")
print(f"cube(5) = {cube(5)}")

# 13. 实战练习
print("\n13. 实战练习")
print("-" * 60)

# 练习1：数据清洗
print("练习1：数据清洗")
data = ["  hello  ", "  WORLD  ", "  PyThOn  ", "  "]
cleaned = [s.strip().lower() for s in data if s.strip()]
print(f"原始数据: {data}")
print(f"清洗后: {cleaned}")

# 练习2：日志装饰器
print("\n练习2：日志装饰器")
def log_function(func):
    """日志装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 执行 {func.__name__}")
        try:
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} 成功")
            return result
        except Exception as e:
            print(f"[LOG] {func.__name__} 失败: {e}")
            raise

@log_function
def divide(a, b):
    """除法"""
    return a / b

divide(10, 2)
divide(10, 0)

# 练习3：缓存装饰器
print("\n练习3：缓存装饰器")
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_cached(n):
    """带缓存的斐波那契"""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print(f"fibonacci_cached(30) = {fibonacci_cached(30)}")
print(f"缓存信息: {fibonacci_cached.cache_info()}")

# 练习4：数据管道
print("\n练习4：数据管道")
def filter_positive(numbers):
    """过滤正数"""
    return [n for n in numbers if n > 0]

def square_numbers(numbers):
    """平方"""
    return [n**2 for n in numbers]

def sum_numbers(numbers):
    """求和"""
    return sum(numbers)

def pipeline(data, *functions):
    """数据管道"""
    result = data
    for func in functions:
        result = func(result)
    return result

data = [-2, -1, 0, 1, 2, 3]
result = pipeline(data, filter_positive, square_numbers, sum_numbers)
print(f"数据: {data}")
print(f"结果: {result}")

# 练习5：生成器处理大文件
print("\n练习5：生成器处理大文件")
def read_large_file(filename):
    """逐行读取大文件"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return

def process_lines(lines):
    """处理行"""
    for i, line in enumerate(lines, 1):
        if i <= 3:
            print(f"  行{i}: {line[:50]}...")

# 创建测试文件
with open("large_file.txt", "w", encoding="utf-8") as f:
    for i in range(100):
        f.write(f"这是第{i+1}行内容，包含一些测试数据\n")

lines = read_large_file("large_file.txt")
process_lines(lines)

# 清理
import os
os.remove("large_file.txt")

print("\n" + "=" * 60)
print("教程完成！")
print("=" * 60)
